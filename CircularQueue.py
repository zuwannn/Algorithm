# circular queue

class CircularQueue():

    def __init__(self, k):
        # k is Desired queue size
        self.k = k
        self.queue = [None]*k
        self.head = self.tail = -1 # set default head&tail is -1

    # insert element into circularqueue
    def enqueue(self, data):
        # if tail+1 mod k = head print queue is full
        if ((self.tail+1)%self.k == self.head):
            print("the circular queue is full\n")
        
        elif(self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data

    # delete element from circularqueue
    def dequeue(self):
        if (self.head == -1):
            print("the circular queue is empty\n")

        elif(self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head+1) % self.k
            return temp

    def printCQ(self):
        if(self.head==-1):
            print("no element in circular queue")
        elif(self.tail >= self.head):
            for i in range(self.head, self.tail+1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.head, self.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail+1):
                print(self.queue[i], end=" ")
            print()

if __name__ == "__main__":
    cq = CircularQueue(5)
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    cq.enqueue(4)
    cq.enqueue(5)
    print("initial queue")

    cq.printCQ()

    cq.dequeue()
    print("after remove element from queue")
    cq.printCQ()