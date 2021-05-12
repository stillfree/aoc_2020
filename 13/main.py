#!/usr/bin/env python3
import sys, time, math

def readInput():
    if( len( sys.argv ) == 2 ):
        file = open( sys.argv[1] , "r")
    else:
        file = open("input", "r")
    lines = file.readlines()
    return lines

def partOne( lines ):
    goal = int( lines[0] )
    buses = list( map( int, list(filter( lambda a: a != "x", lines[1].replace("\n","").split(",") ))) )
    minimum = [100, 100, 0]
    for bus in buses:
        multiplier = 1
        done = False
        while( not done ):
            result = bus * multiplier
            if( result == goal ):
                done = True
            elif( result > goal ):
                diff = result - goal
                if( diff < minimum[0] ):
                    minimum[0] = diff
                    minimum[1] = bus
                done = True
            multiplier += 1
    print( "PartOne:", minimum[0] * minimum[1] )


def partTwo( lines ):
    buses = lines[1].replace("\n","").split(",")
    busIDs = list( map( int, list(filter( lambda a: a != "x", lines[1].replace("\n","").split(",") ))) )
    busIDs.sort( reverse=True )
    busIDs = list( map( lambda x: str(x), busIDs ) )
    workArray = []
    for id in busIDs:
        workArray.append( [ int( id ) , buses.index(id) ] )
    done = False
    multiplier = 1#int( 100000000000000 / workArray[0][0])
    while( not done ):
        result = multiplier * workArray[0][0]
        cts = workArray[0][1]
        allTrue = True
        for i in range(1, len( workArray ) ):
            bus = workArray[i]
            if( (result + ( bus[1] - cts) % bus[0]) != 0 ):
                allTrue = False
                break
        if( allTrue ):
            print( "PartTwo:", str( result - cts ) )
            done = True
        multiplier += 1

def main():
    lines = readInput()
    partOne( lines )
    partTwo( lines )


if __name__ == "__main__":
    main()
