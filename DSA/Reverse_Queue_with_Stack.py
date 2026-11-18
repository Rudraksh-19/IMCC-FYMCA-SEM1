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
            popped_data = temp.data
            self.top = self.top.next 
            temp = None 
            return popped_data
        
    def print(self):
        if self.isempyt():
            print("Stack is Empty")
        else:
            print("Stack contains :- ")
            temp = self.top 
            while temp:
                print(temp.data)
                temp = temp.next 

class LQueue:
    def __init__(self):
            self.front = self.rear = None

    def isempty(self):
            return self.front is None

    def enqueue(self, new_node):
            if self.rear:
                self.rear.next = new_node 
                self.rear = new_node
            else:
                self.front = self.rear = new_node

    def dequeue(self):
            temp = self.front
            dequed_data = temp.data
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            temp = None
            return dequed_data


    def print(self):
            temp = self.front
            print("Queue contains :- ")
            while temp:
                print(temp.data, end = "->")
                temp = temp.next 
            print("None") 

def reverse_stack(s1):
    q1 = LQueue()
    while not s1.isempyt():
        q1.enqueue(node(s1.pop()))
    #q1.print()
    while not q1.isempty():
        s1.push(node(q1.dequeue()))
    s1.print()


st = stack()
st.push(node(10))
st.push(node(20))
st.push(node(30))
st.push(node(40))
st.push(node(50))
st.print()
reverse_stack(st)









