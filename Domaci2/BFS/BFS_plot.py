import time
import numpy as np
import matplotlib.pyplot as plt
import BFS
import random

def CreatePlot(input_data, exec_time, algo_name):
    fig = plt.figure()     
    fig.suptitle(algo_name, fontsize=14, fontweight='bold')    
 
    ax = fig.add_subplot(111)
    fig.subplots_adjust(top=0.85)       
    ax.set_title('Vreme izvrsenja')
    ax.set_xlabel('Ulaz [V]')    
    ax.set_ylabel('Vreme [ms]')

    ax.plot(input_data, exec_time, '-', color='green')
    
    print(algo_name)
    for i in range(0, len(input_data)):
        print("input_data: ", input_data[i], ", exec_time: ", exec_time[i])

    return fig
    
def ShowPlot():
    plt.show()    
   
def FirstPlot():
    algo_name = "BFS search"
    input_data = []
    exec_time = []
    for n in range(100,1100,100):
       graphList = []
       graph = BFS.Graph(g = graphList)   
       vertexList = []
       BFS.createGraph(graph,vertexList,n)
       vertexNum = random.randint(0,n-1) 
       start_time = time.clock()
       BFS.BFS(graph,vertexList[vertexNum])
       end_time = time.clock()
       exec_time.append((end_time - start_time)*1000)
       input_data.append(n)
       
    CreatePlot(input_data,exec_time,algo_name)
    
             
# Profile functions and create plots

FirstPlot()

# Show plots
ShowPlot()  