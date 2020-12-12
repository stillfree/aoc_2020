#!/usr/bin/env python3
import sys, time, math
import numpy as np

def readInput():
    if( len( sys.argv ) == 2 ):
        file = open( sys.argv[1] , "r")
    else:
        file = open("input", "r")
    lines = file.readlines()
    return lines
# N = 0, E = 1, S = 2, W = 3
def moveDirection( direction, angle):
    angle = np.deg2rad(angle)
    matrix = np.array( [ [ math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle) ] ] )
    return matrix.dot( direction ).astype(int)


def partOne( lines ):
    direction = np.array( [1,0] )
    position = np.array( [0,0] )
    for line in lines:
        line.replace("\n", "")
        operator = line[0]
        number = int(line[1:])
        if( operator == "N" ):
            position[1] -= number
        elif( operator == "S" ):
            position[1] += number
        elif( operator == "E" ):
            position[0] += number
        elif( operator == "W" ):
            position[0] -= number
        elif( operator == "F" ):
            position = position + direction.dot( number )
        elif( operator == "L" ):
            direction = moveDirection( direction, -number)
        elif( operator == "R" ):
            direction = moveDirection( direction, number)
    print("Part One:", position, abs( position[0]) + abs( position[1] ) )

def rotate( waypoint, position, angle ):
    angle = np.deg2rad(angle)
    matrix = np.array( [ [ math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle) ] ] )
    #waypoint = waypoint - position
    #result =  matrix.dot( waypoint ).astype(int)
    #return result + position
    return matrix.dot(waypoint)#.astype( int )

def partTwo( lines ):
    waypoint = np.array( [10,-1] )
    position = np.array( [0,0] )
    for line in lines:
        line.replace("\n", "")
        operator = line[0]
        number = int(line[1:])
        if( operator == "N" ):
            waypoint[1] -= number
        elif( operator == "S" ):
            waypoint[1] += number
        elif( operator == "E" ):
            waypoint[0] += number
        elif( operator == "W" ):
            waypoint[0] -= number
        elif( operator == "F" ):
            #result = ( waypoint - position ).dot( number )
            position = position + waypoint.dot(number)
        elif( operator == "L" ):
            waypoint = rotate( waypoint, position, -number)
        elif( operator == "R" ):
            waypoint = rotate( waypoint, position, number)
        if( waypoint[0] < 0 or waypoint[1] < 0 ):
            print("NEGATIVE")
            print( waypoint )
        #print("Po",position)
        #print("Wy", waypoint)
    print("Part Two:", int( round( abs( position[0]) + abs( position[1] ) ) ) )

def main():
    lines = readInput()
    partOne( lines )
    partTwo( lines )


if __name__ == "__main__":
    main()
