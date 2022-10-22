NUM = 8
D = 1

class Node:
    def __init__(self, queens: list, g: int = 0):
        self.queens = queens
        self.childs : list[Node] = []
        self.h = self.countConflicts()
        self.g = g
        self.f = self.g + self.h

    def changeG(self, new_g):
        self.g = new_g
        self.f = self.g + self.h

    def addChildByChangingParent(self, i: int, j: int):
        queens = []
        for k in range(NUM):
             queens.append(self.queens[k])
        queens[i] = (queens[i] + j) % NUM
        self.childs.append(Node(queens, self.g + D))
        return

    def addChild(self, queens: list):
        self.childs.append(Node(queens, self.g + D))

    def countConflicts(self):
        conflicts = 0
        for i in range(NUM):
            for j in range(i + 1, NUM):
                if self.queens[i] == self.queens[j]:
                    conflicts += 1
                    for k in range(i + 1, j):
                        if self.queens[i] == self.queens[k]:
                            conflicts -= 1
                            break
                if self.queens[i] == self.queens[j] + j - i:
                    conflicts += 1
                    for k in range(i + 1, j):
                        if self.queens[i] == self.queens[k] + k - i:
                            conflicts -= 1
                            break
                if self.queens[i] == self.queens[j] - j + i:
                    conflicts += 1
                    for k in range(i + 1, j):
                        if self.queens[i] == self.queens[k] - k + i:
                            conflicts -= 1
                            break
        return conflicts
