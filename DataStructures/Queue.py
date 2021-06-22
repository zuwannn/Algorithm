# queue algorithm

class Queue:

    def __init__(self):
        self.queue = []

    # Add an element to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # Remove an element from the front of the queue
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # display the queue
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(6)
    q.enqueue(4)
    q.enqueue(5)

    q.display()