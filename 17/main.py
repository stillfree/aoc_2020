#!/usr/bin/env python3
import sys, time, math

def readInput():
    if( len( sys.argv ) == 2 ):
        file = open( sys.argv[1] , "r")
    else:
        file = open("input2", "r")
    lines = file.readlines()
    return lines

def getAllNeighbors( vector ):
    vectorList = []
    for x in [ -1, 0, 1 ]:
        for y in [ -1, 0, 1 ]:
            for z in [ -1, 0, 1 ]:
                #vectorList.append( [vector[0] + x, vector[1] + y, vector[2] + z] )
                for w in [ -1, 0, 1 ]:
                    vectorList.append( [vector[0] + x, vector[1] + y, vector[2] + z, vector[3] + w] )
    #vectorList.remove( [vector[0], vector[1], vector[2]] )
    vectorList.remove( [vector[0], vector[1], vector[2], vector[3]] )
    return vectorList

def partOne( lines ):
    x = 0
    currentList = []
    for line in lines:
        y = 0
        for letter in line.strip():
            if( letter == "#" ):
                currentList.append( [x, y, 0, 0] )
            y += 1
        x += 1
    for i in range(6):
        numList = [[],[],[],[]]
        for vec in currentList:
            neigh = getAllNeighbors( vec )
            for nei in neigh:
                if nei not in numList[3] and nei in numList[2]:
                    numList[3].append( nei )
                else:
                    if nei not in numList[2] and nei in numList[1]:
                        numList[2].append( nei )
                    else:
                        if nei not in numList[1] and nei in numList[0]:
                            numList[1].append( nei )
                        else:
                            numList[0].append( nei )
        newList = []
        for vec in numList[1]:
            if vec in numList[2] and vec not in numList[3]:
                newList.append( vec )
            elif vec in currentList and vec not in numList[3]:
                newList.append( vec )
        currentList = list( newList )
        print(len(currentList))

def partTwo( lines ):
    pass

def main():
    lines = readInput()
    print(lines)
    partOne( lines )
    partTwo( lines )


if __name__ == "__main__":
    main()
