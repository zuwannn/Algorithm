# full binary tree
'''
A full Binary tree is a special type of binary tree 
in which every parent node/internal node has either two 
or no children.
'''

class Node:
    def __init__(self, item):
        self.item = item
        self.leftChild = None
        self.rightChild = None
# checking full bnary tree
def isFullBinaryTree(root):

    # tree empty case
    if root is None:
        return True

    # checking whether child is present
    if root.leftChild is None and root.rightChild is None:
        return True

    if root.leftChild is not None and root.rightChild is not None:
        return (isFullBinaryTree(root.leftChild) and isFullBinaryTree(root.rightChild))

    return False
if __name__ == "__main__":
    
    root = Node(1)

    root.leftChild = Node(2)
    root.rightChild = Node(3)

    root.leftChild.leftChild = Node(4)
    root.leftChild.rightChild = Node(5)

    root.leftChild.rightChild.leftChild = Node(6)
    root.leftChild.rightChild.rightChild = Node(7)
    

    if isFullBinaryTree(root):
        print("the tree is a full binary tree")
    else:
        print("the tree is not a full binary tree")