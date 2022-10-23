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
    closed = []
    opened = MinHeap(B)
    opened.insert(root)
    while opened.size != 0:
        current = opened.remove()
        if current.h == 0:
            return current, iterations, total_num_of_states, opened.size + len(closed) + 1
        closed.append(current)
        for child in expand(current).childs:
            pathCost = current.g + D
            if child in closed and pathCost >= child.g:
                continue
            if not child in closed or pathCost < child.g:
                current.addChild(child.queens)
                if not child in opened:
                    opened.insert(child)
        iterations += 1
    return None, iterations, total_num_of_states, opened.size + len(closed) + 1
