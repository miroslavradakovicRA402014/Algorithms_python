import radix_n


testArr1 = []

for i in range(99,9,-1):
   testArr1.append(i)
 
 
testArr2 = []

for i in range(999,99,-1):
   testArr2.append(i)   
   
 
testArr3 = []

for i in range(9999,999,-1):
   testArr3.append(i)    
   

Arr1 = range(10,100)
Arr2 = range(100,1000)
Arr3 = range(1000,10000)

radix_n.radixSort(testArr1,2)
radix_n.radixSort(testArr2,3)
radix_n.radixSort(testArr3,4)

pass1 = 1
pass2 = 1
pass3 = 1

for i in range(0,len(testArr1)):
   if testArr1[i] != Arr1[i]:
     pass1 = 0
     break
    
    
for i in range(0,len(testArr2)):
   if testArr2[i] != Arr2[i]:
     pass2 = 0
     break   

    
for i in range(0,len(testArr3)):
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

      

