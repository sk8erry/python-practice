class node(): 
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

class binary_search_tree():
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root == None: 
            self.root = node(value)
        else:
            self._insert(value, self.root)
    
    def _insert(self, value, current_node):
        if value < current_node.value:
            if current_node.left == None:
                current_node.left = node(value)
                return
            self._insert(value, current_node.left)
        else:
            if current_node.right == None:
                current_node.right = node(value)
                return
            self._insert(value, current_node.right)
    
    def display(self):
        self._display(self.root)
    
    def _display(self, current_node):
        print(current_node.value)
        if current_node.left != None:
            self._display(current_node.left)
        if current_node.right != None:
            self._display(current_node.right)
        return

test_tree = binary_search_tree()
test_tree.insert(3)
test_tree.insert(4)
test_tree.insert(5)
test_tree.insert(2)
test_tree.display()