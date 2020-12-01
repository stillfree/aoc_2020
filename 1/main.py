#!/usr/bin/env python3
import sys
import time
import math

fastArray = [ 0 ] * 2021

def readInput():
    file = open("input", "r")
    #file = open("testinput", "r")
    lines = file.readlines()
    return lines

def evaluateList( array ):
    for A in array:
        for B in array:
            if( A + B == 2020  ):
               print( A, B, A * B )
               return
            elif( A + B > 2020 ):
                continue

def partOne( lines ):
    even = []
    odd = []
    for e in lines:
        e.replace('\n', '')
        number = int( e )
        fastArray[number] = 1
        if ( number % 2 == 0 ):
            even.append( number )
        else:
            odd.append( number )
    odd.sort()
    even.sort()
    evaluateList( even )
    evaluateList( odd )
    return( even , odd )

def shortenList( liste, value):
    returnlist = []
    for e in liste:
        if e < value:
            returnlist.append( e )
        else:
            return returnlist
    return returnlist

def partTwo( even, odd ):
    sumList = even + odd
    sumList.sort()
    for chosen in sumList:
        for second in shortenList( sumList, 2020 - chosen ):
            left = 2020 - chosen - second
            if( fastArray[left]  == 1 ):
                print( chosen, second, left, left*chosen*second )
                return

def main():
    lines = readInput()
    even, odd = partOne( lines )
    partTwo( even, odd )
    #print(lines)


if __name__ == "__main__":
    main()
