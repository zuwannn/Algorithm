# Binary Search

'''
Recursive Method

binarySearch(arr, x, low, high)
    if low > high
        return False 
    else
        mid = (low + high) / 2 
        if x == arr[mid]
            return mid
        else if x > arr[mid]     // x is on the right side
            return binarySearch(arr, x, mid + 1, high)
        else                     // x is on the right side
            return binarySearch(arr, x, low, mid - 1)
'''

def BS_recursive(array, x, low, high):
    if high >= low:
        mid = low + (high - low)//2

        #if found at mid, then return it
        if array[mid] == x:
            return mid
        
        #search the left half
        elif array[mid] > x:
            return BS_recursive(array, x, low, mid-1)

        #search the right half
        else:
            return BS_recursive(array, x, mid + 1, high)
    else:
        return -1

list = [19,2,31,45,6,11,121,27]
# x is the number to find
x = 2
result = BS_recursive(list, x, 0, len(list)-1)

if result != -1:
    print("element is paresent at index " + str(result))
else:
    print("no found")