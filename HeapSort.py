# Heap Sort

'''
Heapsort is a comparison based sorting technique based on a Binary Heap data structure. 
It is similar to selection sort where we first find the maximum element and 
place the maximum element at the end. 
We repeat the same process for the remaining element.
runtime is o(n log n) 
'''

def heapify(list, n, i):
    # find largest among root and children
    largest = i  # as root on tree
    left  = 2 * i + 1
    right = 2 * i + 2

    # See if left child of root exists 
    # and is greater than root
    if left < n  and list[i] < list[left]:
        largest = left

    # See if right child of root exists 
    # and is greater than root
    if right < n  and list[largest] < list[right]:
        largest = right

    # if root is not largest, swap with largest and continue heapifying
    if largest != i:
        list[i], list[largest] = list[largest], list[i]
        heapify(list, n, largest)



def heapSort(list):
    n = len(list)

    #build max heap
    for i in range(n//2, -1, -1):
        heapify(list, n, i)

    for i in range(n-1, 0, -1):
        #swap
        list[i], list[0] = list[0], list[i]

        #heapify root element
        heapify(list, i, 0)



list = [19,2,31,45,6,11,121,27]
heapSort(list)
print(list)