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
    algo_name = "LCS"
    input_data = []
    exec_time = []
    S = []
    T = []
    for n in range(1,20,2):
       len1 = random.randint(1,n)
       len2 = random.randint(1,n)
       #len1 = n
       #len2 = n
       for i in range(0,len1):
            S.append(random.randint(1,28))
       for i in range(0,len2):
            T.append(random.randint(1,28))
       
       start_time = time.clock()
       LCS(S,len1-1,T,len2-1)  
       end_time = time.clock()
       exec_time.append((end_time - start_time)*1000)
       input_data.append(n)
       
    CreatePlot(input_data,exec_time,algo_name)

def maxVal(a,b):
    if a > b:
       return a
    else:
       return b

def LCS(S,n,T,m):
    if n == -1 or m == -1:
        return 0
    if S[n] == T[m]:
        return 1 + LCS(S,n-1,T,m-1)
    else:
        return maxVal(LCS(S,n-1,T,m),LCS(S,n,T,m-1)) 
        
def LCSLength(X,Y):
    m = len(X)-1
    n = len(Y)-1
    b = []
    c = []

    b = [[1 for x in range(m+1)] for y in range(n+1)]         
    c = [[0 for x in range(m+1)] for y in range(n+1)] 
    
    for i in range(1,m+1):
        c[i][0] = 0
    for j in range(0,n+1):
        c[0][j] = 0
            
    for i in range(1,m+1):           
        for j in range(1,n+1):
            if X[i] == Y[j]:
                c[i][j] = c[i-1][j-1]
                b[i,j] = 2
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = 0
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = 1
    retVal = (c,b)
    return retVal
    
def 

                            
        
#S = ['A','B','C','B','D','A','B']
#T = ['B','C','A','B','A']

#seq = LCS(S,len(S)-1,T,len(T)-1) 
#print (seq)

X = ['0','A','B','C','B','D','A','B']
Y = ['0','B','C','A','B','A']

tup = LCSLength(X,Y) 
print (tup[0])
print (tup[1])


#FirstPlot()          
#ShowPlot()