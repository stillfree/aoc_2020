#!/usr/bin/env python3
import sys, time, math

def readInput():
    if( len( sys.argv ) == 2 ):
        file = open( sys.argv[1] , "r")
    else:
        file = open("input", "r")
    lines = file.readlines()
    return lines

class element():
    def __init__( self, color ):
        self._color = color
        self._children = []
        self._parents = []

elementList = {}
def partOne( lines ):
    global elementList
    for line in lines:
        color = " ".join( line.split(" ")[:2])
        elementList[ color ] = element( color )

    for line in lines:
        line = line.split("contain")
        color = " ".join(line[0].split( " " )[:2] )
        if( not "no other bags." in line[1] ):
            receipt = line[1].replace('.', '')
            temp = [ receipt ]
            if( "," in line[1]):
                temp = receipt.split(',')
            for e in temp:
                e = e.split(" ")[1:]
                childNumber = e[0]
                childColor = " ".join( e[1:3] )
                elementList[ color ]._children.append( [ elementList[ childColor ], childNumber ])
                if( elementList[ color ] not in elementList[ childColor ]._parents ):
                    elementList[ childColor ]._parents.append( elementList[ color ] )
    overallParents = []
    currentElement = elementList[ "shiny gold" ]
    parents = currentElement._parents
    overallParents += parents
    current = 0
    if( len( parents ) ):
        current = parents.pop()
    while( current ):
        for parente in current._parents:
            if( parente not in overallParents ):
                overallParents.append( parente )
            if( parente not in parents ):
                parents.append( parente )
        current = 0
        if( len( parents ) ):
            current = parents.pop()
    print( "PartOne: ", len( overallParents ) )

def recursive( element ):
    if( len( element._children ) <= 0 ):
        return [ 1, False ]
    summe = 0
    for child in element._children:
        number = int( child[1] )
        result = recursive( child[0] )
        save = result
        temp = number
        if( result[1] == False ):
            summe += number
        else:
            summe += number
            summe += ( number * result[0])
    return [ summe, True ]

def partTwo( lines ):
    global elementList
    print( "PartTwo: ", recursive( elementList[ "shiny gold" ] )[0] )

def main():
    lines = readInput()
    partOne( lines )
    partTwo( lines )

if __name__ == "__main__":
    main()
