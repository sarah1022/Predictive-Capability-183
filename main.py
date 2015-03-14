# Authors: Hallie Wiese, Ben Segal, Sarah Brock, Shao-Kai Lai
# uniqnames: hamawies, bensegal, mathwhiz, sklai
# Date: 12/5/2014
# Purpose: To test the functions in our other files (diagnostics.py, eecsCsv.py, generation.py, and measures.py).
# Description:

import sys
import eecsCsv
import eecsCsvExtensionAge
import eecsCsvExtensionState
import generation
import measures
import diagnostics

"""
Use this function for your testing for bare-bones, and then use it as the driver
for your project extension
"""


def main(argv):
    fun = [1, 3, 2]
    print measures.mean(fun)
    print measures.variance(fun)
    print measures.stdev(fun)
    print measures.median(fun)
    print fun
    print

    star = [1, 3, 2, 4]
    print measures.mean(star)
    print measures.variance(star)
    print measures.stdev(star)
    print measures.median(star)
    print star
    print

    k = [1, 3, 2]
    h = [2, 4, 2]
    print diagnostics.singlePopulationCovariance(fun, h, measures.mean(fun), measures.mean(h))
    print diagnostics.singlePopulationCovariance(k, h, measures.mean(k), measures.mean(h))

    a = [3, 9, 6]
    b = [2, 4, 6]
    print diagnostics.singlePopulationCovariance(a, b, measures.mean(a), measures.mean(b))
    print

    print generation.uniformGen()
    print generation.generateFromBinomial(generation.uniformGen(), 3, 0.6)
    print

    print eecsCsv.parseCSVFile("2013hurdat.csv")
    print

    dictionary1 = {'ANDREA': [['ANDREA', '20130605', '1800', 'TS', 25.1, -86.6, 35, 1006],
                              ['ANDREA', '20130606', '0000', 'TS', 25.6, -86.5, 40, 1002]],
                   'BARRY': [['BARRY', '20130605', '1800', 'TS', 25.1, -86.6, 35, 1006],
                             ['BARRY', '20130606', '0000', 'TS', 25.6, -86.5, 40, 1002]]}

    print 'star'
    print eecsCsv.retrieveValue(dictionary1, 'ANDREA', 0)
    print eecsCsv.retrieveValue(dictionary1, 'ANDREA', 1)
    print

    print eecsCsv.retrieveEntireAttribute(eecsCsv.parseCSVFile("2013hurdat.csv"), 5)
    print eecsCsv.retrieveEntireAttribute(eecsCsv.parseCSVFile("2013hurdat.csv"), 0)

    print

    inclist = [0, 0, 0, 0, 1, 1, 1, 1]
    print diagnostics.correlationMatrix(eecsCsv.parseCSVFile("2013hurdat.csv"), inclist)
    print
    inclist1 = [1, 1, 1, 1, 1, 1, 1, 1]
    print diagnostics.correlationMatrix(eecsCsv.parseCSVFile("2013hurdat.csv"), inclist1)

    print
    print

#    username1 = raw_input("Enter your state: ")
#    username1 = username1.upper()
#    print username1


    print eecsCsvExtensionAge.parseCSVFile("age.csv")
    print
    print eecsCsvExtensionState.parseCSVFile("State.csv")

    def retrieveKeyList(dictionary, key):
        keylist = dictionary.keys()
        if key in keylist:
            return True
        else:
            return False

    print retrieveKeyList(dictionary1, "BARRY")
    print retrieveKeyList(dictionary1, "ANDREA")
    print retrieveKeyList(dictionary1, "barry")

    statedict = eecsCsvExtensionState.parseCSVFile("State.csv")
    agedict = eecsCsvExtensionAge.parseCSVFile("age.csv")
    print statedict
    print agedict

    print eecsCsv.retrieveValue(dictionary1, 'ANDREA', 0)







# DO NOT modify these 2 lines of code or you will be very sad
# Similarly, do not place any code below them
if __name__ == "__main__":
    main(sys.argv)