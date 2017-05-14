import vertex_example
import random

class Graph:

    def __init__(self,g = None,s = 0):
        self.graph = g
        self.size = s
    def addVertexToGraph(self,vertex):
        self.graph.append(vertex)
        self.size += 1      
    def addVertexAdjacent(self,vertexNum,vertex):
        (self.graph[vertexNum]).adjacency.append(vertex)
    def printAdjacency(self,vertexNum):
        print ("Vertex",(self.graph[vertexNum]).data1+1,"adjacency ")
        for v in (self.graph[vertexNum]).adjacency:
            v.printAdjacent()
    def printGraphsVertexes(self):
        num = 0
        for v in self.graph:
            print ("==========================================")         
            print ("Vertex num",v.data1+1)
            print ("Vertex value",v.data2)
            if v.color == vertex_example.VertexColor.WHITE:
              print ("WHITE")
            elif v.color == vertex_example.VertexColor.GRAY:
              print ("GRAY")
            else:
              print ("BLACK")  
            self.printAdjacency(num)        
            num += 1  
            
class QueueList:
    
    def __init__(self,q = None,s = 0):
        self.vertexQueue = q
        self.size = s   
    def enqueue(self,vertex):
        self.vertexQueue.insert(0,vertex)
        self.size += 1
    def dequeue(self):
        self.size -= 1
        return self.vertexQueue.pop()
    def isEmpty(self):
        if self.size == 0:
           return True
        else:
           return False       
    def printQueue(self):
        print ("Vertex queue")
        for v in self.vertexQueue:
            print ("==========================================")         
            print ("Vertex num",v.data1)
            print ("Vertex value",v.data2)
            if v.color == vertex_example.VertexColor.WHITE:
              print ("WHITE")
            elif v.color == vertex_example.VertexColor.GRAY:
              print ("GRAY")
            else:
              print ("BLACK")  
           
def BFS(G,s):
    for u in G.graph:
      if u.data1 != s.data1:
         u.color = vertex_example.VertexColor.WHITE
         u.data2 = 500000000
         u.preview = None
    s.color = vertex_example.VertexColor.GRAY
    s.data2 = 0
    s.preview = None
    queueList = []
    queueV = QueueList(q = queueList)
    queueV.enqueue(s)
    while not queueV.isEmpty():
        u = queueV.dequeue()
        for v in u.adjacency:
            if v.color == vertex_example.VertexColor.WHITE:
                v.color = vertex_example.VertexColor.GRAY
                v.data2 = u.data2 + 1
                v.preview = u
                queueV.enqueue(v)
        u.color = vertex_example.VertexColor.BLACK
        
def printPath(G,s,v):
    if v == s:
       print ("==========================================")         
       print ("Vertex value",v.data2)
       if v.color == vertex_example.VertexColor.WHITE:
          print ("WHITE")
       elif v.color == vertex_example.VertexColor.GRAY:
          print ("GRAY")
       else:
          print ("BLACK")  
    elif v.preview == None:
       print ("Path don't exist")
    else:
       printPath(G,s,v.preview)           
 
def printDistance(G):
    for v in G.graph:
        print ("Distance  to ",v.data1+1,"is",v.data2)  


def createGraph(G,vList,vertexNum):    
    for i in range(0,vertexNum):
        vList.append(vertex_example.Vertex(c=vertex_example.VertexColor.WHITE, d2=0, d1=i))
    for v in vList:
        G.addVertexToGraph(v) 
    for v in G.graph:
        adjNum = random.randint(1,4)
        for i in range(0,adjNum):
            adjV = random.randint(0,vertexNum-1)
            if adjV != v.data1 and (not vList[adjV] in v.adjacency):
                G.addVertexAdjacent(v.data1,vList[adjV])       
                G.addVertexAdjacent(adjV,v)                                                                                                                 
########################################################################################
'''
graphList = []
graph = Graph(g = graphList)
vertexList = []

createGraph(graph,vertexList,5)

queueList = []
queueV = QueueList(q = queueList)
     
graph.printGraphsVertexes()

BFS(graph,vertexList[2])
printDistance(graph)
#printPath(graph,vertexList[2],vertexList[4])
'''
    