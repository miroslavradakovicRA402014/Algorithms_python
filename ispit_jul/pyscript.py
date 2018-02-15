import vertex_example

time = 0
vertexStack = []
treeList = []

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
		
	def addEdgeToGraph(self, edge):
		
		(self.edges).append(edge)	
		
	def addVertexAdjacent(self, vertexNum, vertex):
	
		(self.vertexes[vertexNum].adjacency).append(vertex)	
	
	def printGraph(self):
	
		print ("==============VERTEXES==============")
		for v in self.vertexes:
			v.printVertex()	
			
	def printEdges(self):
		print ("==============EDGES==============")
		for e in self.edges:
			print ("\n#######################")
			print ("Source :", e.source.name)
			print ("Destination :", e.destination.name)
			print ("Edge weight :", e.weight)		
				

def makeGraph(graph):

	vertexA = vertex_example.Vertex(i = 0, n = 'a')	
	vertexB = vertex_example.Vertex(i = 1, n = 'b')	
	vertexC = vertex_example.Vertex(i = 2, n = 'c')	
	vertexD = vertex_example.Vertex(i = 3, n = 'd')	
	vertexE = vertex_example.Vertex(i = 4, n = 'e')			
	vertexF = vertex_example.Vertex(i = 5, n = 'f')
	
	graph.addVertexToGraph(vertexA)	
	graph.addVertexToGraph(vertexB)	
	graph.addVertexToGraph(vertexC)	
	graph.addVertexToGraph(vertexD)	
	graph.addVertexToGraph(vertexE)
	graph.addVertexToGraph(vertexF)
	
	graph.addVertexAdjacent(0, vertexB)						
	graph.addVertexAdjacent(0, vertexD)
	
	graph.addVertexAdjacent(1, vertexE)
	
	graph.addVertexAdjacent(2, vertexE)
	graph.addVertexAdjacent(2, vertexF)				
			
	graph.addVertexAdjacent(3, vertexB)
	
	graph.addVertexAdjacent(4, vertexD)
	
	graph.addVertexAdjacent(5, vertexF)
	
	edgeAB = Edge(vertexA, vertexB, w = 2)
	edgeAD = Edge(vertexA, vertexD, w = 6)
	edgeBE = Edge(vertexB, vertexE, w = 1)
	edgeED = Edge(vertexE, vertexD, w = 8)
	edgeDB = Edge(vertexD, vertexB, w = 4)
	edgeCE = Edge(vertexC, vertexE, w = 2)
	edgeCF = Edge(vertexC, vertexF, w = 4)
	edgeFF = Edge(vertexF, vertexF, w = 0)
	
	graph.addEdgeToGraph(edgeAB)
	graph.addEdgeToGraph(edgeAD)
	graph.addEdgeToGraph(edgeBE)
	graph.addEdgeToGraph(edgeED)
	graph.addEdgeToGraph(edgeDB)
	graph.addEdgeToGraph(edgeCE)
	graph.addEdgeToGraph(edgeCF)
	graph.addEdgeToGraph(edgeFF)	
	
def transponseGraph(graph):

	tranGraph = Graph()
	
	for v in graph.vertexes:
		vertex = vertex_example.Vertex(n = v.name, i = v.id)
		tranGraph.addVertexToGraph(vertex)
	
	for e in graph.edges:
		edge = Edge(e.destination, e.source, w = e.weight)													
		tranGraph.addEdgeToGraph(edge)
	
	for e in tranGraph.edges:
		tranGraph.addVertexAdjacent(e.source.id, tranGraph.vertexes[e.destination.id])			
	
	return tranGraph

def applyDFS(graph):

	for u in graph.vertexes:
		u.color = vertex_example.VertexColor.WHITE
		u.prev = None
		 
	global time	
	time = 0
	
	for u in graph.vertexes:
		if u.color == vertex_example.VertexColor.WHITE:
			DFSvisit(graph,u)

def DFSvisit(graph, u):
	
	global time
	global vertexStack
	time += 1
	u.start = time
	u.color = vertex_example.VertexColor.GRAY
	
	for v in u.adjacency:
		if v.color == vertex_example.VertexColor.WHITE:
			v.prev = u
			DFSvisit(graph, v)
	
	u.color = vertex_example.VertexColor.BLACK
	time += 1
	u.finish = time
	vertexStack.append(u.id)

def DFSvisitInOrder(graph, u, listT):

	global vertexStack
	u.color = vertex_example.VertexColor.GRAY
	listT.append(u)
	vertexStack.remove(u.id)
	
	for v in u.adjacency:
		if v.color == vertex_example.VertexColor.WHITE:
			v.prev = u
			DFSvisitInOrder(graph, v, listT)
	
	u.color = vertex_example.VertexColor.BLACK
			 	
def printVertexTimes(graph):

	for v in graph.vertexes:
		print ("\n#######################")
		print ("Vertex name :", v.name)
		print ("Start time :", v.start)
		print ("Finish time :", v.finish)
		

def applyDFSinOrder(graph):

	global vertexStack
	global treeList
	
	for u in graph.vertexes:
		u.color = vertex_example.VertexColor.WHITE
		u.prev = None
	
	vertexStack.reverse()

	while vertexStack != []:
		listT = []	
		DFSvisitInOrder(graph, graph.vertexes[vertexStack[0]], listT)			
		treeList.append(listT)
		
def printStronglyConnectedComponents():

	global treeList
	
	print ("Strongly connected components")
	for l in treeList:
		print ("Component")
		for v in l:
			print (v.name)
			
def applyStronglyConnectedComponents():

	graph = Graph()
	makeGraph(graph)
	applyDFS(graph)	
	transponsedGraph = transponseGraph(graph)	
	#transponsedGraph.printGraph()
	applyDFSinOrder(transponsedGraph)		
	printStronglyConnectedComponents()	
	
################################################################################

applyStronglyConnectedComponents()									
