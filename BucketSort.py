# bucket sort
'''
ีbucketSort(list) เมื่อ list เป็นข้อมูลเข้า nตัว ที่แต่ละค่าเป็นจำนวนระหว่างช่วง [0, 1) 
'''

def bucketSort(list):
    bucket = []

    #create empty buckets
    for i in range(len(list)+1):
        bucket.append([])

    #insert elements into their respective buckets
    for j in list:
        index_bucket = int(10*j)
        bucket[index_bucket].append(j)

    #get the sorted elements
    k = 0
    for i in range(len(list)):
        for j in range(len(bucket[i])):
            list[k] = bucket[i][j]
            k = k + 1
    return list


list = [0.11, 0.21, 0.31, 0.25, 0.01, 0.1212]
bucketSort(list)
print(list)

