#!/usr/bin/env python3
'''
hanoi.py 
  script to solve the tower of Hanoi problem
'''

import argparse
import sys

parser = argparse.ArgumentParser()


parser.add_argument('-n', '--number',
        help='Number of disks to move',
        default=3,
        type=int
        )

parser.add_argument("-u", "--usage",
        action="store_true",
        help='print usage message'
        )

args = parser.parse_args()
n = args.number

if args.usage:
    print('''
    This is a towers of Hanoi program. 
    It show how to move disks between towers so 
    that smaller disks are always on top of 
    bigger disks. 
    ''')
    sys.exit(1)

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


