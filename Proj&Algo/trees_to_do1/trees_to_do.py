
# Add

class BTNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def add(self, val):
        new_node = BTNode(val)

        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if val <= current.val:
                    if current.left is None:
                        current.left = new_node
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        break
                    else:
                        current = current.right

if __name__ == "__main__":
    bst = BST()
    bst.add(5)
    bst.add(3)
    bst.add(7)
    bst.add(2)
    bst.add(4)

    def in_order_traversal(node):
        if node is not None:
            in_order_traversal(node.left)
            print(node.val)
            in_order_traversal(node.right)

    in_order_traversal(bst.root)


# Contains

class BTNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def contains(self, val):
        current = self.root
        while current is not None:
            if current.val == val:
                return True
            elif val < current.val:
                current = current.left
            else:
                current = current.right
        return False

if __name__ == "__main__":
    bst = BST()

    print(bst.contains(3))
    print(bst.contains(6))

# Min

class BTNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def min(self):
        current = self.root
        while current.left is not None:
            current = current.left
        return current.val

if __name__ == "__main__":
    bst = BST()

    print(bst.min())


# Max

class BTNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def max(self):
        current = self.root
        while current.right is not None:
            current = current.right
        return current.val


if __name__ == "__main__":
    bst = BST()

    print(bst.max())


# Size

class BTNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def size(self):
        return self._size_recursive(self.root)

    def _size_recursive(self, node):
        if node is None:
            return 0
        return 1 + self._size_recursive(node.left) + self._size_recursive(node.right)

if __name__ == "__main__":
    bst = BST()

    print(bst.size())

# Is Empty

class BTNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root is None

if __name__ == "__main__":
    bst = BST()

    print(bst.isEmpty())

    print(bst.isEmpty())

