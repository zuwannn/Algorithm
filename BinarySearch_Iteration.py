# Binary Search
'''
Iteration Method

do until the pointers low and high meet each other.
    mid = (low + high)/2
    if (x == arr[mid])
        return mid
    else if (x > arr[mid])     // x is on the right side
        low = mid + 1
    else                       // x is on the left side
        high = mid - 1
'''
def BS_iteration(array, x, low, high):
    while low <= high:
        mid = low + ( high - low ) // 2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

list = [19,2,31,45,6,11,121,27]
# x is the number to find
x = 4
result = BS_iteration(list, x, 0, len(list)-1)

if result != -1:
    print("element is paresent at index " + str(result))
else:
    print("no found")

