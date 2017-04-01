import selection
import radix
import radix_n

Arr1 = [-10,20,5,11,8,2,6,16,4,-1,17]
Arr2 = [58,1234,2,58887,32,111]
Arr3 = [329,457,657,839,436,720,355]

print (Arr1)

selection.selectionSort(Arr1)

print (Arr1)

print (Arr2)

radix.radixSort(Arr2)

print (Arr2)

#n = radix.nDig(59887,1)

#print (n)

print (Arr3)

radix.radixSort(Arr3)

print (Arr3)
