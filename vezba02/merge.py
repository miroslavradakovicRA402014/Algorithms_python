def merge(A,p,q,r):
    n1 = q - p + 1
    n2 = r - q
    Left = []
    Right = []
    for i in range(0,n1):
      Left.insert(i,A[p+i])
    for j in range(0,n2):
      Right.insert(j,A[q+j+1])
    i = 0
    j = 0
    k = 0
    #for k in range(p,r+1):
    #    if Left[i] <= Right[j]:
    #       A[k] = Left[i]
    #       i += 1
    #    else: 
    #       A[k] = Right[j]
    #       j += 1
    while i < n1 and j < n2:
          if Left[i] <= Right[j]:
            A[p+k] = Left[i]
            k += 1
            i += 1
          else:
            A[p+k] = Right[j]
            k += 1
            j += 1
   
    while i < n1:
          A[p+k] = Left[i]
          k += 1       
          i += 1
    while j < n2:
          A[p+k] = Right[j]
          k += 1
          j += 1

