from enum import Enum	

class VertexColor(Enum):
        BLACK = 0
        GRAY = 127
        WHITE = 255	

class Vertex:
    """
    Graph vertex: A graph vertex (node) with data
    """
    def __init__(self, c = VertexColor.WHITE, p = None, n = None, s = 0, f = 0, i = 0):

        self.color = c
        self.prev = p
        self.name = n
        self.start = s
        self.finish = f
        self.id = i
        self.adjacency = []
   
    def printVertex(self):	
    	
    	print ("\n#######################")
    	print ("Vertex name :", self.name)
    	if self.color == VertexColor.WHITE: 
    		print ("Color WHITE")
    	elif self.color == VertexColor.GRAY: 
    		print ("Color GRAY")
    	else:
    		print ("Color BLACK")				
    	
    	if self.adjacency != []:
    		print ("Vertex adjacency ")
    	for v in self.adjacency:
    		print ("Vertex name :", v.name)
    		if v.color == VertexColor.WHITE: 
    			print ("Color WHITE")
    		elif v.color == VertexColor.GRAY: 
    			print ("Color GRAY")
    		else:
    			print ("Color BLACK")   		
		
		



