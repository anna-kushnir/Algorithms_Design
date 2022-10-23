from Node import *

total_num_of_states = 1

def isAGoalState(queens: list):
    for i in range(NUM):
        for j in range(i + 1, NUM):
            if queens[i] == queens[j] or queens[i] == queens[j] + j - i or queens[i] == queens[j] - j + i:
                return False
    return True

def expand(node: Node):
    global total_num_of_states
    newNode = Node(node.queens)
    for i in range (NUM):
        for j in range (1, NUM):
            newNode.addChild(i, j)
    total_num_of_states += NUM * (NUM - 1)
    return newNode

def IDFS(root: Node):
    depth = 0
    while True:
        result = DLS(root, depth)
        if result != None and isAGoalState(result.queens):
            return result, depth, total_num_of_states, depth * NUM * (NUM - 1)
        depth += 1

def DLS(node: Node, depth: int):
    if depth == 0 and isAGoalState(node.queens):
        return node
    elif depth > 0:
        for child in expand(node).childs:
            result = DLS(child, depth - 1)
            if result != None:
                return result
    else:
        return None
