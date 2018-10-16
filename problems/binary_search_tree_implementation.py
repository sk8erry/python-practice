class node:
    def __init__(self, value = None):
        self.value = value
        self.leftChild = None
        self.rightChild = None

class binarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, curNode):
        if value < curNode.value:
            if curNode.leftChild == None:
                curNode.leftChild = node(value)
            else:
                self._insert(value, curNode.leftChild)
        elif value > curNode.value:
            if curNode.rightChild == None:
                curNode.rightChild = node(value)
            else:
                self._insert(value, curNode.rightChild)
        else: 
            print("Value already in tree!")

    def printTree(self):
        if self.root != None:
            self._printTree(self.root)
        else:
            print("The tree is empty")

    def _printTree(self, curNode):
        if curNode != None:
            self._printTree(curNode.leftChild)
            print(curNode.value)
            self._printTree(curNode.rightChild)
    
    def height(self):
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0
    
    def _height(self, curNode, curHeight):
        if curNode == None: return curHeight
        leftHeight = self._height(curNode.leftChild, curHeight + 1)
        rightHeight = self._height(curNode.rightChild, curHeight + 1)
        return max(leftHeight, rightHeight)

    def isInTree(self, value):
        if self.root != None:
            return self._isInTree(value, self.root)
        else:
            return False

    def _isInTree(self, value, curNode):
        if value == curNode.value:
            return True
        elif value < curNode.value and curNode.leftChild != None:
            return self._isInTree(value, curNode.leftChild)
        elif value > curNode.value and curNode.rightChild != None:
            return self._isInTree(value, curNode.rightChild)
        return False

    def nodeHeight(self, value):
        if self.root != None:
            return self._nodeHeight(value, self.root, 0)
        else:
            return False

    def _nodeHeight(self, value, curNode, curHeight):
        if value == curNode.value:
            return curHeight
        elif value < curNode.value and curNode.leftChild != None:
            return self._nodeHeight(value, curNode.leftChild, curHeight + 1)
        elif value > curNode.value and curNode.rightChild != None:
            return self._nodeHeight(value, curNode.rightChild, curHeight + 1)
        return False

    def searchBST(self, value):
        if self.root != None:
            return self._searchBST(self.root, value)
        else: return None
    
    def _searchBST(self, curNode, value):
        if curNode.value == value:
            return curNode.value, curNode.leftChild.value, curNode.rightChild.value
        elif value < curNode.value and curNode.leftChild != None:
            return self._searchBST(curNode.leftChild, value)
        elif value > curNode.value and curNode.rightChild != None:
            return self._searchBST(curNode.rightChild, value)
        return False
    
treeContent = [4, 2, 7, 1, 3]
def fillTree(treeContent):
    
    for element in treeContent:
        tree.insert(element)

tree = binarySearchTree()
fillTree(treeContent)

tree.printTree()
print(tree.searchBST(2))
        
    