#!/usr/bin/env python3
import sys, time, math

def readInput():
    if( len( sys.argv ) == 2 ):
        file = open( sys.argv[1] , "r")
    else:
        file = open("input", "r")
    lines = file.readlines()
    return lines

def getPN( string ):
    return int( string.replace("\n", "") )

def partOne( lines ):
    acc = 0
    op = 0
    programCode = list( lines )
    while( 1 ):
        print( "OP:", op )
        if( "visited" in programCode[op] ):
            break
        programCode[op] = programCode[op] + " visited"
        line = programCode[op].split( " ")
        print( "Current Line: ", line )
        if( line[0] == "nop"):
            op += 1
        elif( line[0] == "acc"):
            acc += getPN( line[1] )
            op += 1
        elif( line[0] == "jmp"):
            op += getPN( line[1] )
    print( acc )

def partTwo( lines ):
    options = []
    lineNumber = 0
    for line in lines:
        if( "nop" in line  ):
            options.append( [ lineNumber, "nop", "jmp" ] )
        elif( "jmp" in line  ):
            options.append( [ lineNumber, "jmp", "nop" ] )
        lineNumber += 1

    for opt in options:
        acc = 0
        op = 0
        lineNumber = opt[0]
        programCode = list( lines )
        maxOp = len( programCode ) - 1
        programCode[lineNumber] = programCode[lineNumber].replace( opt[1], opt[2] )
        while( 1 ):
            if( "visited" in programCode[op] ):
                break
            programCode[op] = programCode[op] + " visited"
            line = programCode[op].split( " ")
            if( line[0] == "nop"):
                op += 1
            elif( line[0] == "acc"):
                acc += getPN( line[1] )
                op += 1
            elif( line[0] == "jmp"):
                op += getPN( line[1] )
            if( op > maxOp ):
                print( acc )
                return

def main():
    lines = readInput()
    partOne( lines )
    partTwo( lines )


if __name__ == "__main__":
    main()
