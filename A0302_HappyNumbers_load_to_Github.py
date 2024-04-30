##Lauren Blakeley
##I have not given or received any unauthorized assistance on this assignment.

#This code has been written to fulfill the requirements of assignment A0302. 

def happy_number(n):
    """
    This function is meant to look at all values of argument n to determine whether a value is happy or sad.
    """
    reviewed = set() ##this keeps track of the numbers that have been reviewed while determining if a number is happy or sad.
    while True:
        if n == 1: ##condition checks if n = 1.
            return True, [1] ##if n does equal 1, True is returned, as well as the value 1
        if n in reviewed: ##condition checks if n appears in the set reviewed already.
            return False, list(reviewed) ##if n in reviewed, the values are in a loop that will never reach 1. False is returned, so is a list of all values reviewed.
        reviewed.add(n) ##exists outside of the conditions. While True, n is added to the set reviewed.
        n = sum(int(digit)**2 for digit in str(n)) ##This line is where the calculation to determine whether a number is happy or sad occurs.
                                                   ###n is equal to each digit in string n, converted to an integer, squared and summed. 



def main():
    """
    The main function is responsible for creating a dictionary of values and their respective keys.
    This function also utilizes exception handling for ValueErrors in user input. 
    """
    dict = {} ##empty dictionary is created
    while True:
        input_val = input("Enter a positive number, or 'exit' if you wish to exit the program.: ") ##user must enter a positive integer.
        if input_val.lower() == 'exit': ##user may enter exit to leave program. .lower() handles if the user enters EXIT, or Exit, for instance. 
            print("The user wishes to exit the program. Goodbye")
            break ##code breaks if user exits.
        try: ##begin exception handling.
            val = int(input_val) ##string value entered by user is converted to integer and assigned to variable val.
            if val <= 0: ##if the value is less than or equal to 0, the user is prompte to enter a positive integer. 
                print("Please enter a positive integer.")
                continue ##loop continues. 
            is_happy_number, set_numbers = happy_number(val) ##calls happy_number() function to determine if the value is happy or sad.
            if is_happy_number: ##if the number is happy, print that it is a happy number and then print the list of values for n. Happy will just be [1].
                print(f"{val} is a happy number: {set_numbers}")
            else: ##If the number is not happy, it is sad. This else statement will print that the value entered is sad and then the list of all values of n.
                print(f"{val} is a sad number: {set_numbers}")
            dict[val] = ('happy' if is_happy_number else 'sad', set_numbers) ##Add the input value as the key and then whether happy or sad and the list of values of n associated with it as the values.
        except ValueError: ##if the user input was something like "nine", this would print to handle the value error.
            print("User input is invalid. Please enter a positive integer or 'exit' if you wish to leave the program.")
    print("Summing up the results:") ##After exiting the program, print summing up the results.
    print(dict) ##Then print the key, value pairs for all integers evaluated during the program run-time. 
main()
