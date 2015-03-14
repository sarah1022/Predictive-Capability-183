# Authors: Hallie Wiese, Ben Segal, Sarah Brock, Shao-Kai Lai
# uniqnames: hamawies, bensegal, mathwhiz, sklai
# Date: 12/5/2014
# Purpose: Create a dictionary of lists in order to later retrieve values and entire attributes.
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
    hurDict = {}

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

    # For each detail line of the current storm,
    # the key (storm name) and the desired entries
    # are added to the list 'data'. The key 'name'
    # and 'data' are appended to the dictionary
    # hurDict as a key-value pair.
        data = []
        count = 0
        while count < numEntries:
            detLine = csvfile.readline()
            detLine = detLine.replace(" ", "")
            detLine = detLine.split(',')
            detLine[4] = float(detLine[4])
            detLine[5] = float(detLine[5])
            detLine[6] = int(detLine[6])
            detLine[7] = int(detLine[7])
            detailList = [name]
            detailList.extend(detLine[0:2])
            detailList.extend(detLine[3:len(detLine) - 1])
            data.append(detailList)
            count += 1
        hurDict[name] = data
    return hurDict



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



