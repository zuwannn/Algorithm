# perfect binary tree
'''
A perfect binary tree เป็น binary tree ชนิดหนึ่ง
โดยที่ทุกโหนดภายใน (internal node) ต้องมีโหนดย่อยสองโหนด
และ(leaf nodes) ทั้งหมดอยู่ในระดับเดียวกัน
'''
class Node:
    def __init__(self, k):
        self.k = k
        self.right = self.left = None

# Calculate the depth
def calculateTheDepth(node):
    depth = 0
    while (node is not None):
        depth += 1
        node = node.left
    return depth

# check if the tree is perfect binary tree
def isPerfect(root, depth, level=0):
    # check if the tree is empty
    if(root is None):
        return True

    # check the presence of trees
    if(root.left is None and root.right is None):
        return (depth == level+1)

    if(root.left is None or root.right is None):
        return False

    return (isPerfect(root.left, depth, level+1) and
            isPerfect(root.right, depth, level+1))


if __name__=="__main__":
    root = None
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    if (isPerfect(root, calculateTheDepth(root))):
        print("the tree is a perfect binary tree")
    else:
        print("the tree is not a perfect binary tree")