#pragma warning(disable : 4996)
#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include "stdio.h"
#include <ctime>
using namespace std;

constexpr auto NUM_OF_FILES = 16;

// Сортування збалансованим багатошляховим злиттям.
int multiwayMerge(string, string);
// Створення масиву (вектору) назв файлів.
vector<string> createFileNames(string);
// Пошук номеру найменшого елемента послідовності.
int findNumOfMin(vector<int>&);
// Почергове злиття файлів B1, B2, ..., Bm у файли C1, C2, ..., Cm і навпаки, поки у B1 або C1 не утвориться одна серія.
int alternateMergingOfFiles(vector<string>&, vector<string>&, int);
// Розподіл серій вхідного файлу по m допоміжних файлах (B1, B2, ..., Bm).
int splitInputFile(vector<string>&, FILE*);
// Злиття файлів B1, B2, ..., Bm у файли C1, C2, ..., Cm.
void mergeFiles(vector<string>&, vector<string>&);
// Перетворення бінарного файлу у текстовий.
void convertBinToText(string, string);
// Видалення допоміжних файлів.
void deleteFiles(vector<string>&);

int main()
{
    string path1 = "start_file.txt";
    string path2 = "end_file.txt";
    clock_t start = clock();
    if (multiwayMerge(path1, path2)) {
        return 1;
    }
    double duration = (clock() - start) / CLOCKS_PER_SEC;
    cout << "Duration: " << duration << " seconds.\n";
    return 0;
}

int multiwayMerge(string path1, string path2)
{
    FILE* file;
    file = fopen(path1.c_str(), "rt");
    if (file == NULL) {
        return 1;
    }
    vector<string> pathsB = createFileNames("B");
    vector<string> pathsC = createFileNames("C");
    int num = splitInputFile(pathsB, file);
    fclose(file);

    int flag = alternateMergingOfFiles(pathsB, pathsC, num);

    if (flag == 1) {
        convertBinToText(pathsB[0], path2);
    }
    else {
        convertBinToText(pathsC[0], path2);
    }
    deleteFiles(pathsB);
    deleteFiles(pathsC);
    return 0;
}

vector<string> createFileNames(string name)
{
    vector<string> paths(NUM_OF_FILES);
    for (int i = 0; i < NUM_OF_FILES; ++i) {
        paths[i] = name + to_string(i) + ".dat";
    }
    return paths;
}

int findNumOfMin(vector<int>& nums)
{
    int j = 0;
    for (int i = 1; i < nums.size(); ++i) {
        if (nums[i] < nums[j]) {
            j = i;
        }
    }
    return j;
}

int alternateMergingOfFiles(vector<string>& pathsB, vector<string>& pathsC, int num)
{
    int i = 0;
    while (true) {
        if (i % 2 == 0) {
            mergeFiles(pathsB, pathsC);
            ifstream C(pathsC[0], ios::binary);
            C.seekg(0, ios::end);
            if (num * sizeof(int) == C.tellg()) {
                return 2;
            }
            C.close();
        }
        else {
            mergeFiles(pathsC, pathsB);
            ifstream B(pathsB[0], ios::binary);
            B.seekg(0, ios::end);
            if (num * sizeof(int) == B.tellg()) {
                return 1;
            }
            B.close();
        }
        i++;
    }
}

int splitInputFile(vector<string>& paths, FILE* file)
{
    int k, m, i = 0, num = 0;
    fscanf(file, "%i", &k);
    num++;
    vector<FILE*> B(NUM_OF_FILES);
    for (int i = 0; i < NUM_OF_FILES; ++i) {
        B[i] = fopen(paths[i].c_str(), "wb");
    }
    fwrite(&k, sizeof(int), 1, B[0]);

    while (!feof(file)) {
        fscanf(file, "%i", &m);
        num++;
        if (k > m) {
            i++;
            if (i == NUM_OF_FILES) {
                i = 0;
            }
        }
        fwrite(&m, sizeof(int), 1, B[i]);
        k = m;
    }
    for (int i = 0; i < NUM_OF_FILES; ++i) {
        fclose(B[i]);
    }
    return num;
}

void mergeFiles(vector<string>& pathsB, vector<string>& pathsC)
{
    vector<int> nums;
    vector<FILE*> B(NUM_OF_FILES), C(NUM_OF_FILES);
    for (int i = 0; i < NUM_OF_FILES; ++i) {
        B[i] = fopen(pathsB[i].c_str(), "rb");
        C[i] = fopen(pathsC[i].c_str(), "wb");
    }
    int k, m, n;
    for (int i = 0; i < NUM_OF_FILES; ++i) {
        k = INT_MAX;
        fread(&k, sizeof(int), 1, B[i]);
        nums.push_back(k);
    }
    n = findNumOfMin(nums);
    k = nums[n];
    int i = 0;
    fwrite(&k, sizeof(int), 1, C[0]);
    while (true) {
        nums[n] = INT_MAX;
        fread(&nums[n], sizeof(int), 1, B[n]);
        n = findNumOfMin(nums);
        m = nums[n];
        if (m == INT_MAX) {
            break;
        }
        if (k > m) {
            i++;
            if (i == NUM_OF_FILES) {
                i = 0;
            }
        }
        fwrite(&m, sizeof(int), 1, C[i]);
        k = m;
    }
    for (int i = 0; i < NUM_OF_FILES; ++i) {
        fclose(B[i]);
        fclose(C[i]);
    }
}

void convertBinToText(string pathBin, string pathTxt)
{
    FILE* bin, *txt;
    bin = fopen(pathBin.c_str(), "rb");
    txt = fopen(pathTxt.c_str(), "wt");
    int i = 0, k;
    while (fread(&k, sizeof(int), 1, bin)) {
        fprintf(txt, "%i ", k);
        i++;
        k = false;
    }
    fclose(txt);
    fclose(bin);
}

void deleteFiles(vector<string>& paths)
{
    for (int i = 0; i < paths.size(); ++i) {
        remove(paths[i].c_str());
    }
}
