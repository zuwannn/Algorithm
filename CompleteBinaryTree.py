# complete binary tree
'''
complete binary tree ก็เหมือนกับ full binary tree แตกต่างกัน คือ
1.ทุกlevel ต้องเต็มหมด
2.leaf node ต้องเอนไปทางขวา
3.leaf node สุดท้าย'อาจ'ไม่มีพี่น้องทางขวาก็ได้
(completeBT 'ไม่จำเป็นต้องเป็น' fullBT)
'''

class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

# count the number of node
def count_nodes(root):
    if root is None:
        return 0
    return ( 1 + count_nodes(root.left) + count_nodes(root.right) )

# check if the tree is complete binary tree
def isComplete(root, index, numberNodes):
    # check if the tree is empty
    if root is None:
        return True

    if index >= numberNodes:
        return False

    return (isComplete(root.left, 2*index+1, numberNodes) and
            isComplete(root.right, 2*index+2, numberNodes))


if __name__=="__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.right.left = Node(8)
    
    node_count = count_nodes(root)
    index = 0

    if isComplete(root, index, node_count):
        print("the tree is a complete binary tree")
    else:
        print("the tree is not a complete binary tree")