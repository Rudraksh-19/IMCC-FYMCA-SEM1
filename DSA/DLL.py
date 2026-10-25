class node:
    def __init__(self,value):
        self.prev = None
        self.data = value
        self.next = None
class linked_list :
    def __init__(self):
        self.head = None


    def append(self, new_node):
        temp =self.head
        if temp:
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        else: #First Node
            self.head = new_node


    def insert(self,new_node,pos):
        temp = self.head
        if pos <= 1 or self.head is None:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
        else:
            p =  1 
            while p != pos - 1 and temp.next:
                temp = temp.next
                p+=1
            new_node.next = temp.next
           
            if temp.next:    # Last Node
                temp.next.prev = new_node
            temp.next = new_node
            new_node.prev =temp


    def reverse(self):
        temp = self.head
        if temp == None:
            print("List is empty")
            return 
        while temp.next:
            temp = temp.next 
        print("\nList elements in reverse order: ")
        while temp:
            print(temp.data, end = " ")
            temp = temp.prev
        print()
            

    def delete(self,value):
        temp = self.head
        while temp and temp.data != value:
            temp = temp.next

        if temp is None:
            print("Value is not present in the list")
            return

        if temp.prev is None:  # deleting first node
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        else:
            temp.prev.next = temp.next
            if temp.next:
                temp.next.prev = temp.prev

    # write a function to count occurance of a no in dll
    def count_occurrences(self, value):
        count = 0
        temp = self.head
        while temp:
            if temp.data == value:
                count += 1
            temp = temp.next
        return count

    def swap(self):
        temp = node1 = self.head    #node1 is first node and n
        while temp.next:
            temp = temp.next
    
        temp.next = node1.next
        node1.next = None
        node1.prev = temp.prev
        temp.prev.next = node1
        temp.prev = None
        self.head = temp





    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()
    
list = linked_list()
list.append(node(12))
list.append(node(16))
list.append(node(20))
list.append(node(25))
list.append(node(30))
list.print()
list.insert(node(5),1)
list.insert(node(53),2)
list.print()
list.reverse()

list.delete(53)
list.print()
list.count_occurrences(30)
print("Number of occurrences of 30:", list.count_occurrences(30))
list.insert
list.swap()
list.print()



