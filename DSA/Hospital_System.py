class node:
    def __init__(self, pid, name, pr):
        self.patient_id = pid
        self.name = name
        self.priority = pr
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, new_node):
        if self.front is None:        #first node to be inserted
            self.front = self.rear = new_node
            return

        if self.front.priority > new_node.priority:  #first position
            new_node.next = self.front
            self.front = new_node
            return
        else:
            temp = self.front
            while temp.next:
                if new_node.priority < temp.next.priority:
                    break
                else:
                    temp = temp.next

            new_node.next = temp.next
            temp.next = new_node

            if new_node.next is None:
                self.rear = new_node

    def display_next(self):
        if self.front is None:
            print("No patients waiting")
            return

        print("Next patient to be treated:")
        print("Patient ID:", self.front.patient_id)
        print("Patient Name:", self.front.name)
        print("Priority:", self.front.priority)

    def dequeue(self):
        if self.front is None:
            print("No patients to remove")
            return

        temp = self.front
        print("Patient treated:", temp.name)

        self.front = self.front.next

        if self.front is None:
            self.rear = None

    def display_all(self):
        if self.front is None:
            print("No patients waiting")
            return

        temp = self.front
        print("All waiting patients:")

        while temp:
            print("Patient ID:", temp.patient_id,
                  "Name:", temp.name,
                  "Priority:", temp.priority)
            temp = temp.next


pq = PriorityQueue()

pq.enqueue(node(101, "Rudraksh", 2))
pq.enqueue(node(102, "Aayush", 3))
pq.enqueue(node(103, "Prasad", 1))
pq.enqueue(node(104, "Krishna", 2))
pq.enqueue(node(105, "Pranav", 3))

pq.display_all()

pq.display_next()

pq.dequeue()

pq.display_all()