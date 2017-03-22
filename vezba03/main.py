import heapfunctions

Arr = [2,16,5,7,11,9,7,8,1]
heapSize = 9

heapfunctions.buildMaxHeap(Arr,heapSize)

print (Arr)
heapfunctions.heapSort(Arr,heapSize)
print (Arr)

heapfunctions.heapInsertKey(Arr,10,heapSize)
el = heapfunctions.heapExtraxtMax(Arr,heapSize)

if el == "Heap empty":
   print (el)
else:
   print (el)
   print (Arr)  
