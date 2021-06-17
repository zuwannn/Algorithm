# breadth first seach (BFS) algorithm
'''
เป็นsearch algorithm ในการหาข้อมูลทั้งหมดที่โหนดเริ่มต้นของ(Root node)
และทำการสำรวจโหนดของเพื่อนบ้าน การค้นหาแบบกว้างก่อน
เป็นการกําหนดทิศทางการค้นหาแบบทีละระดับของโครงสร้างต้นไม้

โดยในขณะที่กำลังท่องกราฟมายังจุดยอดหนึ่งๆนั้น จะมีการกระทำ2อย่างคือ:
1.เข้าเยี่ยมและตรวจสอบจุดยอดดังกล่าว
2.เข้าถึงจุดยอดข้างเคียงของจุดยอดดังกลาว
'''

import collections

def bfs(graph, root):
    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:

        # dequeue a vertex from queue
        vertex = queue.popleft()
        print(str(vertex), end=" ")

        # if not visited, mark it as visited, and enqueue it
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

if __name__ == "__main__":
    graph = {0: [1,2],
             1: [2],
             2: [3],
             3: [1,2]}
    print("following is Breadth First Traversal: ")
    bfs(graph, 0)
