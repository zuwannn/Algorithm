#merge sort
'''
Merge sort first divides the array into equal halves 
and then combines them in a sorted manner.
'''

def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list

    #find middle point and devide it(devide with 2)
    middle = len(unsorted_list) // 2 # // is floor number to number
    left_list = unsorted_list[:middle] # first to middle
    right_list = unsorted_list[middle:] # middle to last

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return list(merge(left_list, right_list))

def merge(left_haft, right_haft):
    res = []
    while len(left_haft) != 0 and len(right_haft) != 0:
        if left_haft[0] < right_haft[0]:
            res.append(left_haft[0])
            left_haft.remove(left_haft[0])
        else:
            res.append(right_haft[0])
            right_haft.remove(right_haft[0])
    
    if len(left_haft) == 0:
        res = res + right_haft
    else:
        res = res + left_haft
    return res

    
unsorted_list = [19,2,31,45,6,11,121,27]
print(merge_sort(unsorted_list))