# Binary Search Tree

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        if not self.root:
            self.root = node
            return self
        current = self.root
        while True:
            if value < current.value:
                if not current.left:
                    current.left = node
                    return self
                else:
                    current = current.left
            else:
                if not current.right:
                    current.right = node
                    return self
                else:
                    current = current.right

    def search(self, value):
        if not self.root:
            return
        current = self.root
        find = False

        while current and not find:
            if current.value == value:
                find = True
            elif(current.value > value):
                current = current.left
            else:
                current = current.right

        return find

    # Breadth First Search
    def BFS(self):
        data = []
        queue = [self.root]

        while queue:            
            node = queue.pop(0)
            data.append(node.value)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)

        return data
        
    # Depth First Search PreOrder
    def DFSPreOrder(self):
        data = []

        def traverse(node):
            data.append(node.value)
            if node.left: traverse(node.left)
            if node.right: traverse(node.right)
        traverse(self.root)
        return data
    
    # Depth First Search Post Order
    def DFSPostOrder(self):
        data = []

        def traverse(node):
            if node.left: traverse(node.left)
            if node.right: traverse(node.right)
            data.append(node.value)
        traverse(self.root)
        return data

    def DFSInOrder(self):
        data = []

        def traverse(node):
            if node.left: traverse(node.left)
            data.append(node.value)
            if node.right: traverse(node.right)
        traverse(self.root)
            
        return data

bst = BST()
bst.insert(10)
bst.insert(6)
bst.insert(15)
bst.insert(20)
bst.insert(8)
bst.insert(3)
bst.DFSInOrder()
# bst.search(25)
# bst.search(3)
