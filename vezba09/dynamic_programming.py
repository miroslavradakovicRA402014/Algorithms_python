import time
import numpy as np
import matplotlib.pyplot as plt
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
    algo_name = "Cut rod search bottom up extended"
    input_data = []
    exec_time = []
    p = []
    for n in range(100,1100,100):
       p = range(0,n+1) 
       start_time = time.clock()
       #cutRod(p,n)  
       #memoizedCutRod(p,n)  
       extendedBottomUp(p,n)   
       end_time = time.clock()
       exec_time.append((end_time - start_time)*1000)
       input_data.append(n)
       
    CreatePlot(input_data,exec_time,algo_name)

def SecondPlot():
    algo_name = "Cut rod search bottom up"
    input_data = []
    exec_time = []
    p = []
    for n in range(100,1100,100):
       p = range(0,n+1) 
       start_time = time.clock()
       #cutRod(p,n)  
       #memoizedCutRod(p,n) 
       bottomUpCutRod(p,n)    
       end_time = time.clock()
       exec_time.append((end_time - start_time)*1000)
       input_data.append(n)
       
    CreatePlot(input_data,exec_time,algo_name)



def maxVal(a,b):
    if a > b:
       return a
    else:
       return b

def cutRod(p,n):
    if n == 0:
       return 0
    q = -50000
    for i in range(0,n):
        q = maxVal(q,p[i] + cutRod(p,n - i -1))
    return q   

def memoizedCutRod(p,n):
    r = []
    for i in range(0,n+1):
       r.append(-50000)
    return memoizedCutRodAux(p,n,r)  
    
def memoizedCutRodAux(p,n,r):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else: 
        q = -50000
        for i in range(1,n+1):
            q = maxVal(q,p[i] + memoizedCutRodAux(p,n-i-1,r))
    r[n] = q
    return q   
    

def bottomUpCutRod(p,n):
    r = []
    for i in range(0,n+1):
        r.append(0)
            
    for j in range(1,n+1):
        q = -50000
        for i in range(1,j):
            q = maxVal(q,p[i] + r[j-i])
        r[j] = q    
    return r[n] 
    
def extendedBottomUp(p,n):
    r = []
    s = []
    for i in range(0,n+1):
        r.append(0)                
        s.append(0)
    for j in range(1,n+1):
        q = -50000
        for i in range(1,j):
            if q < p[i] + r[j-i]:
                q = p[i] + r[j-i]
                s[j] = i
        r[j] = q
    retVal = (r,s)
    return retVal
    
def printRodCutSolution(p,n):
    tup = extendedBottomUp(p,n)
    r = tup[0]
    s = tup[1]
    while n > 0:
        print (s[n])
        n = n - s[n]
                
         
         
         
p = [1,5,8,9,10,17,17,20,24,30]
#retVal = cutRod(p,10)

#print (retVal)

    
             
# Profile functions and create plots

FirstPlot()
SecondPlot()

# Show plots
ShowPlot() 




    
