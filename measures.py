# Authors: Hallie Wiese, Ben Segal, Sarah Brock, Shao-Kai Lai
# uniqnames: hamawies, bensegal, mathwhiz, sklai
# Date: 12/5/2014
# Purpose: Calculating the mean, variance, standard deviation, and median from a list of data.
# Description: Implementation of mean, variance, stdev, and median functions.

import sys
import math
import eecsCsv
import measures

"""
Requires: data is a list of numbers
Modifies: nothing
Effects: returns the average of the numbers in data
"""
def mean(data):
    nsum = sum(data)
    c = len(data)
    m = nsum / float(c)
    return m



"""
Requires: data is a list of numbers
Modifies: nothing
Effects: returns the variance of the numbers in data. an explanation of how to
    calculate variance is in the spec
"""


def variance(data):
    c = len(data)
    m = mean(data)
    total = 0
    for v in data:
        var1 = v - m
        var2 = math.pow(var1, 2)
        total += var2
    vfinal = total / c
    return vfinal

"""
Requires: data is a list of numbers
Modifies: nothing
Effects: returns the standard deviation of the numbers in data
"""


def stdev(data):
    a = variance(data)
    sd = math.sqrt(a)
    return sd

"""
Requires: data is a list of numbers
Modifies: data
Effects: returns the median of the numbers in data. be careful that when you use
    this function, that the order of the objects in data will be modified.
    therefore, any lists that are passed to data must be able to be changed
"""


def median(data):
    datacopy = list(data)
    datacopy.sort()
    a = len(datacopy)
    med = 0
    if a % 2 == 0:
        mid = a / 2
        med = (datacopy[mid] + datacopy[mid - 1]) / 2.0
    else:
        mid = a / 2
        med = datacopy[mid]
    return med


