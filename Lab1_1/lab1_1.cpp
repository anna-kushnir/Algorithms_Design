#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <ctime>
using namespace std;

constexpr auto NUM_OF_FILES = 4;

// Сортування збалансованим багатошляховим злиттям.
int multiwayMerge(string, string);
// Створення масиву (вектору) назв файлів.
vector<string> createFileNames(string, int);
// Пошук номеру найменшого елемента послідовності.
int findNumOfMin(vector<int>&);
// Почергове злиття файлів B1, B2, ..., Bm у файли C1, C2, ..., Cm і навпаки, поки у B1 або C1 не утвориться одна серія.
int alternateMergingOfFiles(vector<string>&, vector<string>&, int);
// Розподіл серій вхідного файлу по m допоміжних файлах (B1, B2, ..., Bm).
int splitInputFile(vector<string>&, ifstream&);
// Злиття файлів B1, B2, ..., Bm у файли C1, C2, ..., Cm.
void mergeFiles(vector<string>&, vector<string>&);
// Перетворення бінарного файлу у текстовий.
void convertBinToText(string, string);
// Видалення допоміжних файлів.
void deleteFiles(vector<string>&);

int main()
{
    string path1 = "start_file_1.txt";
    string path2 = "end_file_1.txt";
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
    ifstream file(path1);
    if (!file.is_open()) {
        return 1;
    }
    vector<string> pathsB = createFileNames("B", NUM_OF_FILES);
    vector<string> pathsC = createFileNames("C", NUM_OF_FILES);
    int num = splitInputFile(pathsB, file);
    file.close();

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

vector<string> createFileNames(string name, int num)
{
    vector<string> paths;
    for (int i = 0; i < num; ++i) {
        paths.push_back(name + to_string(i) + ".dat");
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

int splitInputFile(vector<string>& paths, ifstream& file)
{
    int k, m, i = 0, num = 0;
    file >> k;
    num++;
    ofstream
        B0(paths[0], ios::binary),
        B1(paths[1], ios::binary),
        B2(paths[2], ios::binary),
        B3(paths[3], ios::binary);
    B0.write((char*)&k, sizeof(int));
    while (!file.eof()) {
        file >> m;
        num++;
        if (k > m) {
            i++;
            if (i == NUM_OF_FILES) {
                i = 0;
            }
        }
        switch (i) {
        case 0:
            B0.write((char*)&m, sizeof(int));
            break;
        case 1:
            B1.write((char*)&m, sizeof(int));
            break;
        case 2:
            B2.write((char*)&m, sizeof(int));
            break;
        case 3:
            B3.write((char*)&m, sizeof(int));
        }
        k = m;
    }
    B0.close();
    B1.close();
    B2.close();
    B3.close();
    return num;
}

void mergeFiles(vector<string>& pathsB, vector<string>& pathsC)
{
    vector<int> nums;
    ifstream
        B0(pathsB[0], ios::binary),
        B1(pathsB[1], ios::binary),
        B2(pathsB[2], ios::binary),
        B3(pathsB[3], ios::binary);
    ofstream
        C0(pathsC[0], ios::binary),
        C1(pathsC[1], ios::binary),
        C2(pathsC[2], ios::binary),
        C3(pathsC[3], ios::binary);
    int k, m, n;
    for (int i = 0; i < NUM_OF_FILES; ++i) {
        k = INT_MAX;
        switch (i) {
        case 0:
            B0.read((char*)&k, sizeof(int));
            break;
        case 1:
            B1.read((char*)&k, sizeof(int));
            break;
        case 2:
            B2.read((char*)&k, sizeof(int));
            break;
        case 3:
            B3.read((char*)&k, sizeof(int));
        }
        nums.push_back(k);
    }
    n = findNumOfMin(nums);
    k = nums[n];
    int i = 0;
    C0.write((char*)&k, sizeof(int));
    while (true) {
        nums[n] = INT_MAX;
        switch (n) {
        case 0:
            B0.read((char*)&nums[n], sizeof(int));
            break;
        case 1:
            B1.read((char*)&nums[n], sizeof(int));
            break;
        case 2:
            B2.read((char*)&nums[n], sizeof(int));
            break;
        case 3:
            B3.read((char*)&nums[n], sizeof(int));
        }
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
        switch (i) {
        case 0:
            C0.write((char*)&m, sizeof(int));
            break;
        case 1:
            C1.write((char*)&m, sizeof(int));
            break;
        case 2:
            C2.write((char*)&m, sizeof(int));
            break;
        case 3:
            C3.write((char*)&m, sizeof(int));
        }
        k = m;
    }
    B0.close();
    B1.close();
    B2.close();
    B3.close();
    C0.close();
    C1.close();
    C2.close();
    C3.close();
}

void convertBinToText(string pathBin, string pathTxt)
{
    ifstream bin(pathBin, ios::binary);
    bin.seekg(0, ios::end);
    int lenth = bin.tellg(), i = 0;
    ofstream txt(pathTxt);
    bin.seekg(0, ios::beg);
    while (i * sizeof(int) < lenth) {
        int k;
        bin.read((char*)&k, sizeof(int));
        txt << k << " ";
        i++;
    }
    txt.close();
    bin.close();
}

void deleteFiles(vector<string>& paths)
{
    for (int i = 0; i < paths.size(); ++i) {
        remove(paths[i].c_str());
    }
}
