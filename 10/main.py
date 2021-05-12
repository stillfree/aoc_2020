#!/usr/bin/env python3
import sys, time, math
from anytree import Node, RenderTree, PreOrderIter
import numpy as np


def readInput():
    if( len( sys.argv ) == 2 ):
        file = open( sys.argv[1] , "r")
    else:
        file = open("input", "r")
    lines = file.readlines()
    return lines

def partOne( lines ):
    num1 = 0
    num3 = 0
    current = 0
    numbers = list( map( lambda x: int(x), lines ) )
    numbers.sort()
    for i in range( len( numbers ) ):
        difference = numbers[i] - current
        if( difference == 1 ):
            num1 += 1
        elif( difference == 3):
            num3 += 1
        current = numbers[i]
    num3 += 1
    print( "Part One: ", num1 * num3 )
    return numbers

def recursive( numbers ):
    global options
    numbers = list( numbers )
    if( numbers not in variations ):
        variations.append( numbers )
        options += 1
    if( len( numbers ) == 0 ):
        return
    i = 0
    while( i < len( numbers ) - 2):
        difference = numbers[ i +1 ] - numbers[i]
        if( difference == 1 ):
            nextdifference = numbers[ i + 2 ] - numbers[i + 1]
            if( nextdifference <= 2):
                copy = list( numbers )
                copy.remove( numbers[i + 1] )
                recursive( copy )
        elif( difference == 2 ):
            nextdifference = numbers[ i + 2 ] - numbers[i + 1]
            if( nextdifference == 1):
                copy = list( numbers )
                copy.remove( numbers[i + 1] )
                recursive( copy )
        i += 1

def allpaths(start):
    skip = len(start.path) - 1
    return [leaf.path[skip:] for leaf in PreOrderIter(start, filter_=lambda node: node.is_leaf)]

def partTwo( numbers ):
    global options
    numbers = [ 0 ] + numbers + [ max(numbers) + 3 ]
    rootNode = Node("0")
    numberList = [0]
    nodeList = [rootNode]
    while( len( nodeList ) ):
        current = numberList.pop(0)
        currentNode = nodeList.pop(0)
        for i in range( 1, 4 ):
            if( current + i in numbers ):
                #Node(str( i + current ), parent=currentNode)
                numberList.append( current + i )
                nodeList.append( Node(str( i + current ), parent=currentNode) )

    print( "Part Two:", len( allpaths( rootNode ) ) )

OUTLET_JOLTAGE = 0

def partThree ( joltages ):
    joltages = [ 0 ] + joltages + [ max(joltages) + 3 ]
    compatible = {}
    for i, joltage in enumerate(joltages[:-1]):
        compatible[joltage] = [j for j in joltages[i+1:i+4] if j - joltage <= 3]

    numArrangements = {joltages[-1]: 1}
    for joltage in reversed(joltages[:-1]):
        numArrangements[joltage] = sum(numArrangements[j] for j in compatible[joltage])
    print ( numArrangements )
    return numArrangements[OUTLET_JOLTAGE]

def main():
    lines = readInput()
    numbers = partOne( lines )
    #partTwo( numbers )
    print( partThree( numbers ) )


if __name__ == "__main__":
    main()
