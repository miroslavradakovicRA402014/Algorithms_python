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
    return int((Num/(10**(n-1)))%10)
    
def countingSortDigit(Arr,B,k,dig):
    C = []
    for i in range(0,k):
      C.append(0)
    for j in range(0,len(Arr)):
      C[nDig(Arr[j],dig)] = C[nDig(Arr[j],dig)] + 1
    for i in range(1,k):
      C[i] = C[i] + C[i-1]
    for j in range(len(Arr)-1,-1,-1):
      C[nDig(Arr[j],dig)] = C[nDig(Arr[j],dig)] - 1    
      B[C[nDig(Arr[j],dig)]] = Arr[j]
    Arr[:] = B[:]  

def radixSort(Arr,B):
    steps = maxDig(Arr)
    for i in range(0,steps):
      countingSortDigit(Arr,B,10,i+1)