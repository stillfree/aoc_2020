#!/usr/bin/env python3
import sys, time, math

def readInput():
    if( len( sys.argv ) == 2 ):
        file = open( sys.argv[1] , "r")
    else:
        file = open("input", "r")
    lines = file.readlines()
    return lines

def getRow( string ):
    string = string.replace('B','1')
    string = string.replace('F','0')
    return int( string, 2 )

def getColumn( string ):
    string = string.replace('R','1')
    string = string.replace('L','0')
    return int( string, 2 )

def partOne( lines ):
    seatIDs = []
    for line in lines:
        line =line.replace("\n","")
        rowStr = line[:7]
        columnStr = line[7:]
        row = getRow( rowStr )
        column = getColumn( columnStr )
        seatID = row * 8 + column
        seatIDs.append( seatID )
    print("PartOne: ", max( seatIDs ) )
    pass

def partTwo( lines ):
    array = []
    for i in range( 128 ):
        liste = []
        for j in range( 8 ):
            liste.append( 0 )
        array.append( liste )
    for line in lines:
        line =line.replace("\n","")
        rowStr = line[:7]
        columnStr = line[7:]
        row = getRow( rowStr )
        column = getColumn( columnStr )
        array[row][column] = 1

    for i in range( 12, 110 ):
        for j in range( 7 ):
            if( array[i][j] == 0 ):
                print("PartTwo: ", i*8+ j )

def main():
    lines = readInput()
    partOne( lines )
    partTwo( lines )


if __name__ == "__main__":
    main()
