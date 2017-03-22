
def binary(A,el,p,r):
    mid = p + (r - p)//2
    if A[mid] == el:
       return mid
    elif mid == 0 or mid == r:
       return -1
    elif A[mid] > el:
       return binary(A,el,0,mid-1)
    else:
       return binary(A,el,mid+1,r)
    