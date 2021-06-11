# shell sort

def shell_sort(inputList):
    gap = len(inputList)//2 

    while gap > 0:
        for i in range(gap, len(inputList)):
            temp = inputList[i]
            j = i

            #sort the sublist for this gap