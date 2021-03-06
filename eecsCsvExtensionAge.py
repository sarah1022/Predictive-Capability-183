# Authors: Hallie Wiese, Ben Segal, Sarah Brock, Shao-Kai Lai
# uniqnames: hamawies, bensegal, mathwhiz, sklai
# Date: 12/5/2014
# Purpose: Extension - Create a dictionary of lists in order to later retrieve values and entire attributes.
# Description: Implementation of parseCSVFile, retrieveValue, and retrieveEntireAttribute functions.

import sys
import csv

"""
This function reads in a CSV file and stores the values therein in a
dictionary. The key in the key-value pair is one of the entries in the
table, and the value is a list of the entries (which are themselves lists)
associated with that value in the table.

For the purposes of the bare-bones, the key is the name of the storm, and
the values stored in the list are as follows:
name, date, time, system_status, lat, lon, wind, pressure
The types of these values for the purposes of grading of core functionality
are:
str, str, str, str, float, float, int, int

When you are writing your own function to read in your specific file, you
can set the types to whatever you see fit.

For the purposes of your extension, you will need to modify this code so
that it works for your data set. You can decide what the key and values are,
but make sure you choose your key wisely.

In any event, this function will return the dictionary that is built by
parsing the CSV file.

Requires: fileName contains the name of the CSV file
Modifies: nothing
Effects: See the above.
"""


def parseCSVFile(fileName):
    csvfile = open(fileName, 'r')
    ageDict = {}

    # Reading in one line at a time from the csv file.
    while True:
        line = csvfile.readline()
        if not line:
            break

        if line[0] != "A":
            continue
    
    # Extracts key name from header line.
        line = line.replace(" ", "")
        headerList = line.split(',')
        name = headerList[1]
        numEntries = int(headerList[2])
        
    # For each detail line of the current age range,
    # the key (age range) and the desired entries
    # are added to the list 'data'. The key 'name' 
    # and 'data' are appended to the dictionary
    # ageDict as a key-value pair.
        data = []
        count = 0
        while count < numEntries:
            detLine = csvfile.readline()
            detLine = detLine.replace(" ", "")
            detLine = detLine.split(',')
            detLine[0] = int(detLine[0])
            detLine[1] = int(detLine[1])
            detLine[2] = int(detLine[2])
            detLine[3] = int(detLine[3])
            detLine[4] = int(detLine[4])
            detLine[5] = int(detLine[5])
            detLine[6] = int(detLine[6])
            detLine[7] = int(detLine[7])
            detLine[8] = int(detLine[8])
            detLine[9] = int(detLine[9])
            detLine[10] = int(detLine[10])
            detLine[11] = float(detLine[11])
            detLine[12] = float(detLine[12])
            detLine[13] = float(detLine[13])
            detLine[14] = float(detLine[14])
            detLine[15] = float(detLine[15])
            detLine[16] = float(detLine[16])
            detLine[17] = float(detLine[17])
            detLine[18] = float(detLine[18])
            detLine[19] = float(detLine[19])
            detailList = [name]
            detailList.extend(detLine[0:len(detLine) - 1])
            data.append(detailList)
            count += 1
        ageDict[name] = data
    return ageDict



"""
This function retrieves an entry from the list of entries in the dictionary
for a given key and position in the list for the key.

Requires: dictionary is the dictionary built in parseCSVFile, key is the
key from which we want to fetch values, and entry is the index of the
entry we wish to fetch

Modifies: nothing
Effects: retrieves a single entry from the list of entries in the dictionary
such that entry holds the position in the list of entries, and that key
is the key from which we wish to fetch it
"""


def retrieveValue(dictionary, key, entry):
    row = dictionary[key]
    value = row[entry]
    return value


"""
Requires: dictionary holds a dictionary created by parseCSVFile
columnNo holds the index of the attribute we wish to create a list from
Modifies: nothing
Effects: returns a list of the values in the column specified by columnNo
"""


def retrieveEntireAttribute(dictionary, columnNo):
    keylist = dictionary.keys()
    keylist.sort()
    list1 = []
    for key in keylist:
        for row in dictionary[key]:
            list1.append(row[columnNo])
    return list1

def retrieveEntireAttributeAge(dictionary, key, columnNo):
    keylist = dictionary.keys()
    list1 = []
    if key in keylist:
        for row in dictionary[key]:
            list1.append(row[columnNo])
    return list1

def retrieveKeyListAge(dictionary, key):
    keylist = dictionary.keys()
    if key in keylist:
        return True
    else:
        return False