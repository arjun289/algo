from linked import LinkedList
from linked import Node


if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third
    
    llist.printList()
    
    llist.push(4)
    llist.push(5)
    llist.printList()
    llist.append(10)
    llist.append(20)
    llist.printList()
    llist.delete(20)
    llist.printList()
    print(llist.getC())
    llist.push(30)
    llist.printList()
    print(llist.getCentre())
    llist.reverse()
    llist.printList()
    llist.rev()
    llist.printList()
