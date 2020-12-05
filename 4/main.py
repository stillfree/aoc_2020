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
    return { "byr" :"???", "iyr": "???", "eyr" :"???", "hgt": "???", "hcl": "???", "ecl": "???", "pid": "???", "cid": "???" }



def partOne( lines ):
    idList = []
    generatedID = generateEmptyID()
    for line in lines:
        if(line == "\n"):
            idList.append( generatedID )
            generatedID = generateEmptyID()
            continue
        line = line.split( ' ' )
        for element in line:
            element = element.split( ':' )
            generatedID[ element[0] ] = element[1].replace('\n', '')
    idList.append( generatedID )
    counter = 0
    for currentID in idList:
        valid = True
        for element in currentID:
            if( element != "cid" ):
                if currentID[ element ] == "???":
                    valid = False
        if( valid ):
            counter += 1
    print( "PartOne: ", counter )
    return( idList )

def partTwo( idList ):
    counter = 0
    Checklist = [ "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid" ]
    print(len( idList ))
    for currentID in idList:
        invalid = False
        for check in Checklist:
            element = currentID[check]
            try:
                if( check == "byr" ):
                    if( int(element) > 2002 or int(element) < 1920):
                        invalid = True
                        #print("Invalid:", element, check)
                elif( check == "iyr" ):
                    if( int(element) < 2010 or int(element) > 2020):
                        invalid = True
                        #print("Invalid:", element, check)
                elif( check == "eyr"):
                    if( int(element) < 2020 or int(element) > 2030):
                        invalid = True
                        #print("Invalid:", element, check)
                elif( check == "hgt"):
                    if( "cm" in element ):
                        element = element.replace("cm","")
                        if ( int(element) > 193 or int(element) < 150 ):
                            invalid = True
                            #print("Invalid:", element, check)
                    elif( "in" in element ):
                        #print( check, element )
                        element = element.replace("in","")
                        if ( int(element) > 76 or int(element) < 59 ):
                            invalid = True
                            #print("Invalid:", element, check)
                    else:
                        invalid = True
                elif( check == "hcl"):
                    if( element[0] != "#" ):
                            invalid = True
                    element = element.replace('#','' )
                    number = int( element, 16 )
                    if( number < 0 or number > 0xFFFFFF ):
                        invalid = True
                        #print("Invalid:", element, check)
                elif( check == "ecl"):
                    if( element not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
                        invalid = True
                        #print("Invalid:", element, check)
                elif( check == "pid"):
                    if( len(element) != 9 or int( element ) < 0 or int(element) > 999999999 ):
                        invalid = True
                else:
                    invalid = True
                    print("Invalid:", element, check)
            except Exception as e:
                #print( e, check, element )
                invalid = True
        if( not invalid ):
            print( currentID )
            counter += 1
    print( "PartTwo: ", counter )


def main():
    lines = readInput()
    idList = partOne( lines )
    partTwo( idList )


if __name__ == "__main__":
    main()
