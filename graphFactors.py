#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import math 
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
"""
Created on Tue Dec 25 08:09:50 2018

@author: Will Morgan
"""
upTo = 100 #change this constant around for higher upper bound


#greatest common divisor of two (positive) integers
def gcd(x, y):
    if x == y:
        return x
    elif x > y: 
        if x % y == 0:
            return y
        else:
            g = 1
            for i in range(2, y):
                if x % i == 0 and y % i == 0:
                    g = i
            return g 
    else:
        return gcd(y, x)

#lowest common multiple
def lcm(x, y):
    return int(x * y / gcd(x, y))

def lcmList(L):
    
    l = len(L)
    if l < 2:
        print("the list of numbers should have two or more elements")
        return 
    elif l == 2:
        return lcm(L[0], L[1])
    else: 
        k = lcm(L[0], L[1])
        for i in range(2, l):
            k = lcm(L[i], k)
        return k 
    
def plotLcm(L):
    num = max(L)
    lcms = [lcmList(L)]
    plt.scatter(num, lcms)
    plt.show()



def isprime(x):
    if x <= 1:
        return False 
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0: 
            return False 
    return True



primes = [i for i in range(1, upTo + 1) if isprime(i)]

primeLength = len(primes) - 1


#return the value of the prime exponents for x's prime factorization 
def primeExponents(x):
   return Counter(primeFact(x)).values()

#return how many positive integers divide positive integer x 
def numFactors(x):
    L = [1 + i for i in primeExponents(x)]
    return listProduct(L)

def listProduct(L):
    prod = 1
    l = len(L)
    for i in range(l):
        prod *= L[i]
    return prod 


#return prime factors of integer x
def primeFact(x):
    prime_factors = []
    if isprime(x):
        return [x] #x is prime so return
    i = 0
    while x > 1:
        if i > primeLength or primes[i] > primeLength:
            break
        elif x % primes[i] == 0:
            prime_factors.append(primes[i])
            x = x/primes[i] #divide x by its prime factor
            while x % primes[i] == 0:
                prime_factors.append(primes[i])
                x = x/primes[i] #divide x by this prime factor so long as it is divisible by it
        i += 1
        
    return prime_factors 

def plotDiv(x):
    nums = [i for i in range(1, x + 1)]
    y = [numFactors(nums[j]) for j in range(0, x)]
    plt.semilogx(nums, y, 'bo', markersize = 1)
    plt.xlabel('numbers')
    plt.ylabel('number of factors')
    plt.title('Divisibility of integers')
    plt.show()
    
plotDiv(upTo)
        
