#!/usr/bin/env python3
import sys, time, math

def readInput():
    if( len( sys.argv ) == 2 ):
        file = open( sys.argv[1] , "r")
    else:
        file = open("input", "r")
    lines = file.readlines()
    return lines

def calculate( string ) :
    string = string.replace( '\n', '')
    characterList = []
    for char in string:
        if( char not in characterList ):
            characterList.append( char )
    return len( characterList )

def calculateTwo( string ) :
    lineNum = string.count( '\n' )
    characterLists = []
    characterLists.append( [] )
    index = 0
    for char in string:
        if( char == '\n'):
            index += 1
            characterLists.append( [] )
        else:
            if( char not in characterLists[index]):
                characterLists[index].append( char )
    summe = 0
    sumList = ""
    for characterList in characterLists:
        for char in characterList:
            sumList += char

    for i in range( 97, 123 ):
        if( sumList.count( chr( i ) ) == lineNum ):
            summe += 1
    return summe

def partOne( lines ):
    currentStr = ""
    summe = 0
    for line in lines:
        if( line == "\n"):
            summe += calculate( currentStr )
            currentStr = ""
        else:
            currentStr += line
    summe +=  calculate( currentStr )
    print( "Part One: ", summe )


def partTwo( lines ):
    currentStr = ""
    summe = 0
    for line in lines:
        if( line == "\n"):
            summe += calculateTwo( currentStr )
            currentStr = ""
        else:
            currentStr += line
    summe +=  calculateTwo( currentStr + "\n" )
    print( "Part Two: ", summe )


def main():
    lines = readInput()
    partOne( lines )
    partTwo( lines )


if __name__ == "__main__":
    main()
