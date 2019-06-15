import math 
from collections import Counter

#generate the sequence of primes, recursively
def prime_sequence():
    primes = [2]
    j = 3
    while j < 10**6:
        print(j)
        L = [j % p == 0 for p in primes] #boolean list 
        if any(L): #then not prime, i.e., has a prime factor other than itself
            j += 1 #increment 
        else: 
            primes.append(j) #then is prime. No smaller prime divides j
            j += 1 #increment 
        
    return primes

#find the last ten digits of this large non-Mersenne prime 
def large_prime():
    p = 28433*(2**7830457) + 1
    return p % 10**10

#find first triangular number that has over 500 divisors        
def triangular():
    j = 2
    while True:
        if numFactors(tri(j)) > 500:
            break
        j+= 1
    return tri(j)

      
#return 1 + 2 + ... + x
def tri(x):
    return int(x*(x + 1)/2)
#return how many numbers divide x (include 1 and x)   
def numFactors(x):
    L = [1 + i for i in primeExponents(x)]
    return listProduct(L)

#def return the prime exponents of a number in a list.
#e.g. 100 should return 2 and 2 because 100 = 2^2 * 5^2
def primeExponents(x):
    exponents = []
    y = Counter(primeFact(x)).values()
    return y 
    
def factors(x):
    f = []
    for i in range(1, x + 1):
        if x % i == 0:
            f.append(i)
    return f
            
#Naive: return the number of factors of (positive) integer x    
def naiveFactors(x):
    num_facts = 1 #1 to start because x divides itself 
    for i in range(1, int(x/2 + 1)):
        if x % i == 0:
            num_facts += 1
    
    return num_facts
            


#compute largest palindrome number that's a product of two 3 digit numbers 
def largest_palindrome():
    palindromes = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            if is_palindrome(i*j):
                palindromes.append(i*j)
        
            
    return max(palindromes)

#check if integer x is a palindrome
def is_palindrome(x):
    s = str(x)
    if s== s[::-1]:
        return True
    return False 
    

#compute the first ten digits of the sum of the large integers
#in the file euler_sum.txt
def large_sum():
    filename = 'euler_sum.txt'
    with open(filename, "r") as i:
        arr = []
        for line in i:
            arr.append(line)
    
    new_arr = []
    for j in arr:
        new_arr.append(int(j))
    
    s = str(sum(new_arr))[0:10]
    return int(s)
    
    



#return product of abc such that a^2 + b^2 = c^2
#and a + b + c = 1000. (a, b, c) is unique 
def pyth_triple():
    squares = []
    for i in range(1, 1000):
        for j in range(1, 1000):
            if square(i*i + j*j):
                squares.append((i, j, math.sqrt(i*i + j*j)))
                
    for k in range(len(squares)):
        if sum(squares[k]) == 1000:
            return squares[k][0]*squares[k][1]*squares[k][2]
    
                
            
#return if x is a perfect square
def square(x):
    root = math.sqrt(x)
    if root - int(root) == 0:
        return True
    return False 
    
    
#return product of elements in L
def list_product(L):
    prod = 1
    l = len(L)
    for i in range(l):
        prod *= L[i]
    return prod 
        
        


#return sum of the digits of 100 factorial 
def sum_100():
    f = factorial(100)
    return sum_digits(f)


#return factorial of x
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)

#find the first 1000 digit fibonnaci sequence, return its index in the fib seq
def fib1000():
    nums = [1, 1]
    j = 2
    while True:
        x = sum(nums[j - 2:j])
        if len(str(x)) == 1000:
            nums.append(x)
            break
        nums.append(x)
        j += 1  
    return len(nums) 
    



#return product of all primes less than x (let x be less than 2**13 for safety)
def primeFactorial(x):
    if x > 8500:
        print("this number is too large - enter a number less than or equal to 8500")
        return
    primes = [i for i in range(1, x + 1) if isprime(i)]
    return product(primes)
    

#return the product of all the numbers in list L 
def listProduct(L):
    if len(L) == 1:
        return L[0]
    else:
        return L[0] * listProduct(L[1:])
    
    

#return the sum of the digits of positive integer x
def sum_digits(x):
    digits = [int(i) for i in str(x)]
    return sum(digits)

#return the sum of the prime numbers smaller than x
def sumPrimes(x):
    L = [i for i in range(1, x) if isprime(i)]
    return sum(L)
    


#return the sum square difference of numbers up until x
def ssd(x):
    L = [i*i for i in range(1, x + 1)]
    sum_squared = sum(L)
    s = sum([i for i in range(1, x + 1)])
    squared_sum = s*s
    
    return squared_sum - sum_squared


#return LCM of a list of numbers, L
def lcmList(L):
    if not posInt(L):
        print("your list should only contain positive integers (no decimals)")
        return 
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
    
#return whether L only contains positive integers      
def posInt(L):
    for i in L:
        if type(i) != int or i < 1: 
            return False
    return True 
    
    

#lowest common multiple of two numbers
def lcm(x, y):
    return int(x * y / gcd(x, y))

#return gcd of two (positive) integers 
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
            
#return the prime factorization of x (in a list)
def primeFact(x):
    prime_factors = []
    if isprime(x):
        return [x] #x is prime
    elif isprime(math.sqrt(x)):
        return [math.sqrt(x), math.sqrt(x)] #prime power 
    i = 2
    while x > 1:
        if isprime(i) and x % i == 0:
            prime_factors.append(i)
            x = x/i #divide x by its prime factor
            while x % i == 0:
                prime_factors.append(i)
                x = x/i #divide x by this prime factor so long as it is divisible by it
        i += 1
        
    return prime_factors 
            
    
#return the largest prime factor of x
def largestFact(x):
    if isprime(x):
        return x
    primes = []
    for i in range(2, int(x/2) + 1):
        if isprime(i) and x % i ==0:
            primes.append(i)
    return max(primes)

#find smallest number divisible by each of the numbers from 1 to 20
def small():
    i = 2520 #the smallest num divisible by each of the numbers from 1 to 10
    while not divisible(i):
        print(i)
        i += 1
    return i 
        
    
def divisible(x):
    for i in range(2, 21):
        if x % i != 0: 
            return False
    return True 

#find the xth prime number 
def p(x):
    primes = []
    j = 2
    while True:
        if len(primes) >= x:
            break
        if isprime(j):
            primes.append(j)
        j += 1
    return primes[-1]
        

    
#returns whether x (an integer) is prime or not
def isprime(x):
    if type(x) != int:
        return False 
    elif x <= 1:
        return False 
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0: 
            return False 
    return True


#return sum of even fibonnaci numbers under 4 million 
def generateFib():
    nums = [1, 2]
    j = 2
    while True:
        x = sum(nums[j - 2:j])
        if x < 4000000:
            nums.append(x)
        else: 
            break
        j += 1
    
    even = [i for i in nums if i%2 == 0]
    return sum(even)
        


#return sum of multiples of 3 and 5 under 1000 
def div(): 
    s = []
    for i in range(1,1000): 
        if i % 3 == 0 or i % 5 ==0:
            s+=[i]
    return sum(s)
            
    
