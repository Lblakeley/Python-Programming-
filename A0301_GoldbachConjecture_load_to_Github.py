##Lauren Blakeley
##I have not given or received any unauthorized assistance on this assignment.

#This code has been written to fulfill the requirements of assignment A0301. 


##The code for the function used to derive a list of prime numbers in the range (2,101) is based on the formula sieve of eratosthenes.
def primeValues(n):
 """
This code utilizes the Sieve of Eratosthenes to create a list of all prime numbers less than or equal to argument n.  
 """
 primes = [True] * (n+1) ##initializes a list that sets all values for (n+1) as True. Uses n+1 as range is exclusive for range end values.
 primes[0] = primes[1] = False ##sets both 0 and 1 as false in the primes list as 0 and 1 are not prime numbers and should definitely not be in the list.
 for i in range(2,int(n**.5)+1): ##uses for loop to iterate through all numbers from two to the square root of n.
     if primes[i]: ##stating that if a value is currently True and in the list primes[] (so all values up to n less 0 and 1 at this point)... 
       for j in range(i*i, n+1, i): ##for each prime number i, all multiples of i are marked as non-prime...
            primes[j] = False ##...by setting their location in the primes list to false.
 return[i for i in range(2, n+1) if primes[i]] ##filters out the False values from the primes list so only numbers set as True in the primes list are included.


def sumPrimes(prime_numbers,start_range,n):
   """
   This code checks all integers start_range through n to see if they can be formed through the sum of two primes.
   """
   for i in range(start_range,(n+1)):
      for num in prime_numbers: ##argument prime_numbers is defined in the main function but it is just a list of all prime values in set n.
          if num in primeValues(n+1) and (i-num) in primeValues(n+1): ##states that if a number is in the prime_values list and i(each of the integers we're testing) less num is also in that list...
             print(f"{i} = {num} + {i-num}") ##...print i = num + (i-num)
             break


def main(n,start_range):
 """
 This main function takes argument n- which is the largest value to be evaluated- and start_range- 
 which is the first integer to be tested against the Goldbach Conjecture.
 """
 primeValues(n)
 prime_numbers = list(primeValues(n)) ##local variable prime_numbers is derived from primeValues() function and passed into sumPrimes().
 sumPrimes(prime_numbers, start_range,n)
main(100,4)


##Observation
###Every integer 4-100 did not get printed. IE(97, 51, 11, etc.). This is where Goldbach's weak conjecture is relevant. There are odd 
###numbers that are equal to the sum of three primes but not two. Take 11. It is not the sum of two primes, but 3+3+5 = 11, which makes
###11 fall in line with Goldbach's weak conjecture but not Goldbach's Conjecture, or Goldbach's strong conjecture. 
        
            
         