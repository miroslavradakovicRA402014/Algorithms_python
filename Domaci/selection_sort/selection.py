def minSearch(Arr,ind):
   minVal = Arr[ind]
   minInd = ind
   n = len(Arr)
   for i in range(ind+1,n):
      if minVal > Arr[i]:
        minVal = Arr[i]
        minInd = i
   return minInd

def selectionSort(Arr):
   minInd = 0
   n = len(Arr)
   for i in range(0,n):
     minInd = minSearch(Arr,i)
     if minInd != i:
       t = Arr[i]
       Arr[i] = Arr[minInd]
       Arr[minInd] = t 