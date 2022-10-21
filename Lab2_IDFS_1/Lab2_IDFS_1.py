

def isAGoalState(queens):
    for i in range(8):
        for j in range(i + 1, 8):
            if queens[i] == queens[j] or queens[i] == queens[j] + j - i or queens[i] == queens[j] - j + i:
                return False
    return True



