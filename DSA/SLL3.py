#Single Linear Linked List
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if (self.head == None):
            self.head = new_node
        else:
            temp = self.head
            while (temp.next):
                temp = temp.next
            temp.next = new_node     #appending new node

    def insert(self, new_node, pos):
        temp = self.head
        if pos == 1:                     #inserting at first position
            new_node.next = self.head
            self.head = new_node
        else:
            p = 1
            while (p!=pos-1):
                temp = temp.next
                p += 1
            new_node.next = temp.next
            temp.next = new_node

    def print(self):
        temp = self.head
        count = 0
        total_sum = 0
        while temp:
            print(temp.data)
            count += 1
            total_sum += temp.data
            temp = temp.next
        print(f"Total number of nodes: {count}")
        print(f"Sum of node values: {total_sum}")

list = LinkedList()
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(Node(55))
list.append(Node(48))
list.print()
list.insert(Node(100),1)
list.print()
list.insert(Node(66), 7)
list.print()