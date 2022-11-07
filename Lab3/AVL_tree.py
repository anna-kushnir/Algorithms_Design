class Node:
    def __init__(self, key: int, value: str, parent = None, left = None, right = None):
        self.key = key
        self.value = value
        self.parent = parent
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
        if not node:
            return -1
        return node.height


    def right_rotate(self, node: Node):
        temp = node.left
        node.left = temp.right
        temp.right = node

        temp.parent = node.parent
        node.parent = temp
        node.left.parent = node

        node.height = max(self.height(node.right), self.height(node.left)) + 1
        temp.height = max(self.height(temp.left), node.height) + 1
        return temp

    def left_rotate(self, node: Node):
        temp = node.right
        node.right = temp.left
        temp.left = node

        temp.parent = node.parent
        node.parent = temp
        node.right.parent = node

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
            self.root = self._insert(key, value, self.root, None)

    def _insert(self, key, value, node: Node, parent: Node):
        if not node:
            node = Node(key, value, parent)
        elif key < node.key:
            node.left = self._insert(key, value, node.left, node)
            if (self.height(node.left) - self.height(node.right)) == 2:
                if key < node.left.key:
                    node = self.right_rotate(node)
                else:
                    node = self.left_right_rotate(node)
        elif key > node.key:
            node.right = self._insert(key, value, node.right, node)
            if (self.height(node.left) - self.height(node.right)) == -2:
                if key > node.right.key:
                    node = self.left_rotate(node)
                else:
                    node = self.right_left_rotate(node)
        node.height = max(self.height(node.right), self.height(node.left)) + 1
        return node

    def find_min(self):
        if not self.root:
            return None
        return self._find_min(self.root)

    def _find_min(self, node: Node):
        if node.left:
            return self._find_min(node.left)
        return node

    def find_max(self):
        if not self.root:
            return None
        return self._find_max(self.root)

    def _find_max(self, node: Node):
        if node.right:
            return self._find_max(node.right)
        return node

    def delete(self, key):
        if not self.root:
            return
        self.root = self._delete(self.find(key))

    def _delete(self, node: Node):
        if not node or not self.find(node.key):
            return None
        
        if not node.left and not node.right:
            if node.parent:
                if node.parent.left == node:
                    node.parent.left = None
                else:
                    node.parent.right = None
            else:
                self.root = None

        elif not node.left or not node.right:
            if node.left:
                child = node.left
            else:
                child = node.right

            if node.parent:
                if node.parent.left == node:
                    node.parent.left = child
                else:
                    node.parent.right = child
            else:
                self.root = child
            child.parent = node.parent

        else:
            successor = self.find_min(node.right)
            node.key = successor.key
            node.value = successor.value
            self._delete(successor)
            return

        if node.parent:
            node.parent.height = max(self.height(node.parent.left), self.height(node.parent.right)) + 1
            self._rebalance_from_parent_to_root(node.parent)

    def _rebalance_from_parent_to_root(self, node: Node):
        if not node:
            return
        if (self.height(node.left) - self.height(node.right)) == 2:
            if self.height(node.left.left) > self.height(node.left.right):
                node = self.right_rotate(node)
            else:
                node = self.left_right_rotate(node)
        elif (self.height(node.left) - self.height(node.right)) == -2:
            if self.height(node.right.right) > self.height(node.right.left):
                node = self.left_rotate(node)
            else:
                node = self.right_left_rotate(node)
        self._rebalance_from_parent_to_root(node.parent)

    def preOrderTraverse(self, node: Node):
        if node is not None:
            print(node.key)
            self.preOrderTraverse(node.left)
            self.preOrderTraverse(node.right)
