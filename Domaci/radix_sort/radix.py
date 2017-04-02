def maxDig(Arr):
    num = max(Arr)
    return digNum(num)

def digNum(Num):
    dig = 1
    while Num//10 != 0:
     dig += 1
     Num = Num//10
    return dig   

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


def radixSort(Arr):
    steps = maxDig(Arr)
    for i in range(0,steps):
      insertionSortDigit(Arr,i+1)