# Authors: Hallie Wiese, Ben Segal, Sarah Brock, Shao-Kai Lai
# uniqnames: hamawies, bensegal, mathwhiz, sklai
# Date: 12/5/2014
# Purpose: To test the functions in our other files (diagnostics.py, eecsCsv.py, generation.py, and measures.py).
# Description:

import sys
import eecsCsv
import generation
import measures
import diagnostics
import eecsCsvExtensionAge
import eecsCsvExtensionState
import random


"""
Use this function for your testing for bare-bones, and then use it as the driver
for your project extension
"""


def main(argv):
    statedict = eecsCsvExtensionState.parseCSVFile("State.csv")
    agedict = eecsCsvExtensionAge.parseCSVFile("age.csv")

    userstate = raw_input("ENTER THE STATE IN WHICH YOU LIVE: ")
    userstate = userstate.upper()

    if eecsCsvExtensionState.retrieveKeyListState(statedict, userstate):
        years = eecsCsvExtensionState.retrieveEntireAttributeState(statedict, userstate, 1)
        deathrate = eecsCsvExtensionState.retrieveEntireAttributeState(statedict, userstate, 2)
        yearsMean = measures.mean(years)
        deathrateMean = measures.mean(deathrate)
        varYears = measures.variance(years)

        B1 = (4.0/5.0) * (diagnostics.singlePopulationCovariance(years, deathrate, yearsMean, deathrateMean) / varYears)
        B0 = deathrateMean - (B1 * yearsMean)

        staterate = (B0 + 2015 * B1) / 10.0
        print "YOUR LIKELIHOOD OF DEATH FROM LIVING IN", userstate, "IS {0}% IN 2015!!".format(staterate)
        print

    else:
        print "ERROR!! STATE NOT IDENTIFIED: FINDING AVERAGE OF UNITED STATES..."
        USyears = eecsCsvExtensionState.retrieveEntireAttribute(statedict, 1)
        USdeathrate = eecsCsvExtensionState.retrieveEntireAttribute(statedict, 2)
        USyearsMean = measures.mean(USyears)
        USdeathrateMean = measures.mean(USdeathrate)
        USvarYears = measures.variance(USyears)

        B1 = (4.0/5.0) * (diagnostics.singlePopulationCovariance(USyears, USdeathrate, USyearsMean, USdeathrateMean) / USvarYears)
        B0 = USdeathrateMean - (B1 * USyearsMean)

        staterate = (B0 + 2015 * B1) / 10.0
        print "YOUR LIKELIHOOD OF DEATH WHILE LIVING IN THE UNITED STATES IS {0}% IN 2015!!".format(staterate)
        print
        userstate = "MICHIGAN"



    userAGE = raw_input("ENTER YOUR CURRENT AGE (ENTER IN NUMERIC FORM): ")

    if ('1' <= userAGE <= '4'):
        AGE = int(userAGE)
        userAGE = 'ageonetofour'
    elif ('5' <= userAGE <= '14'):
        AGE = int(userAGE)
        userAGE = 'agefivetofourteen'
    elif ('15' <= userAGE <= '24'):
        AGE = int(userAGE)
        userAGE = 'agefifteentotwentyfour'
    elif ('25' <= userAGE <= '34'):
        AGE = int(userAGE)
        userAGE = 'agetwentyfivetothirtyfour'
    elif ('35' <= userAGE <= '44'):
        AGE = int(userAGE)
        userAGE = 'agethirtyfivetofortyfour'
    elif ('45' <= userAGE <= '54'):
        AGE = int(userAGE)
        userAGE = 'agefortyfivetofiftyfour'
    elif ('55' <= userAGE <= '64'):
        AGE = int(userAGE)
        userAGE = 'agefiftyfivetosixtyfour'
    elif ('65' <= userAGE <= '74'):
        AGE = int(userAGE)
        userAGE= 'agesixtyfivetoseventyfour'
    elif ('75' <= userAGE <= '84'):
        AGE = int(userAGE)
        userAGE = 'ageseventyfivetoeightyfour'
    elif ('85' <= userAGE <= '120'):
        AGE = int(userAGE)
        userAGE = 'ageeightyfiveandover'
    else:
        print 'ERROR: NOT A VALID ANSWER!! PROGRAM RANDOMIZING AGE...'
        for rand in range(1):
            userAGE = random.randint(1, 99)
            AGE = userAGE
            userAGE = str(userAGE)
            print 'USER RANDOMIZED AGE: {0}!'.format(userAGE)
            if ('1' <= userAGE <= '4'):
                userAGE = 'ageonetofour'
            elif ('5' <= userAGE <= '14'):
                userAGE = 'agefivetofourteen'
            elif ('15' <= userAGE <= '24'):
                userAGE = 'agefifteentotwentyfour'
            elif ('25' <= userAGE <= '34'):
                userAGE = 'agetwentyfivetothirtyfour'
            elif ('35' <= userAGE <= '44'):
                userAGE = 'agethirtyfivetofortyfour'
            elif ('45' <= userAGE <= '54'):
                userAGE = 'agefortyfivetofiftyfour'
            elif ('55' <= userAGE <= '64'):
                userAGE = 'agefiftyfivetosixtyfour'
            elif ('65' <= userAGE <= '74'):
                userAGE= 'agesixtyfivetoseventyfour'
            elif ('75' <= userAGE <= '84'):
                userAGE = 'ageseventyfivetoeightyfour'
            else:
                userAGE = 'ageightyfiveandover'
    print


    userGender = raw_input("ENTER YOUR GENDER (ENTER '1' IF MALE, ENTER '2' IF FEMALE): ")
    if (userGender != '1') and (userGender != '2'):
        print 'ERROR: USER INPUT NOT VALID!! PROGRAM RANDOMIZING GENDER...'
        rs = random.sample([1, 2], 1)
        userGender = rs[0]
        if userGender == 1:
            userGender = '1'
            print 'USER GENDER IS RANDOMIZED TO MALE'
        else:
            userGender = '2'
            print 'USER GENDER IS RANDOMIZED TO FEMALE'
    print


    userRace = raw_input("ENTER YOUR RACE (ENTER 1 IF WHITE, ENTER 2 IF BLACK, ENTER 3 IF ASIAN OR PACIFIC ISLANDER, ENTER 4 IF AMERICAN INDIAN, ESKIMO NEUT, OR OTHER: ")
    if (userRace != '1') and (userRace != '2') and (userRace != '3') and (userRace != '4'):
        print 'ERROR: USER INPUT NOT VALID!! PROGRAM RANDOMIZING... '
        rss = random.sample([1, 2, 3, 4], 1)
        userRace = rss[0]
        if userRace == 1:
            userRace = '1'
            print 'RACE RANDOMIZED TO WHITE'
        elif userRace == 2:
            userRace = '2'
            print 'RACE RANDOMIZED TO BLACK'
        elif userRace == 3:
            userRace = '3'
            print 'RACE RANDOMIZED TO ASIAN OR PACIFIC ISLANDER'
        else:
            userRace = '4'
            print 'RACE RANDOMIZED TO AMERICAN INDIAN, ESKIMO NEUT, OR OTHER CATEGORY'
    print

    userGenRace = 0
    if userGender == '1':
        GENDER = 'MALE'
        if userRace == '1':
            RACE = 'WHITE'
            userGenRace = 3
        elif userRace == '2':
            RACE = 'BLACK'
            userGenRace = 4
        elif userRace == '3':
            RACE = 'ASIAN OR PACIFIC ISLANDER'
            userGenRace = 5
        else:
            RACE = 'AMERICAN INDIAN, ESKIMO NEUT, OR OTHER CATEGORY'
            userGenRace = 6
    else:
        GENDER = 'FEMALE'
        if userRace == '1':
            RACE = 'WHITE'
            userGenRace = 7
        elif userRace == '2':
            RACE = 'BLACK'
            userGenRace = 8
        elif userRace == '3':
            RACE = 'ASIAN OR PACIFIC ISLANDER'
            userGenRace = 9
        else:
            RACE = 'AMERICAN INDIAN, ESKIMO NEUT, OR OTHER CATEGORY'
            userGenRace = 10


    if eecsCsvExtensionAge.retrieveKeyListAge(agedict, userAGE):
        yearsAge = eecsCsvExtensionState.retrieveEntireAttributeState(agedict, userAGE, 1)
        deathrateAge = eecsCsvExtensionAge.retrieveEntireAttributeAge(agedict, userAGE, userGenRace)
        yearsAgeMean = measures.mean(yearsAge)
        deathrateAgeMean = measures.mean(deathrateAge)
        varYearsAge = measures.variance(yearsAge)

        B1age = (5/6) * (diagnostics.singlePopulationCovariance(yearsAge, deathrateAge, yearsAgeMean, deathrateAgeMean) / varYearsAge)
        B0age = deathrateAgeMean - (B1age * yearsAgeMean)

        agerate = (B0age + (2015 * B1age)) / 1000.0
        print 'BASED ON YOUR AGE: {0}, GENDER: {1}, AND RACE: {2}'.format(AGE, GENDER, RACE)
        print 'YOUR LIKELIHOOD OF DEATH IS {0}% IN 2015!!'.format(agerate)
        print

    agecount = 12
    statecount = 5
    deathlist = []
    while agecount <= 20:
        an = eecsCsvExtensionAge.retrieveValue(agedict, userAGE, 4)
        ah = an[agecount]
        sn = eecsCsvExtensionState.retrieveValue(statedict, userstate, 3)
        sh = sn[statecount]
        death = ((ah + sh)/2.0) / 100.0
        deathlist.append(death)
        agecount += 1
        statecount += 1

    print 'USING THE USER AGE INPUT AND STATE INPUT SOME OF THE TOP POSSIBLE CAUSES OF DEATH ARE:'
    print "THE LIKELIHOOD OF DYING FROM A HEART DISEASE WITHIN THE NEXT YEAR IS {0}%!!!".format(deathlist[0])
    print "THE LIKELIHOOD OF DYING FROM MALIGNANT NEOPLASM WITHIN THE NEXT YEAR IS {0}%!!!".format(deathlist[1])
    print "THE LIKELIHOOD OF DYING FROM CEREBROVASCULAR DISEASE WITHIN THE NEXT YEAR IS {0}%!!!".format(deathlist[2])
    print "THE LIKELIHOOD OF DYING FROM A CHRONIC LOWER RESPIRATORY DISEASE WITHIN THE NEXT YEAR IS {0}%!!!".format(deathlist[3])
    print "THE LIKELIHOOD OF DYING FROM AN ACCIDENT [GENERALIZED] WITHIN THE NEXT YEAR IS {0}%!!!".format(deathlist[4])
    print "THE LIKELIHOOD OF DYING FROM ALZHEIMER'S DISEASE  WITHIN THE NEXT YEAR IS {0}%!!!".format(deathlist[5])
    print "THE LIKELIHOOD OF DYING FROM DIABETES MELLITUS WITHIN THE NEXT YEAR IS {0}%!!!".format(deathlist[6])
    print "THE LIKELIHOOD OF DYING FROM A FORM OF INFLUENZA OR PNEUMONIA, WITHIN THE NEXT YEAR IS {0}%!!!".format(deathlist[7])
    print "THE LIKELIHOOD OF DYING FROM SUICIDE WITHIN THE NEXT YEAR IS {0}%!!!".format(deathlist[8])

    return



if __name__ == "__main__":
    main(sys.argv)



