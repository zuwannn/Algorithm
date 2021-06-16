# doubly linked list

import gc

# create Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # insert node at the front
    def insert_front(self, data):
        # allocate memory for newNode and assign data to newNode
        newNode = Node(data)

        # make mewNode as a head
        newNode.next = self.head

        # assign null to prev (prev is already none in the constructore)

        # previous of head (now head is the second node) is newNode
        if self.head is not None:
            self.head.prev = newNode

        # head points to newNode
        self.head = newNode
    
    # insert a node after a specific node
    def insert_after(self, prev_node, data):

        # check if previous node is null
        if prev_node is None:
            print("Previous node cannot be null")
            return

        # allcate memory for newNode and assign data to newNode
        newNode = Node(data)

        # set next of newNode to next of prev node
        newNode.next = prev_node.next

        # set next of prev node to newNode
        prev_node.next = newNode

        #set prev of newNode to the previous node
        newNode.prev = prev_node

        # set prev of newNode's next to newNode
        if newNode.next:
            newNode.next.prev = newNode

    def insert_end(self, data):
        
        # allcate memory for newNode and assign data to newNode
        newNode = Node(data)

        # assign null to next of newNode (already done in constructor)

        # if the linked list is empty, make the newNode as head node
        if self.head is None:
            self.head = newNode
            return

        # store the head node temporarily (for later use)
        temp = self.head

        # now, the last node of the linked list is temp

        # assign next of the last node (temp) to newNode
        temp.next = newNode

        # assign prev of newNode to temp
        newNode.prev = temp

        return

    # delete a node from the doubly linked list
    def deleteNode(self, dele):

        # if head or del is null
