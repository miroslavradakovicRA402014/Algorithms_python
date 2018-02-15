import vertex_example
import math

class Edge:
	
	def __init__(self, s = None, d = None, w = 0):
		
		self.source = s
		self.destination = d
		self.weight = w
			

class Graph:

	def __init__(self):
	
		self.vertexes = []
		self.vertexNum = 0
		self.edges = []
		
	def addVertexToGraph(self, vertex):	 
		
		(self.vertexes).append(vertex)
		self.vertexNum += 1
		
	def addVertexAdjecent(self, vertexNum, vertex):
	
		(self.vertexes[vertexNum].adjacency).append(vertex)
		
	def addEdgeToGraph(self, edge):
		
		self.edges.append(edge)
		
	def printEdges(self):
		
		print ("================EDGES===================")
		for e in self.edges:
			print ("\n######################");
			print ("Edge source :", e.source.name)
			print ("Edge destionation :", e.destination.name)
			print ("Edge weight :", e.weight)		
		
	def printGraph(self):
	
		print ("================VERTEXES===================")
	
		for v in self.vertexes:
			v.printVertex()
					
			
def makeGraph(graph):			
	
	vertexA = vertex_example.Vertex(n = 'a', d = 0) 
	vertexB = vertex_example.Vertex(n = 'b', d = 1)
	vertexC = vertex_example.Vertex(n = 'c', d = 2)
	vertexD = vertex_example.Vertex(n = 'd', d = 3)
	vertexE = vertex_example.Vertex(n = 'e', d = 4)
	vertexF = vertex_example.Vertex(n = 'f', d = 5)
	vertexG = vertex_example.Vertex(n = 'g', d = 6)
	
	graph.addVertexToGraph(vertexA)
	graph.addVertexToGraph(vertexB)
	graph.addVertexToGraph(vertexC)
	graph.addVertexToGraph(vertexD)
	graph.addVertexToGraph(vertexE)
	graph.addVertexToGraph(vertexF)
	graph.addVertexToGraph(vertexG)				
	
	graph.addVertexAdjecent(0, vertexC)
	graph.addVertexAdjecent(0, vertexB)
	
	graph.addVertexAdjecent(1, vertexD)
	
	graph.addVertexAdjecent(2, vertexD)
	graph.addVertexAdjecent(2, vertexE)
		
	graph.addVertexAdjecent(3, vertexE)
	graph.addVertexAdjecent(3, vertexF)
	
	graph.addVertexAdjecent(4, vertexF)
	graph.addVertexAdjecent(4, vertexG)
	
	graph.addVertexAdjecent(5, vertexG)
	
	edgeAC = Edge(vertexA, vertexC, 6)
	edgeAB = Edge(vertexA, vertexB, 8)
	edgeBD = Edge(vertexB, vertexD, 10)
	edgeCD = Edge(vertexC, vertexD, 15)
	edgeCE = Edge(vertexC, vertexE, 9)
	edgeDE = Edge(vertexD, vertexE, 14)
	edgeDF = Edge(vertexD, vertexF, 4)
	edgeEG = Edge(vertexE, vertexG, 17)
	edgeEF = Edge(vertexE, vertexF, 13)
	edgeFG = Edge(vertexF, vertexG, 7)
	
	graph.addEdgeToGraph(edgeAC)
	graph.addEdgeToGraph(edgeAB)
	graph.addEdgeToGraph(edgeBD)
	graph.addEdgeToGraph(edgeCD)
	graph.addEdgeToGraph(edgeCE)
	graph.addEdgeToGraph(edgeDE)
	graph.addEdgeToGraph(edgeDF)
	graph.addEdgeToGraph(edgeEG)
	graph.addEdgeToGraph(edgeEF)
	graph.addEdgeToGraph(edgeFG)								
	
def getOutDegrees(graph):
	
	outDeg = []
	
	for v in graph.vertexes:
		print ("Vertex name :", v.name)
		print ("Vertex out degree :", len(v.adjacency))
		outDeg.append(len(v.adjacency))
				
	return outDeg			
				
def getOutDegrees(graph):
	
	outDeg = []
	print ("================OUT DEGREE===================")	
	for v in graph.vertexes:
		print ("######################")
		print ("Vertex name :", v.name)
		print ("Vertex out degree :", len(v.adjacency))

		outDeg.append(len(v.adjacency))
				
	return outDeg
	
def getInDegrees(graph):

	inDeg = []
	print ("================IN DEGREE===================")		
	for v in graph.vertexes:
		d = 0
		for vd in graph.vertexes: 
			for a in vd.adjacency:
				if v == a:
					d += 1 
		inDeg.append(d)	
		print ("######################")
		print ("Vertex name :", v.name)
		print ("Vertex in degree :", d)

def edgeWeight(graph, u, v):
	
	for e in graph.edges:
		if e.source == u and e.destination == v:
			return e.weight
		
def relaxEdge(graph, u, v):
	
	if v.data > u.data + edgeWeight(graph,u,v):
		v.data = u.data + edgeWeight(graph,u,v)
		v.prev = u	 		
		
def initializeSingleSource(graph, s):

	for v in graph.vertexes:
		v.data = math.inf
		v.prev = None	
					
	s.data = 0
	
def bellmanFord(graph, s):
	
	initializeSingleSource(graph, s)

	for i in range(0, len(graph.vertexes) - 1):
		for e in graph.edges:
			relaxEdge(graph, e.source, e.destination)
			
def shortestPath(graph, u, v):
		
	path = []
	distance = 0
	
	bellmanFord(graph, u)
	
	distance = v.data
	
	prev = v.prev
	while prev != u:
		path.append(prev.name)
		prev = prev.prev

	print ("Shortest path from ",u.name," to ",v.name,"is")
	print (path)
	print ("Distance from ",u.name," to ",v.name,"is",distance)
		
	retVal  = (path, distance)
		
	return retVal
	
def updateEdge(graph, u, v, weight):

	for e in graph.edges:
		if e.source == u and e.destination == v:
			e.weight = weight
			return e
	
	edge = Edge(u, v, weight)
	graph.addEdgeToGraph(edge)
	
	return None				
		 		
								
#####################################################################

graph = Graph()
makeGraph(graph)

graph.printGraph()	
graph.printEdges()	
			
#getOutDegrees(graph)
#getInDegrees(graph)

#shortestPath(graph,graph.vertexes[0], graph.vertexes[6])
	
updateEdge(graph, graph.vertexes[1], graph.vertexes[2], -4)
graph.printEdges()	

shortestPath(graph,graph.vertexes[0], graph.vertexes[6])	
	
	
		
	
	
	
