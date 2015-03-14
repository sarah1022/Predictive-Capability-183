# Authors: Hallie Wiese, Ben Segal, Sarah Brock, Shao-Kai Lai
# uniqnames: hamawies, bensegal, mathwhiz, sklai
# Date: 12/5/2014
# Purpose: To find the covariance of a single sample of two lists of values and to find the correlation matrix
#          of the dictionary.
# Description: Implementation of singleSampleCovariance and correlationMatrix functions.

import sys
import math
import eecsCsv
import measures

"""
Requires: xVals is a list of all of the values for the first random variable
yVals is a list of all of the values for the second random variable
meanX is the average of all of the values in xVals
meanY is the average of all of the values in yVals
Modifies: nothing
Effects: returns the sample covariance between xVals and yVals
"""


def singlePopulationCovariance(xVals, yVals, meanX, meanY):
    sum_xy = 0
    for i in range(0, len(xVals)):
        sum_xy += ((xVals[i] - meanX) * (yVals[i] - meanY))
    return sum_xy / len(xVals)



"""
Requires: dictionary is a dictionary built by parseCSVFile
inclusionList is the same length as all of the entries in dictionary
for each entry in inclusionList, the value is 1 if that entry is to be
included in the correlation matrix, and 0 if it is not
Modifies: nothing
Effects: returns a list of lists, holding the correlation matrix for the
selected entries
"""


def correlationMatrix(dictionary, inclusionList):
    # Counts the number of included entries/columns and
    # 'count' will be the size of the nxn matrix.
    count = 0
    for i in inclusionList:
        if i == 1:
            count += 1

    # Determines whether a column of the csv file will be
    # included in the correlation matrix and whether that
    # column is made up of integers or floats. The 'data'
    # list will include the list of column values and the
    # mean and standard deviation of these values. Each time
    # through the loop adds 'data' to 'tempMat.' tempMat will
    # hold the list, mean, and standard deviation for each
    # column of the csv file that is included.
    tempMat = []
    index = 0
    while index < len(inclusionList):
        if inclusionList[index] == 1:
            entryList = eecsCsv.retrieveEntireAttribute(dictionary, index)
            if isinstance(entryList[0], int) or isinstance(entryList[0], float):
                entryListMean = measures.mean(entryList)
                entryListStDev = measures.stdev(entryList)
                data = [entryList, entryListMean, entryListStDev]
            else:
                data = [[], 0, 0]
            tempMat.append(data)
        index += 1

    # 'count' denotes the size of the square correlation matrix,
    # which will be of size (count)x(count). The while loop
    # determines if the current 'value' or 'num is a string
    # column, whether the correlation of 'value' is being
    # compared with itself. Otherwise the function calculates
    # the correlation between two lists of data. The determined
    # correlation is added to the 'Numbers' list. When 'Numbers'
    # is added to 'corrMat', this will denote a row of the
    # correlation matrix.
    corrMat = []
    for value in range(0, count):
        Numbers = []
        num = 0
        while num < count:
            if (len(tempMat[value][0]) == 0) or (len(tempMat[num][0]) == 0):
                numbersValue = 0
            elif num == value:
                numbersValue = 1
            else:
                cov = singlePopulationCovariance(tempMat[value][0], tempMat[num][0], tempMat[value][1], tempMat[num][1])
                standardDV = tempMat[value][2] * tempMat[num][2]
                numbersValue = cov / standardDV
            Numbers.append(numbersValue)
            num += 1

        corrMat.append(Numbers)

    return corrMat

