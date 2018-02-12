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

    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return 
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = new_node
    
    def delete(self, data):
        """ delete link with data """

        temp = self.head
        if temp.data == data:
            self.head = temp.next
            temp = None
            return

        while temp.next is not None:
            if temp.data == data:
                break
            prev = temp
            temp = temp.next
        
        if(temp == None):
            return
        prev.next = temp.next

        temp = None
    
    def __getCount(self, node):
        if(node is None):
            return 0
        else:
            return 1 + self.__getCount(node.next)

    def getC(self):
        return self.__getCount(self.head)



