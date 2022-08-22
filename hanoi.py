#!/usr/bin/env python3

'''
hanoi.py 
  script to solve the tower of Hanoi problem
'''


def moveDisk(A,B) :
    '''
    Simple moveDisk routine.
    '''
    print("Move disk from {} to {}".format(A,B))


def solveHanoi(n,f,h,t) :
    '''
    Solve the problem - Recursively
    '''
    if n > 0:
        solveHanoi(n-1, f, t, h)
        moveDisk(f,t)
        solveHanoi(n-1, h, f, t)
    else: 
        pass

if __name__ == "__main__" :
#    moveDisk("R","K")
    solveHanoi(3,"Source", "Helper", "Destination")


