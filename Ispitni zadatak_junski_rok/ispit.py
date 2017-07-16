import vertex_example


class Edge:

   def __init__(self,v = None,w = 0):
        self.vertex = v
        self.weight = w
              
class Graph:

    def __init__(self,g = None,s = 0):
        self.graph = g
        self.size = s 
    def addVertexToGraph(self,vertex):    
        self.graph.append(vertex)
        self.size += 1
    def addVertexAdjacent(self,vertexNum,edge):
        (self.graph[vertexNum]).adjacency.append(edge)
    def printAdjacency(self,vertexNum):
        print("Vertex ",(self.graph[vertexNum]).data," adjacency")
        for e in (self.graph[vertexNum].adjacency):
            #(e.vertex).printAdjacent()
            print("Edge ",(self.graph[vertexNum]).data,"-",(e.vertex).data," weight ",e.weight)
    def printGraphsVertexes(self):
        num = 0
        for v in self.graph:
            print("================")
            print ("Vertex ",v.data)
            self.printAdjacency(num)
            num += 1
        print ("============")  
         
def makeGraph(G):
                 
    G.addVertexToGraph(vertexA)
    G.addVertexToGraph(vertexB)
    G.addVertexToGraph(vertexC)
    G.addVertexToGraph(vertexD)
    G.addVertexToGraph(vertexE)
    G.addVertexToGraph(vertexF)  
    G.addVertexToGraph(vertexG)
    
    edgeAC = Edge(vertexC,6)
    edgeAB = Edge(vertexB,8)
    
    G.addVertexAdjacent(0,edgeAC)
    G.addVertexAdjacent(0,edgeAB)
    
    edgeBD = Edge(vertexD,10)
    
    G.addVertexAdjacent(1,edgeBD)
    
    edgeCD = Edge(vertexD,15)
    edgeCE = Edge(vertexE,9)
      
    G.addVertexAdjacent(2,edgeCE)
    G.addVertexAdjacent(2,edgeCD)  
      
    edgeDE = Edge(vertexE,14)
    edgeDF = Edge(vertexF,4)
    
    G.addVertexAdjacent(3,edgeDE)
    G.addVertexAdjacent(3,edgeDF)
    
    edgeEF = Edge(vertexF,13)
    edgeEG = Edge(vertexG,17)
    
    G.addVertexAdjacent(4,edgeEF)
    G.addVertexAdjacent(4,edgeEG)
    
    edgeFG = Edge(vertexG,7)
    
    G.addVertexAdjacent(5,edgeFG)
    
    G.printGraphsVertexes()
    
def getOutDegrees(G):

    deg = []
    for v in G.graph:
        deg.append(len(v.adjacency))
    return deg
    
def getInDegrees(G):

    deg = []
    for v in G.graph:
        deg.append(0)
    for v in G.graph:
        for e in v.adjacency:
            if e.vertex.data == "a":
                deg[0] += 1
            elif e.vertex.data == "b":     
                deg[1] += 1
            elif e.vertex.data == "c":     
                deg[2] += 1
            elif e.vertex.data == "d":     
                deg[3] += 1        
            elif e.vertex.data == "e":     
                deg[4] += 1
            elif e.vertex.data == "f":     
                deg[5] += 1
            else :
                deg[6] += 1                                           
            
    return deg        
        
def updateEdge(G,vertexNumIn,vertexOut,w):

    for e in G.graph[vertexNumIn].adjacency:
        if e.vertex.data == vertexOut.data:
            e.weight = w
            return                 
    G.addVertexAdjacent(vertexNumIn,Edge(vertexOut,w))
    
    print ("Updated graph")
    G.printGraphsVertexes()  
    
 
def initializeSingleSource(G,s):

    for v in G.graph:
        if v.data == s.data:
            v.distance = 0
            v.prev = None
        else:
            v.distance = 5000000
            v.prev = None
    for v in G.graph:
        print (v.distance)        
            
def edgeWeight(G,u,v):

    for vr in G.graph:
        if vr.data == u.data:
            for e in vr.adjacency:
                if e.vertex.data == v.data:
                    return e.weight          
 
def relax(G,u,v):

    #print (v.distance,u.distance + edgeWeight(G,u,v))

    if v.distance > u.distance + edgeWeight(G,u,v):
        v.distance = u.distance + edgeWeight(G,u,v) 
        v.prev = u          
        #print (v.distance)
    #print (v.distance) 
    #print(edgeWeight(G,u,v))               
    
def bellmanFord(G,s):

    initializeSingleSource(G,s)
    for i in range(0,len(G.graph)-1):
        for v in G.graph:
            for e in v.adjacency:
                relax(G,v,e.vertex)
   

def shortestPath(G,s,d):

    bellmanFord(G,s)
     
    prevList = []
    prevList.append(d.data) 
    prev = d.prev
    while (prev != None):
        prevList.append(prev.data)
        prev = prev.prev
    
    return (d.distance,prevList)  
      
  
###########################################################################

graphList = []
graph = Graph(g = graphList)

vertexA = vertex_example.Vertex(d = "a")
vertexB = vertex_example.Vertex(d = "b")
vertexC = vertex_example.Vertex(d = "c")
vertexD = vertex_example.Vertex(d = "d")
vertexE = vertex_example.Vertex(d = "e")             
vertexF = vertex_example.Vertex(d = "f")  
vertexG = vertex_example.Vertex(d = "g")  

makeGraph(graph) 

outList = getOutDegrees(graph)
inList = getInDegrees(graph)

print ("Vertex a out degree ",outList[0])
print ("Vertex b out degree ",outList[1])
print ("Vertex c out degree ",outList[2])
print ("Vertex d out degree ",outList[3])
print ("Vertex e out degree ",outList[4])
print ("Vertex f out degree ",outList[5])
print ("Vertex g out degree ",outList[6])

print ("=================================")

print ("Vertex a in degree ",inList[0])
print ("Vertex b in degree ",inList[1])
print ("Vertex c in degree ",inList[2])
print ("Vertex d in degree ",inList[3])
print ("Vertex e in degree ",inList[4])
print ("Vertex f in degree ",inList[5])
print ("Vertex g in degree ",inList[6])

print ("=================================")
   
updateEdge(graph,1,vertexC,-4)

print ("=================================")

retTup = ()
retTup = shortestPath(graph,vertexA,vertexG)

print ("Shortest path betwen a and g is",retTup[0])
print ("Shortest path ",retTup[1])

