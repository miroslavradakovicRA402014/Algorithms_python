
def parent(i):
    if i % 2 == 0 :
      return i/2 - 1
    else:
      return i//2

def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2


def maxHeapify(Arr,i,heapSize):

    l = left(i)
    r = right(i)

    if l <= heapSize-1 and Arr[l] > Arr[i]:
       largest = l
    else:
       largest = i

    if r <= heapSize-1 and Arr[r] > Arr[largest]:
       largest = r

    if largest != i:
       t = Arr[largest]
       Arr[largest] = Arr[i]
       Arr[i] = t 
       maxHeapify(Arr,largest,heapSize)

def buildMaxHeap(Arr,heapSize):
    leng = len(Arr)//2
    for i in range(leng-1,-1,-1):
        maxHeapify(Arr,i,heapSize)

def heapSort(Arr,heapSize):
    buildMaxHeap(Arr,heapSize)
    for i in range(len(Arr)-1,0,-1):
        t = Arr[0]
        Arr[0] = Arr[i]
        Arr[i] = t 
        heapSize -= 1
        maxHeapify(Arr,0,heapSize)

def heapMaximum(Arr): 
    return Arr[0]

def heapInsertKey(Arr,key,heapSize):
    heapSize += 1
    Arr.insert(heapSize-1,-50000000)
    heapIncreaseKey(Arr,heapSize-1,key,heapSize)

def heapIncreaseKey(Arr,i,key,heapSize):
    if key < Arr[i]: 
       return "Error"
    p = parent(i)
    Arr[i] = key
    while i > 0 and Arr[p] < Arr[i]:
        t = Arr[p]
        Arr[p] = Arr[i]
        Arr[i] = t 
        i = p
def heapExtraxtMax(Arr,heapSize):
    if heapSize <= 0:
      return "Heap empty"
    maxel = Arr[0]
    Arr[0] = Arr[heapSize - 1]
    heapSize -= 1
    maxHeapify(Arr,0,heapSize)
    return maxel
          