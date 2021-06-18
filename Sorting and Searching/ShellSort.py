# shell sort

def shell_sort(inputList):
    gap = len(inputList)//2 

    while gap > 0:
        for i in range(gap, len(inputList)):
            temp = inputList[i]
            j = i

            #sort the sublist for this gap
            while j>= gap and inputList[j-gap] >temp:
                inputList[j] = inputList[j-gap]
                j = j-gap
            inputList[j] = temp
        
        #reduce the gap for the next element
        gap = gap//2

list = [19,2,31,45,6,11,121,27]
shell_sort(list)
print(list)