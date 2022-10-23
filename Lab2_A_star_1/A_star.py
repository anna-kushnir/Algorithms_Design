from MinHeap import *

def expand(node: Node):
    newNode = Node(node.queens, node.g)
    for i in range (NUM):
        for j in range (1, NUM):
            newNode.addChildByChangingParent(i, j)
    return newNode

def A_star(root: Node):
    closed = []
    opened = MinHeap(B)
    opened.insert(root)
    while opened.size != 0:
        current = opened.remove()
        if current.h == 0:
            return current
        closed.append(current)
        for child in expand(current).childs:
            pathCost = current.g + D
            if child in closed and pathCost >= child.g:
                continue
            if not child in closed or pathCost < child.g:
                current.addChild(child.queens)
                if not child in opened:
                    opened.insert(child)
    return None
