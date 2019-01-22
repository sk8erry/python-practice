import sys

class node(): 
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

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
                current_node.left.parent = current_node
                return
            self._insert(value, current_node.left)
        elif value > current_node.value:
            if current_node.right == None:
                current_node.right = node(value)
                current_node.right.parent = current_node
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
            #Inorder traversal
            self._display(current_node.left)
            print(current_node.value)
            self._display(current_node.right)
        return
    
    def level_print(self): #Breadth first traversal
        this_level = [self.root]
        while this_level:
            next_level = list()
            for node in this_level:
                sys.stdout.write(str(node.value)+' ')
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
            sys.stdout.write('\n')
            this_level = next_level

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
        if current_node.value == value: return True
        elif value < current_node.value and current_node.left != None:
            return self._search(current_node.left, value)
        elif value > current_node.value and current_node.right != None:
            return self._search(current_node.right, value)
        return False
    
    def find(self, value):
        if self.root.value == value: return self.root
        else: return self._find(self.root, value)
    
    def _find(self, current_node, value):
        if current_node.value == value: return current_node
        elif current_node.value > value and current_node.left != None:
            return self._find(current_node.left, value)
        elif current_node.value < value and current_node.right != None:
            return self._find(current_node.right, value)
        else: return False
    
    def delete(self, value):
        return self._delete(self.find(value))
    
    def _delete(self, node):
        node_num_children = self.num_children(node)
        #Case 1 (node has no child)
        if node_num_children == 0:
            if node.parent.left == node: node.parent.left = None
            else: node.parent.right = None
                
        #Case 2 (node has 1 child)
        if node_num_children == 1:
            if node.parent.left == node: node.parent.left = node.left or node.right
            else: node.parent.right = node.left or node.right
            '''
            if node.left != None: child = node.left
            else: child = node.right
            if node.parent.left == node: node.parent.left = child
            else: node.parent.right = child
            child.parent = node.parent
            '''
        
        #Case 3 (node has 2 children)
        if node_num_children == 2:
            successor = self.min_value_node(node.right) #Get the inorder successor of the deleted node
            node.value = successor.value
            self._delete(successor)

    def min_value_node(self, node): #Return the min value under a certain node
        current_node = node
        while current_node.left != None:
            current_node = current_node.left
        return current_node
    
    def num_children(self, node): #Determine the number of children of a node, return 0, 1 or 2
        num_children = 0
        if node.left != None: num_children += 1
        if node.right != None: num_children += 1
        return num_children

test_tree = binary_search_tree()

test_tree.insert(5)
test_tree.insert(4)
test_tree.insert(6)
test_tree.insert(10)
test_tree.insert(9)
test_tree.insert(11)
test_tree.insert(3)
test_tree.insert(7)

#test_tree.display()
test_tree.level_print()
