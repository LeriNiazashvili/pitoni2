class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def _insert(self, node, key):
        if node is None:
            return Node(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)

        return node

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _print_parents(self, node, parent):
        if node:
            if parent is None:
                print(node.key, "-> Root")
            else:
                print(node.key, "-> ", parent.key)

            self._print_parents(node.left, node)
            self._print_parents(node.right, node)

    def print_parents(self):
        print("--- ხის სტრუქტურა და მშობლები ---")
        self._print_parents(self.root, None)

    def _print_leaves(self, node):
        if node is None:
            return

        if node.left is None and node.right is None:
            print(node.key, end=" ")
            return

        self._print_leaves(node.left)
        self._print_leaves(node.right)

    def print_leaves(self):
        print("--- ფოთლები (Leaf Nodes) ---")
        self._print_leaves(self.root)
        print()  



if __name__ == "__main__":
    tree = BST()

    numbers = [50, 30, 70, 20, 40, 60, 80]
    for num in numbers:
        tree.insert(num)

    tree.print_parents()
    print() 

    tree.print_leaves()