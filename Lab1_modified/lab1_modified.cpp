#pragma warning(disable : 4996)
#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include "stdio.h"
#include <ctime>
#include <algorithm>
using namespace std;

constexpr auto MAX_LENTH = 20000000;

// Сортування збалансованим багатошляховим злиттям.
int multiwayMerge(string, string);
// Розподіл вхідного файлу по допоміжних файлах розміром, що не перевищує 100 Мб.
int splitFile(FILE*);
// Злиття допоміжних файлів у кінцевий файл.
void mergeFiles(int, FILE*);
// Видалення допоміжних файлів.
void deleteFiles(int);
// Пошук номеру найменшого елемента послідовності.
int findNumOfMin(vector<int>&);

int main()
{
    string path1 = "start_file_5.txt";
    string path2 = "end_file_5.txt";
    clock_t start = clock();
    if (multiwayMerge(path1, path2)) {
        cout << "Can't open start file!\n";
        return 1;
    }
    double duration = (clock() - start) / CLOCKS_PER_SEC;
    cout << "Duration: " << duration << " seconds.\n";
    return 0;
}

int multiwayMerge(string path1, string path2)
{
    FILE* start_file = fopen(path1.c_str(), "rt");
    if (start_file == NULL) {
        return 1;
    }
    int num_of_files = splitFile(start_file);
    fclose(start_file);

    FILE* end_file = fopen(path2.c_str(), "wt");
    mergeFiles(num_of_files, end_file);
    fclose(end_file);

    deleteFiles(num_of_files);
    return 0;
}

int splitFile(FILE* file)
{
    int* mas = new int[MAX_LENTH];
    int i, n = 0;
    while (!feof(file)) {
        for (i = 0; i < MAX_LENTH; i++) {
            if (feof(file)) {
                break;
            }
            fscanf(file, "%i", &mas[i]);
        }
        sort(mas, mas + i);
        FILE* B = fopen(("B" + to_string(n) + ".dat").c_str(), "wb");
        fwrite(mas, sizeof(int), i, B);
        fclose(B);
        n++;
    }
    delete[] mas;
    return n;
}

void mergeFiles(int num_of_files, FILE* file)
{
    int k, n;
    vector<int> nums;
    vector<FILE*> B(num_of_files);
    for (int i = 0; i < num_of_files; ++i) {
        B[i] = fopen(("B" + to_string(i) + ".dat").c_str(), "rb");
    }
    for (int i = 0; i < num_of_files; ++i) {
        k = INT_MAX;
        fread(&k, sizeof(int), 1, B[i]);
        nums.push_back(k);
    }
    n = findNumOfMin(nums);
    k = nums[n];
    int i = 0;
    fprintf(file, "%i ", k);
    while (true) {
        nums[n] = INT_MAX;
        fread(&nums[n], sizeof(int), 1, B[n]);
        n = findNumOfMin(nums);
        k = nums[n];
        if (k == INT_MAX) {
            break;
        }
        fprintf(file, "%i ", k);
    }
    for (int i = 0; i < num_of_files; ++i) {
        fclose(B[i]);
    }
}

void deleteFiles(int num_of_files)
{
    for (int i = 0; i < num_of_files; ++i) {
        remove(("B" + to_string(i) + ".dat").c_str());
    }
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
