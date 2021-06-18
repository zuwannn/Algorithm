# tree traversal - in-order, pre-order and post-order

class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.value = item

# left -> root -> right
def inorder(root):
    if root:
        # traverse left
        inorder(root.left)
        # traverse root
        print(str(root.value), end=" ")
        # traverse right
        inorder(root.right)

# root -> left -> right
def preorder(root):
    if root:
        print(str(root.value), end=" ")
        preorder(root.left)
        preorder(root.right)


# left -> right -> root
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.value), end=" ")


if __name__ == "__main__":

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("inorder traversal")
    inorder(root)

    print("\npreorder traversal")
    preorder(root)

    print("\npostorder traversal")
    postorder(root)