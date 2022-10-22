NUM = 8

class Node:
    def __init__(self, queens: list):
        self.queens = queens
        self.childs = []

    def addChild(self, i: int, j: int):
        queens = []
        for k in range(NUM):
             queens.append(self.queens[k])
        queens[i] = (queens[i] + j) % NUM
        self.childs.append(Node(queens))
        return
