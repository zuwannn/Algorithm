# complete binary tree
'''
complete binary tree ก็เหมือนกับ full binary tree แตกต่างกัน คือ
1.ทุกlevel ต้องเต็มหมด
2.leaf node ต้องเอนไปทางขวา
3.leaf node สุดท้ายอาจไม่มีพี่น้องทางขวา
(completeBTไม่จำเป็นต้องเป็น fullBT)
'''

class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None


# count the number of node
def count_node(root):
    if root is None:
        return 0
    return

if __name__=="__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)