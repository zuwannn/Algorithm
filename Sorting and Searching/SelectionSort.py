# selection sort

def selection_sort(inputList):
    for index in range(len(inputList)):
        min_index = index
        for j in range(index+1, len(inputList)):
            if inputList[min_index] > inputList[j]:
                min_index = j

        # swap minimun value with compare value
        inputList[index], inputList[min_index] = inputList[min_index], inputList[index]

list = [19,2,31,45,30,11,121,27]
selection_sort(list)
print(list)