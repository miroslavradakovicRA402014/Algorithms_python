import merge

def mergeSort(A,p,r):
   if p < r:
    q = (r + p)//2
    mergeSort(A,p,q)
    mergeSort(A,q+1,r)
    merge.merge(A,p,q,r)