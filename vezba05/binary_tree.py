import class_example

def printNode(node):
    print ("\nNode")
    print ("Key :",node.data.a1)
  
def addRight(root,right):
    root.right = right
    right.parent = root
    
def addLeft(node,left):
    root.left = left   
    left.parent = root  
    
    
def inorderTreeWalk(node):
    if node != None:
      inorderTreeWalk(node.left)
      printNode(node)
      inorderTreeWalk(node.right) 
      
def treeSearch(node,key):
    if node == None or node.data.a1 == key:
       return node
    
    if node.data.a1 > key:
       return treeSearch(node.left,key)
    else: 
       return treeSearch(node.right,key)
       
def iterativeTreeSearch(node,key):
    while node != None and node.data.a1 != key:
          if node.data.a1 > key:
             node = node.left
          else:
             node = node.right
    return node   
    
def treeMinimum(root):
    if root.left != None:
       return treeMinimum(root.left)
    return root
      
def treeMaximum(root):
    if root.right != None:
       return treeMaximum(root.right)
    return root

def treeSuccesor(node):
    if node.right != None:
       return treeMinimum(node.right)
    
    par = node.parent
    
    while par.parent != None and par.right == node:
          par = par.parent
          
    return par.data.a1   
    
def treeInsert(root,node):

    y = None
    x = root
    while x != None:
      y = x
      if node.data.a1 < x.data.a1:
          x = x.left
      else:
          x = x.right
    node.parent = y          
    if y == None:
       root = z
    elif node.data.a1 < y.data.a1:
       y.left = node
    else:
       y.right = node              
                                        

def transplant(root,u,v):
    if u.parent == None:
       root = v
    elif u == u.parent.left:
       u.parent.left = v
    else:
       u.parent.right = v   
    if v != None:
       v.parent = u.parent 
       
def treeDelete(root,node):
    if node.left == None:
       transplant(root,node,node.right)
    elif node.right == None:
       transplant(root,node,node.left)
    else: 
       y = treeMinimum(node.right)
       if y.parent != node:
          transplant(root,y,y.right)
          y.right = node.right
          y.right.parent = y
       transplant(root,node,y)
       y.left = node.left
       y.left.parent = y      
                         
        
##################################################################################################        
rootData = class_example.Data(2,"2")
root = class_example.Node(None,None,None,rootData)

leftNodeData = class_example.Data(1,"1")
leftNode  = class_example.Node(None,None,None,leftNodeData)

rightNodeData = class_example.Data(3,"3")
rightNode = class_example.Node(None,None,None,rightNodeData)

addRight(root,rightNode)
addLeft(root,leftNode)

'''
inorderTreeWalk(root)
node = iterativeTreeSearch(root,3)
if node != None:
   printNode(node)
else:    
   print ("Don't exist that node whit that key")

treeMax = treeMaximum(root)
print ("Tree maximum ",treeMax.data.a1)
treeMin = treeMinimum(root)
print ("Tree minmum ",treeMin.data.a1)

succ = treeSuccesor(root)
print (succ.data.a1)
'''

nodeData = class_example.Data(4,"4")
node = class_example.Node(None,None,None,nodeData)

treeInsert(root,node)
inorderTreeWalk(root)

treeDelete(root,rightNode)
inorderTreeWalk(root)

   