from Node import *

total_num_of_states = 1
num_of_states_in_mem = 0

def isAGoalState(queens: list):
    for i in range(NUM):
        for j in range(i + 1, NUM):
            if queens[i] == queens[j] or queens[i] == queens[j] + j - i or queens[i] == queens[j] - j + i:
                return False
    return True

def expand(node: Node):
    global num_of_states_in_mem
    newNode = Node(node.queens)
    for i in range (NUM):
        for j in range (1, NUM):
            newNode.addChild(i, j)
    num_of_states_in_mem += NUM * (NUM - 1)
    return newNode

def IDFS(root: Node):
    global total_num_of_states, num_of_states_in_mem
    depth = 0
    max_num_of_states_in_mem = 0
    while True:
        result = DLS(root, depth)
        total_num_of_states += num_of_states_in_mem
        if num_of_states_in_mem > max_num_of_states_in_mem:
            max_num_of_states_in_mem = num_of_states_in_mem
        if result != None and isAGoalState(result.queens):
            return result, depth, total_num_of_states, max_num_of_states_in_mem + 1
        depth += 1
        num_of_states_in_mem = 0

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
