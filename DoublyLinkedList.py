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

        # if the linked list is not empty, traverse to the end of the linked list
        while temp.next:
            temp = temp.next

        # now, the last node of the linked list is temp

        # assign next of the last node (temp) to newNode
        temp.next = newNode

        # assign prev of newNode to temp
        newNode.prev = temp

        return

    # delete a node from the doubly linked list
    def deleteNode(self, dele):

        # if head or del is null, deletion is not possible
        if self.head is None or dele is None:
            return
        
        # if del_node is the head node, point the head pointer to the next of del_node
        if self.head == dele:
            self.head = dele.next

        # if del_node is not at the last node, point the prev of node next to del_node to the previous of del_node
        if dele.next is not None:
            dele.next.prev = dele.prev

        # if del_node is not the first node, point the next of the previous node to the next node of del_node
        if dele.prev is not None:
            dele.prev.next = dele.next

        # free the memory of del_node
        gc.collect()

    def display_list(self, node):
        while node:
            print(node.data, end="->")
            last = node
            node = node.next

if __name__ == "__main__":

    # initalize an empty node
    dll = DoublyLinkedList()
    
    dll.insert_end(5)
    dll.insert_front(1)
    dll.insert_front(6)
    dll.insert_end(9)

    # insert 11 after head
    dll.insert_after(dll.head, 11)

    # insert 15 after the second node
    dll.insert_after(dll.head.next, 15)
    dll.display_list(dll.head)

    # delete the last node
    dll.deleteNode(dll.head.next.next.next.next)

    print()
    dll.display_list(dll.head)
