class Node:
    def __init__(self, key: int, value: str, left = None, right = None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.height = 0


class AVLTree:
    def __init__(self):
        self.root = None

    def find(self, key):
        if not self.root:
            return None
        return self._find(key, self.root)

    def _find(self, key, node: Node):
        if not node:
            return None
        elif key < node.key:
            return self._find(key, node.left)
        elif key > node.key:
            return self._find(key, node.right)
        return node

    def height(self, node: Node):
        if node is None:
            return -1
        return node.height


    def right_rotate(self, node: Node):
        temp = node.left
        node.left = temp.right
        temp.right = node
        node.height = max(self.height(node.right), self.height(node.left)) + 1
        temp.height = max(self.height(temp.left), node.height) + 1
        return temp

    def left_rotate(self, node: Node):
        temp = node.right
        node.right = temp.left
        temp.left = node
        node.height = max(self.height(node.right), self.height(node.left)) + 1
        temp.height = max(self.height(temp.right), node.height) + 1
        return temp

    def right_left_rotate(self, node: Node):
        node.right = self.right_rotate(node.right)
        return self.left_rotate(node)

    def left_right_rotate(self, node: Node):
        node.left = self.left_rotate(node.left)
        return self.right_rotate(node)

    def insert(self, key, value):
        if not self.root:
            self.root = Node(key, value)
        else:
            self.root = self._insert(key, value, self.root)

    def _insert(self, key, value, node: Node):
        if node is None:
            node = Node(key, value)
        elif key < node.key:
            node.left = self._insert(key, value, node.left)
            if (self.height(node.left) - self.height(node.right)) == 2:
                if key < node.left.key:
                    node = self.right_rotate(node)
                else:
                    node = self.left_right_rotate(node)
        elif key > node.key:
            node.right = self._insert(key, value, node.right)
            if (self.height(node.left) - self.height(node.right)) == -2:
                if key > node.right.key:
                    node = self.left_rotate(node)
                else:
                    node = self.right_left_rotate(node)
        node.height = max(self.height(node.right), self.height(node.left)) + 1
        return node

    def delete(self, key):
        if not self.root:
            return
        self.root = self._delete(self.find(key))

    def _delete(self, node: Node):
        if node is None or self.find(node.key) is None:
            return None
        """
        MUST BE DONE!
        """
            
            

    def preOrderTraverse(self, node: Node):
        if node is not None:
            print(node.key)
            self.preOrderTraverse(node.left)
            self.preOrderTraverse(node.right)
