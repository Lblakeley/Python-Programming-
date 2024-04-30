##Lauren Blakeley
##I have not given or received any unauthorized assistance on this assignment.

###This code is for Assignment 0102: Coprime.
###Two numbers are considered Coprime when the only factor they share is 1. Looking at all numbers, any two successive integers
    ###are always coprime, so I will use this fact to test my functions. 


###This first user-defined function is euclideanGCD(a,b). I broke up the coprime(a,b) function with this helper function that 
    ###uses a while loop to iterate over the factors of a and b until the remainder is 0 and the highest greatest common divisor is found. 
###The reason the function is named euclideanGCD(a,b) is because the logic in this function to find the GCD is based on the 
    ###Euclidean algorithm. a and b are in the parentheses of the function because they are required parameters.
###The function initiates a loop condition that persists until the value of b is equal to zero. The next line assigns a to the standing 
    ###value of b and b to the remainder of when a is divided by b- just as is done in the Euclidean algorithm.
    ###When b is equal to zero, that means the remainder of a and b is zero, and a is returned (and also printed) as it is the GCD.
###Because I created the euclideanGCD(a,b) helper function, I was able to test out many sets of values for a and b to make sure the 
    ###function worked properly before proceeding. 

def euclideanGCD(a,b):
    while b != 0:
        a, b = b, a % b
    print(a)
    return a


###The function coprime(a,b) needs to be written before the coprime_test_loop() function as it is passed into that function.
###Since I created the euclideanGCD(a,b) helper function first, it is very simple. This function is a one-way if statement 
    ###that says "if the euclideanGCD(a,b) function is equal to 1, print (and return) True. Otherwise, print and return False."
def coprime(a,b):
    if euclideanGCD(a,b) == 1:
        print(True)
        return True
    print(False)
    return False


###The coprime_test_loop() function features a while loop that prompts the user to enter two numbers, or to enter 0 if they wish to exit 
    ###the program. Selecting 0 causes the program to break, or stop. I chose 0 because 0 can never be coprime as it is a factorless number. 
###If the user does not select 0, this loop will continue on endlessly. The values are each converted to 
    ###class type integer when entered. Those numbers are denoted as variable a and b respectively, and are passed into the coprime(a,b)
    ###function where they are evaluated. If the function is evaluated to be true, a statement is printed that makes the user aware
    ###that the two numbers are coprime. However, if the function is returned as False, a statement is printed that states the values are not coprime.
def coprime_test_loop():
    while True or False:
        a = int(input('Please enter a number. Enter 0 if you wish to exit this program: '))
        if a == 0:
            print('The user has indicated that they wish to exit this program. Goodbye.')
            break
        b = int(input('Please enter a number. Enter 0 if you wish to exit this program: '))
        if  b == 0:
            print('The user has indicated that they wish to exit this program. Goodbye.')
            break
        elif coprime(a,b) == True:
            print(str(a)+' and '+str(b)+' are coprime.')
        elif coprime(a,b) == False:
            print(str(a)+' and '+str(b)+' are not coprime.')


coprime_test_loop()


