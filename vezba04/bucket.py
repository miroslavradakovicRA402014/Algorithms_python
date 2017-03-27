import math
import insertion

def bucketSort(Arr):
   n = len(Arr)
   B = []
   for i in range(0,n):
     B.append([])
   for i in range(0,n):
     B[math.floor(n*Arr[i])].append(Arr[i])
   for i in range(0,n):
     insertion.insertionSort(B[i])
   ArrSort = []
   for i in range(0,n):
     ArrSort += B[i]
     #print (B[i])   
   return ArrSort