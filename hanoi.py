#!/usr/bin/env python3
'''
hanoi.py 
  script to solve the tower of Hanoi problem
'''

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-n', '--number',
        dest='number',
        help='Number of disks to move',
        type=int
        )

args = parser.parse_args()
n = args.number

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
    solveHanoi(n,"S", "H", "D")


