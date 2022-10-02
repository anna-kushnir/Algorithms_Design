#include <iostream>
#include <string>
#include <fstream>
#include <vector>
using namespace std;

#define NUM_OF_FILES 8

vector<string> createFileNames(string, int);
int findNumOfMin(vector<int>&);
int splitInputFile(vector<string>&, ifstream&);
void mergeAndSplitFiles(vector<string>&, vector<string>&);
int sortingFiles(vector<string>&, vector<string>&, int num);
void convertBinToText(string, string);
void deleteFiles(vector<string>);

int main()
{
    string path1 = "start_file_0.txt";
    string path2 = "end_file_1.txt";

    ifstream file(path1);
    if (!file.is_open()) {
        return 1;
    }
    vector<string> pathsB = createFileNames("B", NUM_OF_FILES);
    vector<string> pathsC = createFileNames("C", NUM_OF_FILES);
    int num = splitInputFile(pathsB, file);
    file.close();

    int flag = sortingFiles(pathsB, pathsC, num);
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

int splitInputFile(vector<string>& paths, ifstream& file)
{
    int k, m, i = 0, num = 0;
    file >> k;
    num++;
    ofstream B;
    for (int i = 0; i < NUM_OF_FILES; ++i) {
        B.open(paths[i], ios::binary);
        B.close();
    }
    B.open(paths[i], ios::binary);
    B.write((char*)&k, sizeof(int));
    while (!file.eof()) {
        file >> m;
        num++;
        if (k > m) {
            B.close();
            i++;
            if (i == NUM_OF_FILES) {
                i = 0;
            }
            B.open(paths[i], ios::binary | ios::app);
        }
        B.write((char*)&m, sizeof(int));
        k = m;
    }
    B.close();
    return num;
}

void mergeAndSplitFiles(vector<string>& pathsB, vector<string>& pathsC)
{
    vector<int> nums, pos;
    ifstream B;
    int k, m, n;
    for (int i = 0; i < NUM_OF_FILES; ++i) {
        B.open(pathsB[i], ios::binary);
        k = INT_MAX;
        B.read((char*)&k, sizeof(int));
        nums.push_back(k);
        pos.push_back(0);
        B.close();
    }
    n = findNumOfMin(nums);
    k = nums[n];
    pos[n]++;
    int i = 0;
    ofstream C;
    for (int i = 0; i < NUM_OF_FILES; ++i) {
        C.open(pathsC[i], ios::binary);
        C.close();
    }
    C.open(pathsC[0], ios::binary);
    C.write((char*)&k, sizeof(int));
    while (true) {
        B.open(pathsB[n], ios::binary);
        B.seekg(0, ios::end);
        if (pos[n] * sizeof(int) < B.tellg()) {
            B.seekg(pos[n] * sizeof(int));
            B.read((char*)&nums[n], sizeof(int));
        }
        else {
            nums[n] = INT_MAX;
        }
        B.close();
        n = findNumOfMin(nums);
        m = nums[n];
        pos[n]++;
        if (m == INT_MAX) {
            break;
        }
        if (k > m) {
            i++;
            if (i == NUM_OF_FILES) {
                i = 0;
            }
            C.close();
            C.open(pathsC[i], ios::binary | ios::app);
        }
        C.write((char*)&m, sizeof(int));
        k = m;
    }
}

int sortingFiles(vector<string>& pathsB, vector<string>& pathsC, int num)
{
    int i = 0;
    while (true) {
        if (i % 2 == 0) {
            mergeAndSplitFiles(pathsB, pathsC);
            ifstream C(pathsC[0], ios::binary);
            C.seekg(0, ios::end);
            if (num * sizeof(int) == C.tellg()) {
                return 2;
            }
            C.close();
        }
        else {
            mergeAndSplitFiles(pathsC, pathsB);
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

void deleteFiles(vector<string> paths)
{
    for (int i = 0; i < paths.size(); ++i) {
        remove(paths[i].c_str());
    }
}
