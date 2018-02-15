import sys

class Object:
	def __init__(self,v = 0,f = 0,l = None, r = None, p = None):
		self.value = v
		self.freq = f
		self.left = l
		self.right = r
		self.parent = p
		
	def printObject(self):
		print ("\n-------------------")
		if self.value != 0:
			print ("Value ", self.value)
			print ("Freq  ", self.freq)
		else:
			print ("Freq ", self.freq)	
		print ("-------------------")		
			
def getHistogram(hist):
	fin = open("snippets.txt", 'r')
	for line in fin:
		word = line.split()
		for char in word:
			if not char in hist.keys():
				hist[char] = 1
			else:
				hist[char] += 1							
	fin.close()				
	printHistogram(hist)
	
def printHistogram(hist):
	print (hist)	
	
def makeNewElement(val,freq,left,right):
	obj = Object(v = val, f = freq, l = left, r = right, p = None)
	return obj
	
def getMinFreqElement(charList):
	minel = charList[0]
	for c in charList:
		if minel.freq >= c.freq:
			minel = c	
	#print ("Min freq element")
	#minel.printObject()		
	return minel
	
def removeElement(charList,el):
	charList.remove(el)
	
def putElement(charList):
	minElementLeft = getMinFreqElement(charList)
	removeElement(charList,minElementLeft) 
	minElementRight = getMinFreqElement(charList)
	removeElement(charList,minElementRight)
	'''
	print ("\n	#############################")
	print ("	Left child")
	minElementLeft.printObject()
	print ("	Right child")
	minElementRight.printObject()
	'''
	root = makeNewElement(0,minElementLeft.freq + minElementRight.freq,minElementLeft,minElementRight)
	
	minElementRight.parent = root
	minElementLeft.parent = root
	
	charList.append(root)
		
def createCharList(hist,charList):
	for k in hist.keys():
		el = makeNewElement(k,hist.get(k),None,None) 
		charList.append(el)
		
def printCharList(charList):
	for el in charList:
		el.printObject()
		
def makeHuffman(charList):				
	while len(charList) != 1:	
		putElement(charList)
		
'''
def getEncVal(root,hist,val):
	freq = hist.get(val)
	print (val)
	retVal = ''
	while root != None and root.value != val:
		root.printObject()
		if root.freq > freq:
			retVal += '0'
			root = root.left
		else:
			retVal += '1'
			root = root.right		
	return retVal			
'''
def getElement(root,val):
	if root != None:
		if root.value == val:
			return root
		else:
			retR =  getElement(root.right,val)  
			retL =  getElement(root.left,val)
			if retR != None:
				return retR
			else:
				return retL	
	else:
		return None
		
def getEncVal(root,val,encList):		
	el = getElement(root,val)
	while el.parent != None:
		if el == el.parent.right:
			encList.append('1')
		else:
			encList.append('0')
		el = el.parent
	
def inorderHuffmanWalk(root):
	if root != None:
		root.printObject()
		inorderHuffmanWalk(root.right)
		inorderHuffmanWalk(root.left)	
###################################################	
hist = {}
charList = []
encList = []

getHistogram(hist)
createCharList(hist,charList)
	
#printCharList(charList)	
#el = getMinFreqElement(charList)

makeHuffman(charList)
print (getEncVal(charList[0],'f',encList))
#inorderHuffmanWalk(charList[0])
encList.reverse()
print (encList)
