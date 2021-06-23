# balanced binary tree
'''
เป็นbinary treeประเภทหนึ่ง ที่มีความต่างระหว่างความสูง
ของleft และ right subtree  ของแต่ละโหนด คือ 0 หรือ 1
(ความสูงของsubtreeด้านซ้ายและขวาสำหรับโหนดใดๆไม่เกิน 1)
'''

from PerfectBinaryTree import calculateTheDepth


class Node:
    def __init__(self, item):
        self.item = item
        self.left = self.right = None

class CalculateHeight:
    def __init__(self):
        self.CalculateHeight = 0

def is_height_balanced(root, CalculateHeight):
    left_hieght = CalculateHeight()
    right_height = CalculateHeight()