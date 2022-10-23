from MinHeap import *

iterations = 0
total_num_of_states = 1

def expand(node: Node):
    global total_num_of_states
    newNode = Node(node.queens, node.g)
    for i in range (NUM):
        for j in range (1, NUM):
            newNode.addChildByChangingParent(i, j)
    total_num_of_states += NUM * (NUM - 1)
    return newNode

def A_star(root: Node):
    global total_num_of_states, iterations
    U = []
    Q = MinHeap(B)
    Q.insert(root)
    while Q.size != 0:
        current = Q.remove()
        if current.h == 0:
            return current, iterations, total_num_of_states, Q.size + len(U) + 1
        U.append(current)
        for v in expand(current).childs:
            pathCost = current.g + D
            if v in U and pathCost >= v.g:
                continue
            if not v in U or pathCost < v.g:
                current.addChild(v.queens)
                if not v in Q:
                    Q.insert(v)
        iterations += 1
    return None, iterations, total_num_of_states, Q.size + len(U) + 1
