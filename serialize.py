class Node: 
    def __init__(self,key=-1): 
        self.left = None
        self.right = None
        self.val =  -1
  
  
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
        deSerialize(root.left, s[1:])
    if(s[2]!= -1):
        deSerialize(root.right,s[2:])
    return
 