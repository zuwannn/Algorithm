# binary tree

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

    # root -> left -> right
    def PreOrder(self):
        print(self.value, end=" ")

    def InOrder(self):

    def PostOrder(self):

        
if __name__ == "__mai__":

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)

    print("Pre order traversal: ", end="")
    

    print("\In order traversal: ", end="")


    print("\nPost order traversal: ", end="")