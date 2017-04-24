import class_example
import random

class Tree:
    def __init__ (self,r = None):
      self.root = r

def printNode(node):
    print ("\nNode")
    print ("Key :",node.data.a1)
  
def addRight(root,right):
    root.right = right
    right.parent = root
    
def addLeft(root,left):
    root.left = left   
    left.parent = root  
    
    
def inorderTreeWalk(node):
    if node != None:
      inorderTreeWalk(node.left)
      printNode(node)
      inorderTreeWalk(node.right) 
      
def inorderTreeWalkInsert(node,l):
    if node != None:
      inorderTreeWalkInsert(node.left,l)
      l.append(node.data.a1)
      inorderTreeWalkInsert(node.right,l)      
      
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
    
def treeInsert(tree,node):
    y = None
    x = tree.root          
    while x != None:
      y = x
      if node.data.a1 < x.data.a1:
          x = x.left
      else:
          x = x.right
    node.parent = y          
    if y == None:
       tree.root = node
    elif node.data.a1 < y.data.a1:
       y.left = node
    else:
       y.right = node   
          
          
                                                                        
def transplant(tree,u,v):
    if u.parent == None:
       tree.root = v
    elif u == u.parent.left:
       u.parent.left = v
    else:
       u.parent.right = v   
    if v != None:
       v.parent = u.parent 
       
def treeDelete(tree,node):
    if node.left == None:
       transplant(tree,node,node.right)
    elif node.right == None:
       transplant(tree,node,node.left)
    else: 
       y = treeMinimum(node.right)
       if y.parent != node:
          transplant(tree,y,y.right)
          y.right = node.right
          y.right.parent = y
       transplant(tree,node,y)
       y.left = node.left
       y.left.parent = y      
                         
def createNode(data):
    nodeData = class_example.Data(data,str(data))
    node = class_example.Node(None,None,None,nodeData)    
    return node 
           
##################################################################################################        
'''
rootData = class_example.Data(2,"2")
root = class_example.Node(None,None,None,rootData)

leftNodeData = class_example.Data(1,"1")
leftNode  = class_example.Node(None,None,None,leftNodeData)

rightNodeData = class_example.Data(3,"3")
rightNode = class_example.Node(None,None,None,rightNodeData)

addRight(root,rightNode)
addLeft(root,leftNode)

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

nodeData = class_example.Data(4,"4")
node = class_example.Node(None,None,None,nodeData)

treeInsert(root,node)
inorderTreeWalk(root)

treeDelete(root,rightNode)
inorderTreeWalk(root)
'''
n = 10
l = []
sl = []
'''
l.append(random.randint(0,100))
treeRoot = createNode(l[0])

for i in range(1,n):
   l.append(random.randint(0,100))
   node = createNode(l[i])
   treeInsert(treeRoot,node)                
'''

treeRoot = Tree()

for i in range(0,n):
   l.append(random.randint(0,100))
   node = createNode(l[i])
   treeInsert(treeRoot,node)
                    
print (l)
inorderTreeWalkInsert(treeRoot.root,sl)
print (sl)     





