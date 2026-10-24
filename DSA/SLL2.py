# Single Linear Linked List
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def print_alternate(self):
        temp = self.head
        should_print = True
        
        while temp:
            if should_print:
                print(temp.data)
            should_print = not should_print 
            temp = temp.next

list = LinkedList()
list.append(Node(10))
list.append(Node(20))
list.append(Node(30))
list.append(Node(40))
list.append(Node(50))

list.print_alternate()