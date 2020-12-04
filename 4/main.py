#!/usr/bin/env python3
import sys, time, math

def readInput():
    if( len( sys.argv ) == 2 ):
        file = open( sys.argv[1] , "r")
    else:
        file = open("input", "r")
    lines = file.readlines()
    return lines

def generateEmptyID():
    return { ["byr", "0"], ["iyr", "0"], ["eyr", "0"], ["hgt", "0"], ["hc," "0"], ["ecl", "0"], ["pid", "0"], ["cid", "0"] }

def partOne( lines ):
    idList = []
    generatedID = generateEmptyID()
    for line in lines:
        if(line == "\n"):
            idList.append( currentid )
            generatedID = generateEmptyID()
            continue
        line.split( ' ' )
        line.remove( "" )
        for element in line:
            element.split( ':' )
            generatedID[ element[0] ] = element[1]()
    counter = 0
    for currentID in idList:
        valid = false
        for element in currentID:
            if( element ):
                pass
        if( valid ):
            counter += 1




def partTwo( lines ):
    pass

def main():
    lines = readInput()
    print(lines)
    partOne( lines )
    partTwo( lines )


if __name__ == "__main__":
    main()
