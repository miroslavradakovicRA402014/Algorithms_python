import random

def partition(Arr,p,r):
  x = Arr[r]
  i = p - 1
  for j in range(p,r-1):
     if Arr[j] <= x:
       i += 1
       t = Arr[i]
       Arr[i] = Arr[j]
       Arr[j] = t
  t = Arr[i+1] 
  Arr[i+1] = Arr[r]
  Arr[r] = t
  return i+1

def randomizedPartition(Arr,p,r):
   i = random.randint(p,r)
   t = Arr[r]
   Arr[r] = Arr[i]
   Arr[i] = t
   return partition(Arr,p,r)

def randomizedQuickSort(Arr,p,r):
   if p < r:
    q = randomizedPartition(Arr,p,r)
    randomizedPartition(Arr,p,q-1)
    randomizedPartition(Arr,q+1,r)