class node:
    def __init__(self, value):
        self.data = value 
        self.next = None 

class stack:
    def __init__(self):
        self.top = None 

    def isempyt(self):
        return self.top is None 
    def push(self, new_node):
        new_node.next = self.top 
        self.top = new_node 

    def pop(self):
        if self.isempyt():
            print("Stack is empty")
        else:
            temp = self.top 
            print("Popped Elements : ", temp.data)
            self.top = self.top.next 
            temp = None 
    def print(self):
        if self.isempyt():
            print("Stack is Empty")
        else:
            print("Stack contains :- ")
            temp = self.top 
            while temp:
                print(temp.data)
                temp = temp.next 
    def reverse(self):
        temp = self.top 
        while temp:
            sta1.push(node(temp.data))
            temp = temp.next 
        

sta = stack()
sta1 = stack()
sta.push(node(10))
sta.push(node(20))
sta.push(node(30))
sta.push(node(40))
sta.push(node(50))
sta.print()
sta.pop()
sta.print()


sta.reverse()
print("Reversed Stack is :- ")
sta1.print()