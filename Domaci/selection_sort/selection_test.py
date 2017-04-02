import selection


testArr1 = []

for i in range(99,-1,-1):
   testArr1.append(i)
 
 
testArr2 = []

for i in range(999,-1,-1):
   testArr2.append(i)   
   
 
testArr3 = []

for i in range(9999,-1,-1):
   testArr3.append(i)    
   

Arr1 = range(0,100)
Arr2 = range(0,1000)
Arr3 = range(0,10000)

selection.selectionSort(testArr1)
selection.selectionSort(testArr2)
selection.selectionSort(testArr3)

pass1 = 1
pass2 = 1
pass3 = 1

for i in range(0,100):
   if testArr1[i] != Arr1[i]:
     pass1 = 0
     break
    
    
for i in range(0,1000):
   if testArr2[i] != Arr2[i]:
     pass2 = 0
     break   

    
for i in range(0,10000):
   if testArr3[i] != Arr3[i]:
     pass3 = 0
     break
    
     
if pass1 == 1:
   print ("Test1 passed")
else: 
   print ("Test1 is not passed")
   
if pass2 == 1:
   print ("Test2 passed")
else: 
   print ("Test2 is not passed")   

if pass3 == 1:
   print ("Test3 passed")
else: 
   print ("Test3 is not passed") 