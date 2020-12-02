#!/usr/bin/env python3
import sys, time, math

def readInput():
    file = 0
    if( len( sys.argv ) == 2 ):
        file = open( sys.argv[1], "r")
    else:
        file = open("input", "r")
    lines = file.readlines()
    return lines

def partOne( lines ):
    counter = 0
    for line in lines:
        line = line.split( ' ' )
        rangeIndex = line[0].split( '-' )
        number = line[2].count( line[1].split( ':' )[0] )
        print( rangeIndex, number )
        if( number >= int( rangeIndex[0] ) and number <= int( rangeIndex[1] ) ):
            counter += 1
    print( counter )

def partTwo( lines ):
    counter = 0
    for line in lines:
        line = line.split( ' ' )
        rangeIndex = line[0].split( '-' )
        character = line[1].split( ':' )[0]
        high = int( rangeIndex[1] )
        low = int( rangeIndex[0] )
        print( rangeIndex, line[2])
        if( ( line[2][ low - 1 ] == character ) != ( line[2][ high - 1 ] ==  character ) ):
            counter += 1
    print( " PartTwo:", counter )

def main():
    lines = readInput()
    partOne( lines )
    partTwo( lines )


if __name__ == "__main__":
    main()
