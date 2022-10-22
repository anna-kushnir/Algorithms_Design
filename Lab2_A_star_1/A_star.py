from MinHeap import *

def expand(node: Node):
    newNode = Node(node.queens, node.g)
    for i in range (NUM):
        for j in range (1, NUM):
            newNode.addChildByChangingParent(i, j)
    return newNode

def A_star(root: Node):
    U = []
    Q = MinHeap(B)
    Q.insert(root)
    while Q.size != 0:
        current = Q.remove()
        if current.h == 0:
            return current
        U.append(current)
        for v in expand(current).childs:
            tentativeScore = current.g + D
            if v in U and tentativeScore >= v.g:
                continue
            if not v in U or tentativeScore < v.g:
                current.addChild(v.queens)
                if not v in Q:
                    Q.insert(v)
    return None