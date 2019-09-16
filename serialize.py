class Node: 
    def __init__(self,key=-1): 
        self.left = None
        self.right = None
        self.val =  key
  
  
# A function to do inorder tree traversal 
def serialize(root): 
    if root: 
        print(root.val) 
        serialize(root.left)  
        serialize(root.right)
    else:
        print("-1")

def deSerialize(root, s):
    root.val = s[0]
    if(s[1]!=-1):
        root.left = Node()
        deSerialize(root.left, s[1:])
    if(s[2]!= -1):
        root.right = Node
        deSerialize(root.right,s[2:])
    return root

if __name__ == '__main__':
    root = Node(key=1)
    root.left      = Node(key=2) 
    root.right     = Node(key=3) 
    root.left.left  = Node(key=4) 
    root.left.right  = Node(key=5)
    serialize(root)
    # serial = [1,2,4,-1,-1,5,-1,-1,3,-1,-1]
    # newRoot = Node(key=10)
    # newRoot = deSerialize(newRoot,serial)
    # serialize(newRoot)
 