import quick
import bucket

Arr1 = [-5,10,7,9,1,11,2,4,8,-2]
Arr2 = [0.1,0.8,0.76,0.25,0.01]
Arr2Sort = []

print (Arr1)

quick.randomizedQuickSort(Arr1,0,len(Arr1)-1)

print (Arr1)

print (Arr2)

Arr2Sort = bucket.bucketSort(Arr2)

print (Arr2Sort)