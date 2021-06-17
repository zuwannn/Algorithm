# dequeue

class Dequeue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addRear(self, item):
        self.items.append(item)

    def addFront(self, item):
        self.items.insert(0, item)


if __name__ == "__main__":
    d = Dequeue()

    print(d.isEmpty())