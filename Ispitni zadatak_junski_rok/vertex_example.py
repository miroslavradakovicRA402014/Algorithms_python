
class Vertex:
    """
    Graph vertex: A graph vertex (node) with data
    """
    def __init__(self, d = None ,p = None,ds = 0):
        """
        Vertex constructor 
        @param auxilary data1, auxilary data2
        """
        self.data = d
        self.adjacency = []
        self.distance = ds
        self.prev = p
        
    def printAdjacent(v):
        print (v.data)               
    
class Data:
    """
    Graph data: Any object which is used as a graph vertex data
    """
    def __init__(self, val1):
        """
        Data constructor
        @param A list of values assigned to object's attributes
        """
        self.a1 = val1
		
		



