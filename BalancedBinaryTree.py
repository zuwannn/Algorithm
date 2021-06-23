# balanced binary tree
'''
เป็นbinary treeประเภทหนึ่ง ที่มีความต่างระหว่างความสูง
ของleft และ right subtree  ของแต่ละโหนด คือ 0 หรือ 1
(ความสูงของsubtreeด้านซ้ายและขวาสำหรับโหนดใดๆไม่เกิน 1)
'''
# create node
class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

# find height of tree
def height(root):
    # if tree is empty
    if root is None:
        return 0
    return max(height(root.left), height(root.right))+1

# tree is balanced or not
def isBalanced(root):

    # Base condition
    if root is None:
        return True

    # for left and right subtree height
    left_height = height(root.left)
    right_height = height(root.right)
    
if __name__=="__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.left.left = Node(5)

    if height(root):
        print("the root is a balanced binary tree")
    else:
        print("the root is not a balanced binary tree")
