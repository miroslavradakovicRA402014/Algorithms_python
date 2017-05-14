import vertex_example
import random
time = 0

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
                   
def DFS(G):
    for u in G.graph:
        u.color = vertex_example.VertexColor.WHITE
        u.preview = None
    global time
    time = 0
    for u in G.graph:
        if u.color == vertex_example.VertexColor.WHITE:
            DFSvisit(G,u)
def DFSvisit(G,u):
    global time 
    time += 1
    u.data1 = time
    u.color = vertex_example.VertexColor.GRAY
    for v in u.adjacency:
        if v.color == vertex_example.VertexColor.WHITE:
            v.preview = u
            DFSvisit(G,v)
    u.color = vertex_example.VertexColor.BLACK
    time += 1
    u.data2 = time  
    
def printTime(G):
    for v in G.graph:
       print ("Start time  ",v.data1)
       print ("Finish time ",v.data2)        
        
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
                                                                                                  
########################################################################################
    