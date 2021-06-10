# insertion sort

'''
sort each element in the suitable position.
'''

def insertion_sort(inputList):
    for i in range(1,len(inputList)):
        j = i-1
        next_element = inputList[i]

        # compare current element with next element
        while(inputList[j] > next_element) and (j>=0):
            inputList[j+1] = inputList[j]
            j=j-1
        inputList[j+1] = next_element


list = [19,2,31,45,6,11,121,27]
insertion_sort(list)
print(list)

