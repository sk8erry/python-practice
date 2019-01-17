class node():
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linked_list():
    def __init__(self):
        self.head = node()
    
    def append(self, data):
        new_node = node(data)
        current_node = self.head
        if self.head.data == None: self.head = new_node
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node
    
    def display(self):
        current_node = self.head
        buffer = []
        while current_node != None:
            buffer.append(current_node.data)
            current_node = current_node.next
        return buffer
    
    def reverse(self):
        prev = None
        while self.head.next:
            temp = self.head
            self.head = self.head.next
            temp.next = prev
            prev = temp
        self.head.next = prev

test_list = linked_list()

test_list.append(1)
test_list.append(2)
test_list.append(3)
test_list.append(4)
test_list.append(5)

print(test_list.display())
test_list.reverse()
print(test_list.display())
