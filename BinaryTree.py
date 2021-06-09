#Binary Tree
"""
Tree represents the nodes connected by edges(Left Node & Right Node). It is a non-linear data structure.
-One node is marked as Root node.
-Every node other than the root is associated with one parent node.
-Each node can have an arbiatry number of chid node.
We designate one node as root node and then add more nodes as child nodes.
"""

class Node:
    #create Root
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    #insert node
    def insert(self, data):
        #compare the new value with the parent
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    #print tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()
    
    #In-order traversal
    #left -> root -> right
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)


# use insert method to add nodes
root = Node(10)
root.insert(6)
root.insert(14)
root.insert(3)

root.PrintTree()
