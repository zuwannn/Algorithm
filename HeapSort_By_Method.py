# heap sort by method 

from heapq import heappop, heappush

def HeapSort(list):
    heap = []
    for element in list:
        heappush(heap, element)

    ordered = []

    while heap:
        ordered.append(heappop(heap))

    return ordered

list = [19, 2, 31, 45, 6, 11, 121, 27]
print(HeapSort(list))
