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
    print(lines)
    i = 0
    availableNumbers = {}
    indexX = lines.index( "your ticket:\n")
    indexY = lines.index( "nearby tickets:\n")
    restrictions = lines[:indexX-1]
    myticket = lines[indexX+1: indexX+2][0].strip()
    otherTickets = lines[indexY+1:]
    print( restrictions, myticket )
    for res in restrictions:
        res = res.strip().split( " " )
        print( res )
        for e in res:
            if( "-" in e ):
                e = e.split("-")
                for i in range( int(e[0]), int(e[1]) +1 ):
                    availableNumbers[str(i)] = 1
    counter = 0
    for other in otherTickets:
        elements = other.strip().split(",")
        for ele in elements:
            if( ele in availableNumbers.keys() ):
                pass
            else:
                print( "NOT", ele )
                counter += int(ele)
    print( counter )

def partTwo( lines ):
    pass

def main():
    lines = readInput()
    partOne( lines )
    partTwo( lines )


if __name__ == "__main__":
    main()
