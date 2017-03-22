import functions
import sys

sum = functions.sumN()
print ("Sum of the first 100 numbers is ",sum)

if len(sys.argv) == 4:
 
   sumsqr = functions.sumNsqr(int(sys.argv[1]))
   print ("Square sum of the first ",sys.argv[1],"numbers is ",sumsqr)

   str1 = sys.argv[2]
   str2 = sys.argv[3]
    
   if len(str1) > 3 and len(str2) > 3:

      substr = str1[0:3] + str2[(len(str2)-3):]
      outstr = substr*2

      print ("String 1: ",str1," String 2: ",str2)
      print ("Result string :",outstr)
else:
   print ("Don't enough arguments")

numlist = []

for it in range(1,11):
    numlist.append(it)

numlist.reverse()
print (numlist)

tup1 = (10,2.71,"Tuple1")
tup2 = (11,3.14,"Tuple2")
tup3 = (12,1.71,"Tuple3")
tup4 = (13,1.41,"Tuple4")

tuplist = []
tuplist = [tup1,tup2,tup3,tup4]

print (tuplist)

del tuplist[0]

tupset = set()
tupset = {tup1, tup2 , tup3 ,tup4}
tupsetdiff = {tup1}

print (tupset)

tupset = tupset - tupsetdiff
#-------------------------------------------
worddic = {}
wordlist = []

fin = open("dict_test.txt",'r')
 
for line in fin:
   wordlist = line.split()
   for word in wordlist:
     if not word in worddic.keys():
       worddic[word] = 1
     else:
       worddic[word] += 1

print (worddic)

fin.close()

