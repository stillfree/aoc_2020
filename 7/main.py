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
    def __init__( self, color, children):
        self._color = color
        self._children = []
        self._parents = []
        self._gold = False
        for child in children:
            if( child[0] == "shiny gold" ):
                self._gold = True
            self._children.append( [ child, 0 ] )

    def addChild( self, newChild ):
        for child in self._children:
            if( child[0][0] == newChild._color ):
                if( newChild._gold ):
                    self._gold = True
                newChild._parents.append( self )
                child[1] = newChild
                return

def partOne( lines ):
    elementList = []
    for line in lines:
        children = []
        line = line.split("contain")
        color = " ".join(line[0].split( " " )[:2] )
        if( not "no other bags." in line ):
            receipt = line[1].replace('.', '')
            temp = [ receipt ]
            if( "," in line[1]):
                temp = receipt.split(',')
            for e in temp:
                e = e.split(" ")[1:]
                childNumber = e[0]
                childColor = " ".join( e[1:3] )
                children.append( [ childColor, childNumber ] )
        newElement = element( color, children )
        elementList.append( newElement )
        for currentElement in elementList:
            currentElement.addChild( newElement )
    counter = 0
    for currentElement in elementList:
        if( currentElement._gold ):
            parents = currentElement._parents
            current = 0
            if( len( parents ) ):
                current = parents.pop()
            while( current ):
                current._gold = True
                parents += current._parents
                current = 0
                if( len( parents ) ):
                    current = parents.pop()
                    current._gold = True

    for currentElement in elementList:
        if( currentElement._gold ):
            counter += 1
    print( "PartOne: ", counter )

def partOneV2( lines ):

def partTwo( lines ):
    pass

def main():
    lines = readInput()
    partOne( lines )
    partTwo( lines )


if __name__ == "__main__":
    main()
