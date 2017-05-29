import vertex_example

class Graph:

    def __init__(self,g = None,s = 0,e = None):
        self.graph = g
        self.size = s
        self.edges = e
    def addVertexToGraph(self,vertex):
        self.graph.append(vertex)
        self.size += 1      
    def addVertexAdjacent(self,vertexNum,vertex):
        (self.graph[vertexNum]).adjacency.append(vertex)
    def printAdjacency(self,vertexNum):
        print ("Vertex",(self.graph[vertexNum]).data1,"adjacency ")
        for v in (self.graph[vertexNum]).adjacency:
            v.printAdjacent()
    def printGraphsVertexes(self):
        num = 0
        for v in self.graph:
            print ("==========================================")         
            print ("Vertex num",v.data1)
            print ("Vertex value",v.data2)
            if v.color == vertex_example.VertexColor.WHITE:
              print ("WHITE")
            elif v.color == vertex_example.VertexColor.GRAY:
              print ("GRAY")
            else:
              print ("BLACK")  
            self.printAdjacency(num)        
            num += 1
    def printEdges(self):
        for e in self.graph.edges:
            print ("Source",e.source.data2)
            print ("Destination",d.destination.data2)
            print ("Edge weigth",e.weigth)
            

def edgeWeigth(G,u,v):
    for e in self.graph.edges:
        if e.source == u and e.destination == v:
            return e.weigth


            
def initializeSingleSource(G,s):
    for v in G.graph:
        v.data1 = 100000000
        v.preview = None
    s.data1 = 0
    
def relax(G,u,v):
    if v.data1 > u.data1 + edgeWeigth(G,v,w):
        v.data1 = u.data1 + edgeWeigth(G,v,w)
        v.preview = u 

def dijkstra(G,s):
    initializeSingleSource(G,s):
    S = []
    Q = G.graph 
    while len(Q) != 0:
        u = min(Q)
        S.append(u)
        for v in u.adjacency:
            relax(G,u,v)                     
####################################################################################            
graphList = []
graph = Graph(g = graphList)
vertexList = []

graphList = []
graph = Graph(g = graphList,e = [])
vertexList = []

vertexList.append(vertex_example.Vertex(c=vertex_example.VertexColor.WHITE, d1=1, d2='s'))
vertexList.append(vertex_example.Vertex(c=vertex_example.VertexColor.WHITE, d1=2, d2='t'))
vertexList.append(vertex_example.Vertex(c=vertex_example.VertexColor.WHITE, d1=3, d2='x'))
vertexList.append(vertex_example.Vertex(c=vertex_example.VertexColor.WHITE, d1=4, d2='y'))
vertexList.append(vertex_example.Vertex(c=vertex_example.VertexColor.WHITE, d1=5, d2='z')) 

for v in vertexList:
    graph.addVertexToGraph(v)

graph.addVertexAdjacent(0,vertexList[1])
edge1 = vertex_example.Edge(vertexList[0],vertexList[1],10)
graph.edges.append(edge1)
graph.addVertexAdjacent(0,vertexList[3])
edge2 = vertex_example.Edge(vertexList[0],vertexList[3],5)
graph.edges.append(edge2)

graph.addVertexAdjacent(1,vertexList[2])
edge3 = vertex_example.Edge(vertexList[1],vertexList[2],1)
graph.edges.append(edge3)
graph.addVertexAdjacent(1,vertexList[3])
edge4 = vertex_example.Edge(vertexList[1],vertexList[3],2)
graph.edges.append(edge4)

graph.addVertexAdjacent(2,vertexList[4])
edge5 = vertex_example.Edge(vertexList[2],vertexList[4],4)
graph.edges.append(edge5)

graph.addVertexAdjacent(3,vertexList[0])
edge6 = vertex_example.Edge(vertexList[3],vertexList[0],3)
graph.edges.append(edge6)
graph.addVertexAdjacent(3,vertexList[2])
edge7 = vertex_example.Edge(vertexList[3],vertexList[2],9)
graph.edges.append(edge7)
graph.addVertexAdjacent(3,vertexList[4])
edge8 = vertex_example.Edge(vertexList[3],vertexList[4],2)
graph.edges.append(edge8)

graph.addVertexAdjacent(4,vertexList[2])
edge9 = vertex_example.Edge(vertexList[4],vertexList[2],6)
graph.edges.append(edge9)
graph.addVertexAdjacent(4,vertexList[0])
edge10 = vertex_example.Edge(vertexList[4],vertexList[0],7)
graph.edges.append(edge10)

graph.printEdges()





             