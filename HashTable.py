# hash table
'''
Hash table/Hash map เป็นโครงสร้างข้อมูลในรูปแบบตาราง 
มักใช้แถวลำดับหรือMapขนาดใหญ่เพื่อใช้ในการจัดการเก็บข้อมูลจำนวนมาก 
โดยมีลักษณะการเก็บแบบดัชนีได้ (Indexing) วิธีการเก็บนั้นจะนำkey
ที่จะนำมาเก็บผ่านฟังก์ชันแฮช จะได้เลขซึ่งจำเพาะกับข้อมูลนั้น 
กล่าวคือ ข้อมูลแต่ละตัวเมื่อผ่านฟังก์ชันแฮชแล้ว จะได้เลขที่แตกต่างกัน 
แล้วจึงนำข้อมูลไปเก็บไว้ในตาราง แถวลำดับ หรือ Map ที่กำหนดไว้ 

ตารางแฮชเน้นการค้นหาและเพิ่มลดสมาชิกอย่างรวดเร็ว จนเป็นเวลาคงที่ O(1) 
แต่ข้อมูลเหล่านั้นจะต้องไม่มีลำดับและไม่ซ้ำกันเท่านั้น 
'''

# Python program to demonstrate working of HashTable 
hashTable = [[],]*10

def checkPrime(n):
    if n == 1 or n == 0:
        return 0
    
    for i in range(2, n//2):
        if n % i == 0:
            return 0
    return 1

def getPrime(n):
    if n % 2 == 0:
        n += 1
    while not checkPrime(n):
        n += 2
    return n

def hashFunction(key):
    capacity = getPrime(10)
    return key % capacity

def insertData(key, data):
    index = hashFunction(key)
    hashTable[index] = [key, data]

def removeData(key):
    index = hashFunction(key)
    hashTable[index] = 0

if __name__ == "__main__":

    insertData(123, "apple")
    insertData(432, "mango")
    insertData(213, "baanana")
    insertData(654, "guava")

    print("hash table:")
    print(hashTable)

    removeData(213)
    print("after removing data by key:")
    print(hashTable)

    
