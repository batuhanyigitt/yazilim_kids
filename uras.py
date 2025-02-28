

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._insert(self.root, key)
            
    def _insert(self, node, key):
        if key < node.key:
            if not node.left:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        elif key > node.key:
            if not node.right:
                node.right = Node(key)
            else:
                self._insert(node.right, key)
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if not node:
            return False
        if node.key == key:
            return True
        return self._search(node.left, key) if key < node.key else self._search(node.right, key)

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)
            
if __name__ == "__main__": 
    bst = BinarySearchTree()
    for key in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(key)
        
print("Search 40:", bst.search(40))
print("Search 90:", bst.search(90))
print("Duzenli", bst.inorder())