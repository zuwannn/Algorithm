# bubble sort
'''
compare each pair of adjacent elements is compared and 
the elements are swapped if they are not in order.
time is O(n^2)
'''

def bubblesort(list):
    #iterative list
    for iter_num in range(len(list)-1,0,-1):
        #iterative number
        for index in range(iter_num):
            #swap element
            if list[index]>list[index+1]:
                temp = list[index]
                list[index] = list[index+1]
                list[index+1] = temp

list = [19,2,31,45,6,11,121,27]
bubblesort(list)
print(list)