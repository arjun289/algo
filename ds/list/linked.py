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


    def getCentre(self):
        fast = self.head
        slow = self.head

        while(fast is not None and fast.next is not None):
            fast = fast.next.next
            slow = slow.next

        return slow.data
        
    def reverse(self):
        prev = None
        current = self.head
        nex = None

        while(current is not None):
            nex = current.next
            current.next = prev
            prev = current
            current = nex
        self.head = prev

    def rev(self):
        if self.head is  None:
            return
        self.__reverseUtil(self.head, None)

    def __reverseUtil(self, curr, prev):
        if curr.next is None:
            self.head = curr
            curr.next = prev
            return

        nex = curr.next
        curr.next = prev
        self.__reverseUtil(nex, curr)








