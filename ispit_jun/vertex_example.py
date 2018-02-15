from enum import Enum	

class VertexColor(Enum):
        BLACK = 0
        GRAY = 127
        WHITE = 255	

class Vertex:
    """
    Graph vertex: A graph vertex (node) with data
    """
    def __init__(self, c = VertexColor.WHITE , p = None, n = None, d = None):

        self.color = c
        self.prev = p
        self.name = n
        self.data = d
        self.adjacency = []
        	           
    def printVertex(self):

    	print ("\n######################")
    	print ("Vertex name :", self.name)
    	if self.adjacency != []: 
    		print ("Vertex adjacency")
    	for v in self.adjacency:
    	    print ("Adjacent vertex name :", v.name)
	
	
		



