from MinHeap import *

NUM = 8
B = NUM * (NUM - 1)
D = 1

def expand(node: Node):
    newNode = Node(node.queens)
    for i in range (NUM):
        for j in range (1, NUM):
            newNode.addChild(i, j)
    return newNode
