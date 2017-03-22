import insertion
import mergesort
import linearsearch
import binarysearch

Arr1 = [-3,5,8,7,1,-2,4]
Arr2 = [5,8,-6,12,3,7,1,9,10]
Arr3 = [44,31,-61,12,3,71,1,19,56,-25]

print ("Unsorted array :")
print (Arr1)

print ("Unsorted array :")
print (Arr2)

insertion.insertionSort(Arr1)

print ("Sorted array :")
print (Arr1)

mergesort.mergeSort(Arr2,0,8)

print ("Sorted array :")
print (Arr2)

ind = linearsearch.linear(Arr3,12)

if ind != -1:
   print ("Index of elemet ",ind)
else:
   print ("Element don't exist ")


insertion.insertionSort(Arr3)

ind = binarysearch.binary(Arr3,71,0,len(Arr3)-1)

if ind != -1:
   print ("Index of elemet ",ind)
else:
   print ("Element don't exist ")