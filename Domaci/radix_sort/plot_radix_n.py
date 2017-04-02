import time
import numpy as np
import matplotlib.pyplot as plt
import radix_n

def CreatePlot(input_data, exec_time, algo_name):
    fig = plt.figure()     
    fig.suptitle(algo_name, fontsize=14, fontweight='bold')    
 
    ax = fig.add_subplot(111)
    fig.subplots_adjust(top=0.85)       
    ax.set_title('Vreme izvrsenja')
    ax.set_xlabel('Ulaz [n]')    
    ax.set_ylabel('Vreme [ms]')

    ax.plot(input_data, exec_time, '-', color='green')
    
    print(algo_name)
    for i in range(0, len(input_data)):
        print("input_data: ", input_data[i], ", exec_time: ", exec_time[i])

    return fig
    
def ShowPlot():
    plt.show()    
   
def FirstPlot():
    algo_name = "Radix sort n = 3"
    input_data = []
    exec_time = []
    Arr = []
    for n in range(100,1000,100):
       Arr = range(n,100,-1)
       start_time = time.clock() 
       radix_n.radixSort(Arr,3)
       end_time = time.clock()
       exec_time.append((end_time - start_time)*1000)
       input_data.append(n)
       
    CreatePlot(input_data,exec_time,algo_name)
    
def SecondPlot():
    # Measure exeuction time
    algo_name = "Radix sort n = 4"
    input_data = []
    exec_time = []
    Arr = []
    for n in range(1000,10000,1000):
       Arr = range(n,1000,-1)
       start_time = time.clock() 
       radix_n.radixSort(Arr,4)
       end_time = time.clock()
       exec_time.append((end_time - start_time)*1000)
       input_data.append(n)
       
    CreatePlot(input_data,exec_time,algo_name)    
    
   
    
             
# Profile functions and create plots

FirstPlot()
SecondPlot()

# Show plots
ShowPlot()