
import math
import numpy as np
from copy import deepcopy

size=int(input())
ss=math.sqrt(size)
def inp():
    
    return [int(x) for x in input().split()]
def getSquare(i,j):
    return ss*math.floor(i/ss)+ math.floor(j/ss)

square=dict()
row=dict()
col=dict()

given=[]
zero=0

for i in range(size):
    square[i]=[]
    row[i]=[]
    col[i]=[]
    
for i in range(size):
    arr=inp()
    given.append(arr)
    for j in range (size):
        if arr[j]!=0:
            
            square[abs(getSquare(i,j))].append(arr[j])
            row[i].append(arr[j])
            col[j].append(arr[j])
        else:
            zero+=1
        
            

def solver(given,square,row,col,zero):
    if zero==0:
        print('\n\n==>>\n\n')
        print(given)
        return
    for i in range(size):
        for j in range(size):
            if given[i][j]==0:
                for k in range(size):
                    if i==0 and j == 0:
                        
                        print(k+1)
                    
                    if k+1 not in square[getSquare(i,j)] and k+1 not in row[i] and k+1 not in col[j]:
                        
                        sgiven=deepcopy(given)
                        sgiven[i][j]=k+1
                        srow=deepcopy(row)
                        scol=deepcopy(col)
                        srow[i].append(k+1)
                        scol[j].append(k+1)
                        ssquare=deepcopy(square)
                        ssquare[getSquare(i,j)].append(k+1)
                        
                        solver(sgiven,ssquare,srow,scol,zero-1)
                        
    
solver(given,square,row,col,zero)

