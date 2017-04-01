def nDig(Num,n):
    return (Num%(10**n))//(10**(n-1))
    

def insertionSortDigit(Arr,dig):
    for j in range(0,len(Arr)):
     i = j-1
     keyDig = nDig(Arr[j],dig)
     keyNum = Arr[j]; 
     while i >= 0 and keyDig < nDig(Arr[i],dig):
        Arr[i+1] = Arr[i]
        i -= 1
     Arr[i+1] = keyNum

def radixSort(Arr,n):
    for i in range(0,n):
      insertionSortDigit(Arr,i+1)