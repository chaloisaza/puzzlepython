# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 19:26:28 2018

@author: chaloisaza
"""

import random
import numpy

 # return an int, one of 1,2,3,4,5,6

def createInitialParams(n,m):
    list = []
    while True:
        r = random.randrange(0,9)      
        if r not in list: 
            list.append(r)
        
        if len(list) == 9:
            x = reshape(list,(n,m))
            return(x)
            break
        
def createSolution(n,m):

    solution = []
    solution.extend(range(1, (n*m)+1))
    solution = reshape(solution,(n,m))
    return solution

def casePosition(n,m):
    print(n,m)
    
 
def main():
  estado_inicial =  createInitialParams(3,3)
  print (estado_inicial)
  #solucion = createSolution(3,3)
  solucion = [1 ,2 ,3,4 ,5 ,6,7, 8, 0]
  #print (reshape(solucion,(3,3)))
  i,j = numpy.where(estado_inicial==0)
  casePosition(i,j)
  
  print(i,j)

if __name__ == '__main__':
    main()