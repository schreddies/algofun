def insert(root, key):
    if root == None:
        return treeNode(key)
    else:
        if key == root.val:
            return root
        elif root.val > key:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root
    
class treeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
        
def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)
        
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)

def swap(root):
    temp = root.right
    root.right = root.left
    root.left = temp
        
def pivotTree(root):
    if root == None:
        return 0
    else:
        swap(root)
        pivotTree(root.left)
        pivotTree(root.right)
        
def searchTree(root, key):
    if root == None:
        return 0
    else:
        if root.val == key:
            print("found it!")
        elif root.val > key:
            root.left = searchTree(root.left, key)
        else:
            root.right = searchTree(root.right, key)
        return root.val
        
        
obj = treeNode(5)
obj = insert(obj, 3)
obj = insert(obj, 2)
obj = insert(obj, 4)
obj = insert(obj, 7)
obj = insert(obj, 6)
obj = insert(obj, 8)

#inorder(obj)
#pivotTree(obj)
#preorder(obj)
postorder(obj)
#searchTree(obj, 5)