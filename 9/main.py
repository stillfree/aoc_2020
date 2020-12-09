#!/usr/bin/env python3
import sys, time, math

def readInput():
    if( len( sys.argv ) >= 2 ):
        file = open( sys.argv[1] , "r")
    else:
        file = open("input", "r")
    lines = file.readlines()
    return lines

def partOne( lines ):
    lines = list( map( lambda x : int(x), lines ) )
    preamble = 25
    if( len( sys.argv ) == 3 ):
        preamble = int( sys.argv[2] )
    pointer = preamble
    while( pointer < len( lines ) ):
        available = lines[pointer-preamble:pointer]
        current = lines[pointer]
        works = False
        for number in available :
            result = current - number
            if( result == number ):
                continue
            elif( result in available ):
                works = True
                break
        if( not works ):
            print( "Part One: ", current )
            partTwo = list( lines )
            keks = []
            for i in range( len( partTwo ) ):
                currentArray = [partTwo[i]]
                currentSum = partTwo[i]
                keks.append( i )
                for j in range(1, len( partTwo ) - i ):
                    currentSum += partTwo[ i + j ]
                    currentArray.append( partTwo[ i + j ] )
                    if( currentSum > current ):
                        break
                    if( currentSum == current ):
                        mind = min(currentArray)
                        maxi = max(currentArray)
                        print("Part Two: ", mind+maxi)
                        exit()

            break
        pointer += 1

def partTwo( lines ):
    pass

def main():
    lines = readInput()
    partOne( lines )
    partTwo( lines )


if __name__ == "__main__":
    main()
