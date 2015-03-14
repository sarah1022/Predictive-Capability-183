# Authors: Hallie Wiese, Ben Segal, Sarah Brock, Shao-Kai Lai
# uniqnames: hamawies, bensegal, mathwhiz, sklai
# Date: 12/5/2014
# Purpose: Generate sample numbers at random from a probability distribution given its CDF.
# Description: Implementation of uniformGen, generateFromBernoulli, generateFromBinomial, generateFromGeometric,
#              generateFromUniform, generateFromExponential, and generateFromNormal functions.

import sys
import random
import math

"""
Requires: nothing
Modifies: nothing
Effects: generates numbers randomly from a Uniform(0,1) distribution

This function is implemented for you.
"""
def uniformGen():
    return random.random()


"""
Requires: seed is a value generated from a Uniform(0,1) distribution
          p is the probability of success
Modifies: nothing
Effects: returns a randomly generated value from a Bernoulli(p) distribution,
    using the inverse method described in the spec
"""
def generateFromBernoulli(seed, p):
    if seed <= (1 - p):
        return 0
    else:
        return 1


"""
Requires: seed is a value generated from a Uniform(0,1) distribution
		  p is the probability of success
		  n is the number of trials
Modifies: nothing
Effects: returns a randomly generated value from a Binomial(n,p) distribution,
	using the inverse method described in the spec
"""
def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

def generateFromBinomial(seed, n, p):
    choose = 0
    value1 = 0.0
    while choose <= n:
        number = (factorial(n) / (factorial(n - choose) * factorial(choose))) * pow(p, choose) * pow((1 - p), (n - choose))
        value1 += number
        if seed <= value1:
            return choose
        else:
            choose += 1


"""
Requires: seed is a value generated from a Uniform(0,1) distribution
		  p is the probability of success
Modifies: nothing
Effects: returns a randomly generated value from a Geometric(p) distribution,
	using the inverse method described in the spec
"""
def generateFromGeometric(seed, p):
    X = int(math.ceil((math.log(1 - seed, math.e)/(math.log(1 - p)))))
    return X

"""
NOTE FOR THE FOLLOWING TWO FUNCTIONS: You WILL lose points on the bare-bones
	portion of the project if you simply make a call to the corresponding
	function in the random library. The idea is that everyone gains an
	understanding of how to write code to analyze data, and these distributions
	are the easiest implementations of the inverse method for continuous random
	variables.
"""

"""
Requires: seed is a value generated from a Uniform(0,1) distribution
		  a is the beginning of the interval
		  b is the end of the interval
Effects: returns a randomly generated value from a Uniform(a,b) distribution,
	using the inverse method described in the spec
"""
def generateFromUniform(seed, a, b):
    X = a + (b - a) * seed
    return X

"""
Requires: seed is a value generated from a Uniform(0,1) distribution
          ld (lambda) is the rate at which the distribution decays
Modifies: nothing
Effects: returns a randomly generated value from a Exponential(ld) distribution,
    using the inverse method described in the spec
"""
def generateFromExponential(seed, ld):
    X = (-1.0 / ld) * math.log(1 - seed, math.e)
    return X

"""
Generating from a normal distribution in a non-hacky way is nearly impossible,
so we provide you with a function that calls the library for you.

Requires: mu is the mean of the distribution
		  sigma is the standard deviation of the distribution
Effects: Returns a randomly generated sample from a Normal(mu, sigma)
	distribution
"""
def generateFromNormal(mu, sigma):
    return random.gauss(mu, sigma)


"""
The following function is not required, but your dataset may need you to
implement it. If you would like to implement it, remove the "pass" statement
and implement your function as normal.
"""

"""
Requires: seed is a value generated from a Uniform(0,1) distribution
          ld (lambda) is the approximation of n*p from the Binomial(n,p)
             distribution
Modifies: nothing
Effects: returns a randomly generated value from a Poisson(ld) distribution,
	using the inverse method described in the spec
"""
def generateFromPoisson(seed, ld):
    pass

