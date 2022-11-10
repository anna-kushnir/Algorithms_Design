class Node:
    def __init__(self, key: int, value: str, parent = None, left = None, right = None, height: int = 0):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        self.height = height


class AVLTree:
    def __init__(self):
        self.root = None

    def find(self, key: int):
        if not self.root:
            return None
        return self._find(key, self.root)

    def _find(self, key: int, node: Node):
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


    def _right_rotate(self, node: Node):
        temp = node.left
        node.left = temp.right
        temp.right = node

        temp.parent = node.parent
        node.parent = temp
        if node.left:
            node.left.parent = node

        node.height = max(self.height(node.right), self.height(node.left)) + 1
        temp.height = max(self.height(temp.left), node.height) + 1
        return temp

    def _left_rotate(self, node: Node):
        temp = node.right
        node.right = temp.left
        temp.left = node

        temp.parent = node.parent
        node.parent = temp
        if node.right:
            node.right.parent = node

        node.height = max(self.height(node.right), self.height(node.left)) + 1
        temp.height = max(self.height(temp.right), node.height) + 1
        return temp

    def _right_left_rotate(self, node: Node):
        node.right = self._right_rotate(node.right)
        return self._left_rotate(node)

    def _left_right_rotate(self, node: Node):
        node.left = self._left_rotate(node.left)
        return self._right_rotate(node)

    def insert(self, key: int, value):
        if not self.root:
            self.root = Node(key, value)
            flag = True
        else:
            self.root, flag = self._insert(key, value, self.root, None)
        return flag

    def _insert(self, key: int, value, node: Node, parent: Node):
        if not node:
            node = Node(key, value, parent)
            flag = True
        elif key < node.key:
            node.left, flag = self._insert(key, value, node.left, node)
            if (self.height(node.left) - self.height(node.right)) == 2:
                if key < node.left.key:
                    node = self._right_rotate(node)
                else:
                    node = self._left_right_rotate(node)
        elif key > node.key:
            node.right, flag = self._insert(key, value, node.right, node)
            if (self.height(node.left) - self.height(node.right)) == -2:
                if key > node.right.key:
                    node = self._left_rotate(node)
                else:
                    node = self._right_left_rotate(node)
        else:
            flag = False
        node.height = max(self.height(node.right), self.height(node.left)) + 1
        return node, flag

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


    def delete(self, key: int):
        if not self.root:
            return
        if self.find(key):
            self.root = self._delete(key, self.root)

    def _delete(self, key: int, node: Node):
        if not node:
            return None
        if key < node.key:
            node.left = self._delete(key, node.left)
        elif key > node.key:
            node.right = self._delete(key, node.right)
        else:
            if not node.left and not node.right:
                return None
            if not node.left or not node.right:
                if node.left:
                    node.left.parent = node.parent
                    return node.left
                if node.right:
                    node.right.parent = node.parent
                    return node.right
            else:
                successor = self._find_min(node.right)
                node.key, successor.key = successor.key, node.key
                node.value, successor.value = successor.value, node.value
                node.right = self._delete(successor.key, node.right)
                return node
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        return self._rebalance_node(node)

    def _rebalance_node(self, node: Node):
        if (self.height(node.left) - self.height(node.right)) == 2:
            if self.height(node.left.left) > self.height(node.left.right):
                return self._right_rotate(node)
            else:
                return self._left_right_rotate(node)
        elif (self.height(node.left) - self.height(node.right)) == -2:
            if self.height(node.right.right) > self.height(node.right.left):
                return self._left_rotate(node)
            else:
                return self._right_left_rotate(node)
        return node

    def change(self, key: int, new_value):
        self.root, flag = self._change(key, new_value, self.root)
        return flag

    def _change(self, key: int, new_value, node: Node):
        if not node:
            flag = False
        elif key < node.key:
            node.left, flag = self._change(key, new_value, node.left)
        elif key > node.key:
            node.right, flag = self._change(key, new_value, node.right)
        else:
            node.value = new_value
            flag = True
        return node, flag

    def preOrderTraverse(self, node: Node):
        if node is not None:
            print(node.key)
            self.preOrderTraverse(node.left)
            self.preOrderTraverse(node.right)
