#!/usr/bin/env python3
import sys, time, math, copy
from collections import deque

def readInput():
    if( len( sys.argv ) == 2 ):
        file = open( sys.argv[1] , "r")
    else:
        file = open("input", "r")
    lines = file.readlines()
    return lines

def partOne( lines ):
    memory = []
    for line in lines:
        queue = deque()
        for char in line:
            if( char == '.' ):
                queue.append( 0 )
            elif( char == '#' ):
                queue.append( 1 )
        memory.append( queue )
    length = len( memory )
    mult = []
    for e in [[1,1], [3,1], [5,1], [7,1], [1,2]]:
        index = 0
        counter = 0
        copyMemory = copy.deepcopy( memory )
        while( index < length ):
            if( copyMemory[index][0] == 1 ):
                counter += 1
            for i in range( len( copyMemory ) ):
                copyMemory[i].rotate( -1*e[0] )
            index += e[1]
        mult.append( counter )
    print( "PartOne: ", mult[0] )
    print( mult )
    summe = 1
    for mul in mult:
        summe *= mul
    print( "PartTwo: ", summe )

def main():
    lines = readInput()
    print(lines)
    partOne( lines )

if __name__ == "__main__":
    main()
