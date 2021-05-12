#!/usr/bin/env python3
import sys, time, math, re, itertools
from collections import deque

def readInput():
    if( len( sys.argv ) == 2 ):
        file = open( sys.argv[1] , "r")
    else:
        file = open("input", "r")
    lines = file.readlines()
    return lines

def partOne( lines ):
    i = 0
    availableNumbers = {}
    indexX = lines.index( "your ticket:\n")
    indexY = lines.index( "nearby tickets:\n")
    restrictions = lines[:indexX-1]
    myticket = lines[indexX+1: indexX+2][0].strip()
    otherTickets = lines[indexY+1:]
    for res in restrictions:
        res = res.strip().split( " " )
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
                counter += int(ele)
    print( counter )

def fits( A, B ):
    for i in range( len( A ) ):
        numb = A[i]
        rest = B[i]
        if( not (( numb <= rest[2] and numb >= rest[1] )
            or ( numb >= rest[3] and numb <= rest[4] ) )):
            return False
    return True

options = []
myticket = []
def recurs( index, available, current, optionlist ):
    global myticket
    global options
    if( index == len(optionlist ) ):
        if( fits( myticket, current ) ):
            options.append( current )
    else:
        for option in optionlist[index]:
            if( option in available ):
                temp = list( available )
                temp.remove( option )
                recurs( index + 1, temp, current + [option ], optionlist )

def combine( myticket, restrictions ):
    global options
    optionlist = []
    for numb in myticket:
        appendList = []
        for rest in restrictions:
            if( (( numb <= rest[2] and numb >= rest[1] )
                or ( numb >= rest[3] and numb <= rest[4] ) )):
                appendList.append( rest )
        optionlist.append( appendList )
    recurs( 0, restrictions, [], optionlist )

def getRestriction( lines ):
    rawlines = lines[:lines.index( "your ticket:\n")-1]
    restrictions = []
    for line in rawlines:
        name = line[:line.index(":")]
        restrictions.append( [ name ]+ [ int( t )  for t in re.split("-|\s", line) if re.sub("[^0-9]", "", t ) ] )
    return restrictions

def partTwo( lines ):
    global options
    global myticket
    otherTickets = list( map( lambda x: list( map(int, x.split(",") ) ), lines[lines.index( "nearby tickets:\n")+1:] ) )
    myticket =  list(map(int, lines[lines.index( "your ticket:\n") + 1].strip().split(",") ))
    restrictions = getRestriction( lines )
    print( "Create combination" )
    combine( myticket, restrictions )
    print( "Created combination" )
    otherTickets.append( myticket )
    for ticket in otherTickets:
        removeList = []
        for option in options:
            if( not fits( ticket, option ) ):
                removeList.append( option )
                break
        for rem in removeList:
            options.remove( rem )
    print("left:", options)

    indexs = []
    for opt in options[0]:
        if( "departure" in opt[0] ):
            indexs.append( options.index( opt ) )

    sum = 1
    for ind in indexs:
        sum *= myticket[ind]
    print( sum )


def main():
    lines = readInput()
    partOne( lines )
    partTwo( lines )



if __name__ == "__main__":
    main()
