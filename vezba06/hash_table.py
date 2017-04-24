import random
import math
import time

class Data:
  def __init__(self,k = None,l = None):
      self.key = k
      self.literal = l
####################################################      
def printElement(el):
    if el != None:
     print ("Key :",el.key)
    else:
     print ("Empty") 
####################################################
def divisionMethod(k,m):
    return k % m
    
def multiMethod(k,m):
    return math.floor(m*(k*((math.sqrt(5)-1)/2) % 1))
    
def universalHashing(a,b,m,p):
    return ((a*k+b) % p) % m    
####################################################

def hashFunction1(hf,k,m,a,b,p):
    if hf == 0:
      return divisionMethod(k,m)
    elif hf == 1:
      return multiMethod(k,m)
    else: 
      return universalHashing(a,b,m,p)
      
def chainedHashInsert(T,x,hf,k,m,a,b,p):
    i = hashFunction1(hf,x.key,m,a,b,p)
    T[i].insert(0,x)
    
def chainedHashSearch(T,x,hf,k,m,a,b,p):
    i = hashFunction1(hf,x.key,m,a,b,p)
    for el in T[i]:
      if el.key == x.key:
         return el        
    return None       
    
def chainedHashDelete(T,x,hf,k,m,a,b,p):
    el = chainedHashSearch(T,x.key,hf,k,m,a,b,p)
    if el != None:
       i = hashFunction1(hf,x.key,m,a,b,p)
       T[i].remove(x)   
       
####################################################
def basicHash1(k,m):
    return k % m 

def basicHash2(k,m):
    return 1 + (k % m)    

def linearProbing(k,i,m):
    return (basicHash1(k,m) + i) % m

def quadraticProbing(k,i,m):
    return ((int)(basicHash1(k,m) + 0.5*i + 0.5*(i**2))) % m
    
def doubleHashing(k,i,m):
    return (basicHash1(k,m) + i*basicHash2(k,m-1)) % m  
        
def hashFunction(hf,k,i,m):
    if hf == 0:
      return linearProbing(k,i,m) 
    elif hf == 1:
      return quadraticProbing(k,i,m)
    else: 
      return doubleHashing(k,i,m)
    
def hashInsert(T,k,hf):
    i = 0
    while True:
       j = hashFunction(hf,k,i,len(T))
       if T[j].key == None:
          T[j] = Data(k,str(k))   
          return j
       else:
          i += 1
       if i == m:
          return None
          
def hashSearch(T,k,hf):
    i = 0
    while True:
       j = hashFunction(hf,k,i,len(T))
       if T[j].key == k:   
          return j
       else:
          i += 1
       if T[j] == None or i == m:
          return None
#####################################################             
def printTable(T):
    for i in range(0,len(T)):
      printElement(T[i])          
###################################################### 

keys = []
table = []
n = 10000
m = n//2
p = 23
#m = p
a = 0
b = 0

'''
for i in range(0,m):
    table.append([])
    
for i in range(0,n):
    keys.append(random.randint(0,p-1))
    
print (keys)
    
for i in range(0,n):
    el = Data(keys[i],str(keys[i]))
    chainedHashInsert(table,el,0,len(table),m,a,b,p)
    
print (table)    
'''    

for i in range(0,m):
    table.append(Data())
    
for i in range(0,n):
    keys.append(random.randint(1,n))

'''    
for i in range(0,n):
    hashInsert(table,keys[i],0)  
'''    
    
for i in range(0,n):
    hashInsert(table,keys[i],1) 

'''    
for i in range(0,n):
    hashInsert(table,keys[i],2)         
'''

'''        
print (keys)
printTable(table)   
'''

'''
start_time = time.clock() # expressed in seconds
j = hashSearch(table,2601,0)
end_time = time.clock()
exec_time = (end_time - start_time)*1000 #get miliseconds
print (exec_time)
'''
'''
start_time = time.clock() # expressed in seconds
j = hashSearch(table,2601,1)
end_time = time.clock()
exec_time = (end_time - start_time)*1000 #get miliseconds
print (exec_time)
'''

'''
start_time = time.clock() # expressed in seconds
j = hashSearch(table,2601,2)
end_time = time.clock()
exec_time = (end_time - start_time)*1000 #get miliseconds
print (exec_time)
'''

'''
if j != None:
  print ("Element exist on location",j)
else:
  print ("Element don't exist") 
'''              