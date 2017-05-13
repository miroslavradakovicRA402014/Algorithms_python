import vertex_example

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

########################################################################################       
def DFS(G):
    for u in G.graph:
        u.color = vertex_example.VertexColor.WHITE
        u.preview = None
    time = 0
    for u in G.graph:
        if u.color == vertex_example.VertexColor.WHITE:
            DFSvisit(G,u,time)
def DFSvisit(G,u,time):
    time += 1
    u.data1 = time
    u.color = vertex_example.VertexColor.GRAY
    for v in u.adjacency:
        if v.color == vertex_example.VertexColor.WHITE:
            v.preview = u
            DFSvisit(G,v,time)
    u.color = vertex_example.VertexColor.BLACK
    time += 1
    u.data2 = time  
    
def printTime(G):
    for v in G.graph:
       print ("Start time  ",v.data1)
       print ("Finish time ",v.data2)               
                                                                                                  
########################################################################################
graphList = []
graph = Graph(g = graphList)
vertexList = []
########################################################################################
'''
vertexList.append(vertex_example.Vertex(c=vertex_example.VertexColor.WHITE, d1=1, d2=22))
vertexList.append(vertex_example.Vertex(c=vertex_example.VertexColor.WHITE, d1=2, d2=45))
vertexList.append(vertex_example.Vertex(c=vertex_example.VertexColor.WHITE, d1=3, d2=12))
vertexList.append(vertex_example.Vertex(c=vertex_example.VertexColor.WHITE, d1=4, d2=52))
vertexList.append(vertex_example.Vertex(c=vertex_example.VertexColor.WHITE, d1=5, d2=72))        

for v in vertexList:
    graph.addVertexToGraph(v)
   
graph.addVertexAdjacent(0,vertexList[1])
graph.addVertexAdjacent(0,vertexList[4])

graph.addVertexAdjacent(1,vertexList[0])
graph.addVertexAdjacent(1,vertexList[4])
graph.addVertexAdjacent(1,vertexList[2])
graph.addVertexAdjacent(1,vertexList[3])

graph.addVertexAdjacent(2,vertexList[1])
graph.addVertexAdjacent(2,vertexList[3])

graph.addVertexAdjacent(3,vertexList[1])
graph.addVertexAdjacent(3,vertexList[4])
graph.addVertexAdjacent(3,vertexList[2])

graph.addVertexAdjacent(4,vertexList[3])
graph.addVertexAdjacent(4,vertexList[0])
graph.addVertexAdjacent(4,vertexList[1])

print ("Undirected graph")
graph.printGraphsVertexes()

########################################################################################

graphList = []
graph = Graph(g = graphList)
vertexList = []

vertexList.append(vertex_example.Vertex(c=vertex_example.VertexColor.WHITE, d1=1, d2=22))
vertexList.append(vertex_example.Vertex(c=vertex_example.VertexColor.WHITE, d1=2, d2=45))
vertexList.append(vertex_example.Vertex(c=vertex_example.VertexColor.WHITE, d1=3, d2=12))
vertexList.append(vertex_example.Vertex(c=vertex_example.VertexColor.WHITE, d1=4, d2=52))
vertexList.append(vertex_example.Vertex(c=vertex_example.VertexColor.WHITE, d1=5, d2=72)) 
vertexList.append(vertex_example.Vertex(c=vertex_example.VertexColor.WHITE, d1=6, d2=28))

for v in vertexList:
    graph.addVertexToGraph(v)

graph.addVertexAdjacent(0,vertexList[1])
graph.addVertexAdjacent(0,vertexList[3])

graph.addVertexAdjacent(1,vertexList[4])

graph.addVertexAdjacent(2,vertexList[5])
graph.addVertexAdjacent(2,vertexList[4])

graph.addVertexAdjacent(3,vertexList[1])

graph.addVertexAdjacent(4,vertexList[3])

graph.addVertexAdjacent(5,vertexList[5])
'''
'''
print ("Directed graph")
graph.printGraphsVertexes()
'''
########################################################################################
'''
queueList = []
queueV = QueueList(q = queueList)

queueV.enqueue(vertexList[0])
queueV.enqueue(vertexList[1])
queueV.printQueue()
queueV.dequeue()
queueV.printQueue()
'''

'''
vertexList.append(vertex_example.Vertex(c=vertex_example.VertexColor.WHITE, d2=0, d1='v'))
vertexList.append(vertex_example.Vertex(c=vertex_example.VertexColor.WHITE, d2=1, d1='r'))
vertexList.append(vertex_example.Vertex(c=vertex_example.VertexColor.WHITE, d2=2, d1='s'))
vertexList.append(vertex_example.Vertex(c=vertex_example.VertexColor.WHITE, d2=3, d1='w'))
vertexList.append(vertex_example.Vertex(c=vertex_example.VertexColor.WHITE, d2=4, d1='t')) 
vertexList.append(vertex_example.Vertex(c=vertex_example.VertexColor.WHITE, d2=5, d1='x'))
vertexList.append(vertex_example.Vertex(c=vertex_example.VertexColor.WHITE, d2=6, d1='u'))
vertexList.append(vertex_example.Vertex(c=vertex_example.VertexColor.WHITE, d2=7, d1='y'))

for v in vertexList:
    graph.addVertexToGraph(v)
    
graph.addVertexAdjacent(0,vertexList[1])

graph.addVertexAdjacent(1,vertexList[0])
graph.addVertexAdjacent(1,vertexList[2])

graph.addVertexAdjacent(2,vertexList[1])
graph.addVertexAdjacent(2,vertexList[3])

graph.addVertexAdjacent(3,vertexList[2])
graph.addVertexAdjacent(3,vertexList[4])
graph.addVertexAdjacent(3,vertexList[5])

graph.addVertexAdjacent(4,vertexList[3])
graph.addVertexAdjacent(4,vertexList[5])
graph.addVertexAdjacent(4,vertexList[6])

graph.addVertexAdjacent(5,vertexList[3])
graph.addVertexAdjacent(5,vertexList[4])
graph.addVertexAdjacent(5,vertexList[6])   
graph.addVertexAdjacent(5,vertexList[7])

graph.addVertexAdjacent(6,vertexList[4])
graph.addVertexAdjacent(6,vertexList[5])
graph.addVertexAdjacent(6,vertexList[7])

graph.addVertexAdjacent(7,vertexList[5])
graph.addVertexAdjacent(7,vertexList[6])   

#graph.printGraphsVertexes()

BFS(graph,vertexList[2])
printPath(graph,vertexList[2],vertexList[4])
'''

vertexList.append(vertex_example.Vertex(c=vertex_example.VertexColor.WHITE, d2=0, d1='x'))
vertexList.append(vertex_example.Vertex(c=vertex_example.VertexColor.WHITE, d2=1, d1='u'))
vertexList.append(vertex_example.Vertex(c=vertex_example.VertexColor.WHITE, d2=2, d1='v'))
vertexList.append(vertex_example.Vertex(c=vertex_example.VertexColor.WHITE, d2=3, d1='y'))
vertexList.append(vertex_example.Vertex(c=vertex_example.VertexColor.WHITE, d2=4, d1='w')) 
vertexList.append(vertex_example.Vertex(c=vertex_example.VertexColor.WHITE, d2=5, d1='z'))

for v in vertexList:
    graph.addVertexToGraph(v)
    
graph.addVertexAdjacent(0,vertexList[2])

graph.addVertexAdjacent(1,vertexList[0])
graph.addVertexAdjacent(1,vertexList[2])

graph.addVertexAdjacent(2,vertexList[3])

graph.addVertexAdjacent(3,vertexList[0])

graph.addVertexAdjacent(4,vertexList[3])
graph.addVertexAdjacent(4,vertexList[5])

graph.addVertexAdjacent(5,vertexList[5])

#graph.printGraphsVertexes()

DFS(graph)   
printTime(graph)

    