import random

class node():
    def __init__(self, data = None):
        self.data = data
        self.prev = None
        self.next = None

class doubly_linked_list():
    def __init__(self):
        self.head = node()
    
    def append(self, data):
        current_node = self.head
        prev = None
        if self.head.data == None: self.head = node(data)
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = node(data)
        current_node.next.prev = current_node
        print(current_node.next.prev.data)

    def display(self):
        current_node = self.head
        buffer = []
        while current_node != None:
            buffer.append(current_node.data)
            current_node = current_node.next
        return buffer

test_list = doubly_linked_list()
test_list.append(1)
test_list.append(2)
test_list.append(3)


for i in range(0,5):
    test_list.append(random.randint(0,100))

print(test_list.display())