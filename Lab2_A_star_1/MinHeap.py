import sys
from Node import *

class MinHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap : list[Node] = [None]*(self.maxsize + 1)
        self.Heap[0] = -1 * sys.maxsize
        self.FRONT = 1

    def parent(self, pos):
        return pos//2

    def leftChild(self, pos):
        return 2 * pos

    def rightChild(self, pos):
        return (2 * pos) + 1

    def isLeaf(self, pos):
        return pos*2 > self.size

    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    def minHeapify(self, pos):
        if not self.isLeaf(pos):
            if (self.Heap[pos].f > self.Heap[self.leftChild(pos)].f or 
               self.Heap[pos].f > self.Heap[self.rightChild(pos)].f):
                if self.Heap[self.leftChild(pos)].f < self.Heap[self.rightChild(pos)].f:
                    self.swap(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))
                    
    def insert(self, element: Node):
        if self.size >= self.maxsize :
            self.updateMaxsize(self.maxsize)
        self.size+= 1
        self.Heap[self.size] = element
        current = self.size
        while self.Heap[current].f < self.Heap[self.parent(current)].f:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def minHeap(self):
        for pos in range(self.size//2, 0, -1):
            self.minHeapify(pos)

    def remove(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.minHeapify(self.FRONT)
        return popped

    def updateMaxsize(self, add):
        self.maxsize = self.maxsize + add
        for i in range(add):
            self.Heap.append(None)