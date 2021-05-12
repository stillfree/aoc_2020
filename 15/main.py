#!/usr/bin/env python3
import sys, time, math

def readInput():
    if( len( sys.argv ) == 2 ):
        file = open( sys.argv[1] , "r")
    else:
        file = open("input", "r")
    lines = file.readlines()
    return lines

def partOne( lines, limit):
    for line in lines:
        past = {}
        startNumbers =  line.strip().split(",")
        counter = len(startNumbers)
        lastSpoken = 0
        for i in range (len( startNumbers )):
            past[str(startNumbers[i])] = [i]
            lastSpoken = startNumbers[i]
        while( counter < limit ):
            lastNumber = past[str(lastSpoken)]
            spoken=len(lastNumber)
            if( spoken == 1 ):
                if "0" in past:
                    past["0"] = [max(past["0"])] + [counter ]
                else:
                    past["0"] = [counter ]
                lastSpoken = 0
            else:
                number  = lastNumber[len(lastNumber)-1] - lastNumber[len(lastNumber)-2]
                lastSpoken = number
                if str(number) in past:
                    past[str(number)] = [max(past[str(number)])] + [ counter ]
                else:
                    past[str(number)] = [ counter ]
            counter += 1
            #print(counter)
            #print(past["0"])
        print( lastSpoken )

def partTwo( lines, limit):
    partOne( lines, limit )

def main():
    lines = readInput()
    partOne( lines, 2020 )
    partTwo( lines, 30000000 )


if __name__ == "__main__":
    main()
