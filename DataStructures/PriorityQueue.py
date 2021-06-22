# priority queue
'''
Priority queue จะมีการเรียงข้อมูลตาม Priority จากมากไปน้อยตลอดเวลา 
การสร้าง Priority queue นั้นจำเป็นที่จะต้องมีเกณฑ์ที่บอกว่าข้อมูลตัวใดมี 
Priority มากกว่าข้อมูลอีกตัวหนึ่ง เช่น 
หากต้องการจะให้ Priority queue ดำเนินการกับข้อมูลที่มีค่ามากก่อนค่าน้อย 
เมื่อใส่จำนวน 9 5 4 3 2 ลงใน Priority queue นี้ตามลำดับ 
จะได้ว่าข้อมูลที่ออกมาคือ 1 3 4 6 8
'''

def heapify(arr, n, i):
    # find largest among root, left child and right child
    largest = i
    left = 2*i+1
    right = 2*i+2

    if left < n and arr[i] < arr[left]:
        largest = left
    
    if right < n and arr[largest] < arr[right]:
        largest = right

    # swap and continue heapifying if root is not largest
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# function insert element into tree
def insert(array, newNum):
    size = len(array)
    if size == 0:
        array.append(newNum)
    else:
        array.append(newNum)
        for i in range((size//2) -1, -1, -1):
            heapify(array, size, i)


# function delete element from tree
def delete(array, num):
    size = len(array)
    i = 0
    for i in range(0, size):
        if num == array[i]:
            break

    array[i], array[size-1] = array[size-1], array[i]
        
    array.remove(size-1)

    for i in range((len(array)//2)-1, -1, -1):
        heapify(array, len(array), i)

        

if __name__ == "__main__":
    arr = []
    insert(arr, 3)
    insert(arr, 4)
    insert(arr, 9)
    insert(arr, 5)
    insert(arr, 2)
    print("max-heap array : " + str(arr))

    delete(arr, 4)
    print("after delete element : " + str(arr))
