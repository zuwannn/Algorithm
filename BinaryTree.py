# binary tree

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

    # root -> left -> right
    def PreOrder(self):
        print(self.value, end=" ")
        if self.left:
            self.left.PreOrder()
        if self.right:
            self.right.PreOrder()

    # left -> root -> right
    def InOrder(self):
        if self.left:
            self.left.InOrder()
        print(self.value, end=" ")
        if self.right:
            self.right.InOrder()

    # left -> right -> root
    def PostOrder(self):
        if self.left:
            self.left.PostOrder()
        if self.right:
            self.right.PostOrder()
        print(self.value, end=" ")


if __name__ == "__main__":

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)

    print("Pre order traversal: ", end="")
    root.PreOrder()

    print("\nIn order traversal: ", end="")
    root.InOrder()

    print("\nPost order traversal: ", end="")
    root.PostOrder()