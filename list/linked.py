
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    #linked list constructor 
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head

        while(temp):
            print(temp.data, end="->")
            temp = temp.next
        print()
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
