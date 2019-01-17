import random

class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()
    
    def append(self, data):
        new_node = node(data)
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node
    
    def length(self):
        length = 0
        current_node = self.head
        while current_node.next != None:
            length += 1
            current_node = current_node.next
        return length
    
    def display(self):
        list_content = []
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            list_content.append(current_node.data)
        return list_content
    
    def get(self, index):
        if index >= self.length():
            print("Get index out of range")
            return 
        counter = 0
        current_node = self.head
        while True:
            current_node = current_node.next
            if counter == index: return current_node.data
            else: counter += 1
        return current_node.data

test_list = linked_list()

test_list.append(1)
test_list.append(2)
test_list.append(3)
test_list.append(4)

print(test_list.display())
print(test_list.length())
print(test_list.get(2))