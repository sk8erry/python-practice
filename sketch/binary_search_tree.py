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
        elif value > current_node.value:
            if current_node.right == None:
                current_node.right = node(value)
                return
            self._insert(value, current_node.right)
        else: 
            print("Value already in tree")
            return
    
    def display(self):
        if self.root != None:
            self._display(self.root)
        else: print("Tree empty")
        
    def _display(self, current_node):
        if current_node != None:
            self._display(current_node.left)
            print(current_node.value)
            self._display(current_node.right)
        return

    def height(self):
        if self.root != None:
            return self._height(self.root, 0)
        else: return 0
    
    def _height(self, current_node, current_height):
        if current_node == None: return current_height
        else: 
            left_height = self._height(current_node.left, current_height + 1)
            right_height = self._height(current_node.right, current_height + 1)
        return max(left_height, right_height)
    
    def search(self, value):
        if self.root != None:
            return self._search(self.root, value)
        else: print("Tree empty")
    
    def _search(self, current_node, value):
        print(current_node.value, value)
        if current_node.value == value: return True
        elif value < current_node.value and current_node.left != None:
            return self._search(current_node.left, value)
        elif value > current_node.value and current_node.right != None:
            return self._search(current_node.right, value)
        return False


test_tree = binary_search_tree()

test_tree.insert(3)
test_tree.insert(4)
test_tree.insert(5)
test_tree.insert(2)
test_tree.display()

print(test_tree.search(2))