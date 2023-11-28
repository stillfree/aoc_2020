#!/usr/bin/env python3
import sys, time, math

import numpy as np
import math

TOP = 0
RIGHT = 1
BOTTOM = 2
LEFT = 3

reverseDirection = [2,3,0,1]

def getRightSide(tile):
    result = []
    for line in tile:
        result.append(line[len(line)-1])
    return "".join(result)

def getLeftSide(tile):
    result = []
    for line in tile:
        result.append(line[0])
    #return "".join(result)
    return str("".join(result))[::-1]

def getTopSide(tile):
    return "".join(tile[0])

def getBottomSide(tile):
    #return "".join(tile[len(tile)-1])
    return str("".join(tile[len(tile)-1]))[::-1]

def readInput():
    if( len( sys.argv ) == 2 ):
        file = open( sys.argv[1] , "r")
    else:
        file = open("input", "r")
    lines = [ e.rstrip() for e in file.readlines() ]
    return lines

tileMap = {}

def getTiles(lines):
    tiles =  []
    tile = []
    for line in lines:
        if line == "":
            tileMap[tile[0]] = tile[1:]
            tiles.append(tile)
            tile = []
        elif "." in line or "#" in line:
            tile.append(line)
        else:
            tile.append(line.split(" ")[1][:-1])
    return tiles

def getBorders(tile):
    matrix = tile[1:]
    borders = []
    bordersFlipped = []


    borders.append(matrix[0])
    borders.append(matrix[len(matrix)-1])

    bordersFlipped.append(matrix[0][::-1])
    bordersFlipped.append(matrix[len(matrix)-1][::-1])
    border1 =  ""
    border2 =  ""

    for line in matrix:
        border1 += line[0]
        border2 += line[len(line)-1]
    borders.append(border1)
    borders.append(border2)

    bordersFlipped.append(border1[::-1])
    bordersFlipped.append(border2[::-1])
    borders += bordersFlipped
    return borders




def toNumber(string):
    string = "".join([ "1" if x == "#" else "0" for x in string ])
    return int(string, 2)

def fromBinToNum(string):
    return int(string, 2)

def convertToNumpyArray(tile):
    temp = []
    for line in tile:
        temp.append([ "1" if x == "#" else "0" for x in line ])
    return np.array(temp)

similars = {}
borderMap = {}

same = {}

def rotateRight(array):
    return np.rot90(array)

def rotateLeft(array):
    return np.rot90(array, -1)

def flipArray(array):
    return np.fliplr(array)

def partOne( lines ):
    tiles = getTiles(lines)
    for tile in tiles:
        key = tile[0]
        borderMap[key] = []
        for border in getBorders(tile):
            borderMap[key].append(toNumber(border))
        #print(borderMap[key])

    for key in borderMap.keys():
        compareKeys = set(borderMap.keys())
        compareKeys.remove(key)
        counter = 0
        similars[key] = [[],0,set()]
        for compareKey in compareKeys:
            similar = set(borderMap[key]).intersection(borderMap[compareKey])
            if len(similar):
                #print(key, compareKey, similar)
                counter += 1
                similars[key][0].append(compareKey)
                similars[key][2].update(similar)
        similars[key][1] = counter
        #print(key, counter)

def getSide(tile, direction):
    if direction == TOP:
        return getTopSide(tile)
    elif direction == BOTTOM:
        return getBottomSide(tile)
    elif direction == RIGHT:
        return getRightSide(tile)
    elif direction == LEFT:
        return getLeftSide(tile)

def findCorrectOrientation(tile, numberString, direction):
    number = fromBinToNum(numberString)
    print("Numbers to find in", direction, number, numberString, numberString[::-1])
    currentTile = tile
    if( fromBinToNum(getSide(tile, direction)) == number ):
        return np.array(currentTile)
    for j in range(2):
        for i in range(3):
            if( fromBinToNum(getSide(currentTile, direction)) == number ):
                print("Right orientation", currentTile)
                return np.array(currentTile)
            print("Trying this", currentTile)
            currentTile = rotateRight(currentTile)
        currentTile = flipArray(currentTile)
    return np.array(currentTile)

def getEdgesNumbers(tile):
    result = []
    result.append([0, fromBinToNum(getTopSide(tile))])
    result.append([1, fromBinToNum(getRightSide(tile))])
    result.append([2, fromBinToNum(getBottomSide(tile))])
    result.append([3, fromBinToNum(getLeftSide(tile))])
    return result

def addDirection(position, direction):
    x, y = position
    if direction == TOP:
        y -= 1
    elif direction == BOTTOM:
        y += 1
    elif direction == RIGHT:
        x += 1
    elif direction == LEFT:
        x += 1
    return [x, y]

def removeBorders(tile):
    result = []
    for line in tile[1:-1]:
        for element in line[1:-1]:
            result.append(element)
    return result

def getTile(alreadyPlaced, position):
    gridSize = int(math.sqrt(len(alreadyPlaced)))
    for x in range(gridSize):
        for y in range(gridSize):
            for compareKey, compareTile, comparePosition in alreadyPlacedTiles:
                if(position == comparePosition ):
                    return compareTile


def partTwo( lines ):
    startTile = 0
    for key in similars.keys():
        if similars[key][1] == 2:
            startTileKey = key
    currentTile = tileMap[startTileKey]
    currentTile = convertToNumpyArray(currentTile)

    broken = False
    for j in range(2):
        for i in range(3):
            right = getRightSide(currentTile)
            bottom = getBottomSide(currentTile)
            if(fromBinToNum(right) in similars[startTileKey][2]
                    and fromBinToNum(bottom) in similars[startTileKey][2]):
                broken = True
                break
            currentTile = rotateRight(currentTile)
        if broken:
            break
        currentTile = flipArray(currentTile)
    #Add tiles to worklist

    alreadyPlacedTiles = [[startTileKey, currentTile, [0,0]]]
    workList = []

    for tile in getTiles(lines):
        key = tile[0]
        if (key != startTileKey):
            workList.append([key, convertToNumpyArray(tile[1:])])


    while(len(workList)):
        #print(len(workList))
        key, tile =  workList.pop(0)
        # Check if tile can be placed to already set tile
        tempTileOrientation = tile
        mySimilars = similars[key]
        #print(mySimilars)

        placed = False
        for compareKey, compareTile, comparePosition in alreadyPlacedTiles:
            if compareKey in mySimilars[0]:
                placed = True
                edges = getEdgesNumbers(compareTile)
                print(key, compareKey, edges)
                #print([ x[1] for x in edges])
                for direction, number in edges:
                    if number in mySimilars[2]:
                        print("Using edge: ", number, direction)
                        newDirection = reverseDirection[direction]
                        position = addDirection(comparePosition, direction)
                        print("new Position", direction, position, comparePosition)
                        print("")
                        print(getEdgesNumbers(currentTile))
                        numberString = getSide(compareTile, direction)
                        currentTile = findCorrectOrientation(tempTileOrientation, numberString, newDirection)
                        print(currentTile)
                        placedTile = [key, currentTile, position]
                        print("New lined up tile:", getEdgesNumbers(currentTile))
                        alreadyPlacedTiles.append(placedTile)
                break

        # put it back in workList
        if not placed:
            workList.append([key, tile])

        print("")
    editedTiles = []
    ## Delete borders
    for compareKey, compareTile, comparePosition in alreadyPlacedTiles:
        editedTiles.append([compareKey, removeBorders(compareTile), comparePosition])

    bigGrid = []
    gridSize = int(math.sqrt(len(alreadyPlacedTiles)))

    tileGrid = []
    row = []
    for x in range(gridSize):
        row = []
        for y in range(gridSize):
            for compareKey, compareTile, comparePosition in alreadyPlacedTiles:
                if([x, y] == comparePosition ):
                    #print(compareKey, comparePosition)
                    row.append([compareKey, compareTile, comparePosition])
                    print(compareKey + " ", end="")
        tileGrid.append(row)



#TOP = 0
#RIGHT = 1
#BOTTOM = 2
#LEFT = 3


def main():
    lines = readInput()
    partOne( lines )
    partTwo( lines )


if __name__ == "__main__":
    main()
