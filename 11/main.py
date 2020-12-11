#!/usr/bin/env python3
import sys, time, math

def readInput():
    if( len( sys.argv ) == 2 ):
        file = open( sys.argv[1] , "r")
    else:
        file = open("input", "r")
    lines = file.readlines()
    return lines

def count( seats ):
    counter = 0
    for row in seats:
        for char in row:
                counter += 1 if (char == "#") else 0
    return counter

def printGrid( grid ):
    for line in grid:
        print( line )

def partOne( lines ):
    lines = list(lines )
    columns = len(lines[0])
    rows = len(lines)
    for i in range(len( lines ) ):
        lines[i] = "." + lines[i].replace("\n","") + "."
    lines = ["."*(columns+2)] + lines + ["."*(columns+2)]
    newseats = list( lines )
    seats = list( lines )
    change = True
    lastRound = 0
    while( change ):
        #printGrid( seats )
        for i in range( rows ):
            for j in range( columns ):
                seat = seats[i+1][j+1]
                if( seat == "L" ):
                    string = seats[i][j:j+3] + seats[i+1][j:j+3] + seats[i+2][j:j+3]
                    if( string.count("#") == 0 ):
                        newseats[i+1] = newseats[i+1][:j+1] + '#' + newseats[i+1][j+2:]
                elif( seat == "#" ):
                    string = seats[i][j:j+3] + seats[i+1][j:j+3] + seats[i+2][j:j+3]
                    if( string.count("#") >= 5 ):
                        newseats[i+1] = newseats[i+1][:j+1] + 'L' + newseats[i+1][j+2:]
        seats = list( newseats )
        counter = count( seats )
        if( counter == lastRound ):
            change = False
            print("Part One:", counter )
            return
        else:
            lastRound = counter
        #time.sleep( 5 )

def inLimit( vector, xLimit , yLimit ):
    x = vector[0]
    y = vector[1]
    if( x >= 0 and x < xLimit and y >= 0 and y < yLimit ):
        return True
    return False

def directional( grid,  row, column  ):
    startVector = [row, column ]
    counter = 0
    for vector in [ [0,1], [1,1], [1,0], [1,-1], [-1,1], [-1,0], [0,-1], [-1,-1] ]:
        multiplier = 1
        result = [startVector[0] + vector[0]* multiplier, vector[1]*multiplier + startVector[1]]
        xLimit = len(grid )
        yLimit = len(grid[0])
        while( inLimit( result, xLimit, yLimit ) ):
            if( grid[result[0]][result[1]] == "L" ):
                break
            elif( grid[result[0]][result[1]] == "#" ):
                counter += 1
                break

            multiplier += 1
            result = [startVector[0] + vector[0]* multiplier, vector[1]*multiplier + startVector[1]]
    return counter

def partTwo( lines ):
    lines = list(lines )
    columns = len(lines[0])
    rows = len(lines)
    for i in range(len( lines ) ):
        lines[i] = "." + lines[i].replace("\n","") + "."
    lines = ["."*(columns+1)] + lines + ["."*(columns+1)]
    newseats = list( lines )
    seats = list( lines )
    change = True
    lastRound = 0
    while( change ):
        for i in range( rows ):
            for j in range( columns ):
                seat = seats[i+1][j+1]
                if( seat == "L" ):
                    number = directional( seats, i+1, j+1 )
                    if( number == 0 ):
                        newseats[i+1] = newseats[i+1][:j+1] + '#' + newseats[i+1][j+2:]
                elif( seat == "#" ):
                    number = directional( seats, i+1, j+1 )
                    if( number >= 5 ):
                        newseats[i+1] = newseats[i+1][:j+1] + 'L' + newseats[i+1][j+2:]
        seats = list( newseats )
        counter = count( seats )
        if( counter == lastRound ):
            change = False
            print( "Part Two:", counter )
            return
        else:
            lastRound = counter

def main():
    lines = readInput()
    partOne( lines )
    partTwo( lines )


if __name__ == "__main__":
    main()
