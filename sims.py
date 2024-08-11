# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 06:30:02 2024

@author: @JacobBe5
"""

import random
import time
import multiprocessing


def simulateIt(iterations):
    maxRes=0
    for i in range (iterations):
        tempRes=random.binomialvariate(n=231, p=0.25)
        if tempRes>maxRes:
            maxRes=tempRes
    return(maxRes)
    
    

if __name__ =="__main__":
    tStart=time.time()
    nRun = 20 # Number of processes to create
    nSims = 50000000 #Number of runs of 231 to run per process
    # How many simulations peranprocesses to run
    simulations = [nSims] * nRun 
    
    # pool the runs
    p=multiprocessing.Pool()
    
    #apply a map to the list of simulations
    result= p.map(simulateIt, simulations)
    
    print(result)
    
    tEnd=time.time()
    tTotal=tEnd-tStart
    
    print("Done in " + str(tTotal))

