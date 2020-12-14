#!/usr/bin/env python3
import sys, time, math, re

def readInput():
    if( len( sys.argv ) == 2 ):
        file = open( sys.argv[1] , "r")
    else:
        file = open("input", "r")
    lines = file.readlines()
    return lines

def partOne( lines ):
    memory = [0]*230000
    for line in lines:
        if( "mask" in line ):
            ormask = int( re.sub("[^0-9]", "", line.replace( "X", "0")), 2)
            andmask = int( re.sub("[^0-9]", "", line.replace( "X", "1" )), 2)
        else:
            numbers =  list( map( lambda x: re.sub("[^0-9]", "", x ), line.split(" ")))
            slot = int(numbers[0])
            number = int(numbers[2])
            result = (number & andmask ) | ormask
            memory[slot] = result

        #"{0:b}".format(result)
    summe = 0
    for mem in memory:
        summe += mem
    print( summe )


def partTwo( lines ):
    memory = {}
    numX = 0
    for line in lines:
        if( "mask" in line ):
            line = line.replace("mask = ", "" ).replace("\n","")
            numX = line.count("X")
            maskLen = len(line) - 1
            indexX = [i for i, ltr in enumerate(line) if ltr == "X"]
            indexX.sort( reverse=True)
            ormask = int( re.sub("[^0-9]", "", line.replace( "X", "0")), 2)
            XMASK = int( re.sub("[^0-9]", "", line.replace("0", "1").replace( "X", "0")),2)
        else:
            numbers =  list( map( lambda x: re.sub("[^0-9]", "", x ), line.split(" ")))
            slot = int(numbers[0])
            number = int(numbers[2])
            result = (slot | ormask ) & XMASK
            for i in range( 2**numX ) :
                ind = result
                for shift in range( numX ):
                    value = (( (i >> shift) & 1) << maskLen - indexX[shift] )
                    ind = ind | value
                memory[str(ind)] = number

    summe = 0
    for mem in memory:
        summe += memory[mem]
    print( summe )

def main():
    lines = readInput()
    partOne( lines )
    partTwo( lines )

if __name__ == "__main__":
    main()
