
def findmax():
    arr = [12,1,2,3,4,5,6,7,8,9,10,20]
    max = arr[0]
    for i in range(len(arr)):
        if max < arr[i]:
            max = arr[i]
    print(max)

findmax()



"""
you can use max module for find max number in array
arr = [1, 2, 3]
M = max(arr)
print(M)
"""
