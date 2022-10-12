﻿#pragma warning(disable : 4996)
#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include "stdio.h"
#include <ctime>
#include <algorithm>
using namespace std;

constexpr auto MAX_LENTH = 13000000;

// Сортування збалансованим багатошляховим злиттям.
bool multiwayMerge(string, string);
// Розподіл вхідного файлу по допоміжних файлах розміром, що не перевищує 78 Мб.
int splitFile(FILE*);
// Злиття допоміжних файлів у кінцевий файл.
void mergeFiles(int, FILE*);
// Видалення допоміжних файлів.
void deleteFiles(int);
// Пошук номеру найменшого елемента послідовності.
int findNumOfMin(vector<long long>&);

int main()
{
    string path1 = "start_file_1.dat";
    string path2 = "end_file_1.dat";
    clock_t start = clock();
    if (multiwayMerge(path1, path2)) {
        cout << "Can't open start file!\n";
        return 1;
    }
    double duration = (clock() - start) / CLOCKS_PER_SEC;
    cout << "Duration: " << duration << " seconds.\n";
    return 0;
}

bool multiwayMerge(string path1, string path2)
{
    FILE* start_file = fopen(path1.c_str(), "rb");
    if (start_file == NULL) {
        return 1;
    }
    int num_of_files = splitFile(start_file);
    fclose(start_file);

    FILE* end_file = fopen(path2.c_str(), "wb");
    mergeFiles(num_of_files, end_file);
    fclose(end_file);

    deleteFiles(num_of_files);
    return 0;
}

int splitFile(FILE* file)
{
    int n = 0;
    while (true) {
        long long* mas = new long long[MAX_LENTH];
        long lenth = fread(mas, sizeof(long long), MAX_LENTH, file);
        sort(mas, mas + lenth);
        FILE* B = fopen(("B" + to_string(n) + ".dat").c_str(), "wb");
        fwrite(mas, sizeof(long long), lenth, B);
        fclose(B);
        delete[] mas;
        n++;
        if (lenth < MAX_LENTH) {
            break;
        }
    }
    return n;
}

void mergeFiles(int num_of_files, FILE* file)
{
    int n;
    long long k;
    long long* mas = new long long[MAX_LENTH];
    vector<long long> nums;
    vector<FILE*> B(num_of_files);
    for (int i = 0; i < num_of_files; ++i) {
        B[i] = fopen(("B" + to_string(i) + ".dat").c_str(), "rb");
    }
    for (int i = 0; i < num_of_files; ++i) {
        k = LLONG_MAX;
        fread(&k, sizeof(long long), 1, B[i]);
        nums.push_back(k);
    }
    n = findNumOfMin(nums);
    k = nums[n];
    mas[0] = k;
    int lenth = 1;
    while (true) {
        if (lenth == MAX_LENTH) {
            fwrite(mas, sizeof(long long), lenth, file);
            lenth = 0;
        }
        nums[n] = LLONG_MAX;
        fread(&nums[n], sizeof(long long), 1, B[n]);
        n = findNumOfMin(nums);
        k = nums[n];
        if (k == LLONG_MAX) {
            fwrite(mas, sizeof(long long), lenth, file);
            break;
        }
        mas[lenth] = k;
        lenth++;
    }
    delete[] mas;
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

int findNumOfMin(vector<long long>& nums)
{
    int j = 0;
    for (int i = 1; i < nums.size(); ++i) {
        if (nums[i] < nums[j]) {
            j = i;
        }
    }
    return j;
}
