# LinkedList and DoublyLinkedList

'''
|- [head|head.data|head.next] -> [head.next|head.next.data|head.next.next] -> NONE
'''

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = head

'''
NONE <- prev [head] -> [next] -> [tail] -> NONE
HEAD = None, TAIL = HEAD
[HEAD/TAIL] - None
[HEAD]
'''

myList = LinkedList()
myList.head = Node("List Head")

nextVal = Node("Another Node")
finalVal = Node("Last Node")

myList.head.next = nextVal
nextVal.next = finalVal