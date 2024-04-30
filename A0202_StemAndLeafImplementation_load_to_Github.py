##Lauren Blakeley
##I have not given or received any unauthorized assistance on this assignment.

#This code has been written to fulfill the requirements of assignment A0202. The structure of this code was 
#designed in 

##import matplotlib.pyplot to generate the stem-and-leaf plot in the createPlot(data, file) function.
import matplotlib.pyplot as plt

##This function's purpose is to greet the user and explain the purpose of the program.
def greetUser():
    """ 
    This function greets the user and informs them of the purpose of the program
    """

    print("Welcome! The purpose of this program is to generate and display a stem-and-leaf plot")
    print("based on the data associated with the file you (the user) selects.")
    print("You may select stem-and-leaf plots to view for as long as you would like.")
    print("When you wish to exit the program, enter '0'.")

##In this function, the file number entered is left as a string and not converted to type int or float as it is not a value which
##any operations would be performed on, since it is representative of which document should be selected.
##The file entered is returned to the computer.
def selectFile():
     """
     This function requests for the user to make a selection regarding which file they would like 
     to view a stem-and-leaf plot for. They are prompted to enter '1,2, or 3', or '0' if they wish to exit.
     """
     file = input('Please enter the number associated with which file you would like to view a stem-and-leaf plot for (1,2, or 3.) Select 0 to exit the program: ')
     return file 


##I created the if statement in this function to pass the three poetntial categories of file values entered into to determine whether
##the file is valid or not. A valid file in this case means that the loop will continue when a file in that catgeory is entered
##i.e. if a '3' is entered, the loop will continue after the relevant plot is produced.
##and if a number entered is a '6', the program will continue the loop after prompting the user to enter a valid selection (code below).
##However, if a user enters a '0', that means continueLoop will be false, which will be the selection that leads the program to 
##break in the main function.
def continueLoop(file):
        """
        This function is purposed to make the main function more organized. The file selected is read into the function as a parameter
        and if the value entered is anything but '0', it will signal that the loop should continue in the function. 
        However, if the value entered is '0', and this function returns a value of 'False', that will be the precursor for the 
        program to stop running.
        """
        if file not in ("0,1,2,3"):
            return True
        elif file in ("1,2,3"):
            return True
        elif file in ("0"):
             return False
        
##I created this function to keep my main function more organized. If the user makes a valid selection of '1','2',
##or '3', the associated file path is returned to the computer for further processing.
def filePath(file):
    """
    If a '1','2',or'3' is selected by the user, the relevant file path is stored and returned to the computer
    for further processing in the main function.
    """
    if file == '1':
        filepath = 'C:/Users/Lauren/OneDrive/Predictive Analytics/myenv/StemAndLeaf1.txt'
    elif file == '2':
        filepath = 'C:/Users/Lauren/OneDrive/Predictive Analytics/myenv/StemAndLeaf2.txt'
    elif file == '3':
        filepath = 'C:/Users/Lauren/OneDrive/Predictive Analytics/myenv/StemAndLeaf3.txt'
    return filepath

##This function reads in the data from the associated file stored in the variable filepath. It converts each line, or in this 
##case value to type float after stripping the white space. After iterating through each value,
##all of the values are stored in variable type data. Then, I sorted the data so that my stem-and-leaf plots 
##would look better when displayed. The sorted data is returned to the computer.
def readFile(filepath):
    """
    If a '1','2',or '3' is selected, this function will read the data from the respective value's filepath. It will strip the 
    white space for each line in the file and return the value as type float. Then, the data returned is sorted so that
    it is better organized before being formatted as a stem-and-leaf plot in the next step. The processed and sorted data is returned to 
    the computer.
    """
    with open(filepath, 'r') as file:
        data = [float(line.strip()) for line in file]
        data = sorted(data)
        return(data)
    

##This function is responsible for taking the data returned in the readFile(filepath) function and using it to generate a relevant 
##stem-and-leaf plot. For every value of x in the dataset "data", a stem is produced by dividing each float value by ten. The remainder
##becomes the leaf for each plot in the next step. Stems appear on the x-axis and Leaves on the y-axis. The 
##title is also customized depending on the dataset selected. As I was iterating through and looking at my plots I realized 
##this next level of customization was necessary to reduce confusion and add untility for the user. I added a grid for a similar 
##purpose in terms of being more organized visually. Finally, the plot is shown.
def createPlot(data,file):    
    """
    This is where the data read in is further processed into stems and leaves for the final stem-and-leaf plot. The plot
    is given appropriate labels and the title is even formatted to relay to the user which dataset ('1', '2', or '3') the plot
    shown is related to. Finally, the plot is produced and displayed.
    """    
    stems = [x/10 for x in data] 
    leaves =[x%10 for x in data]
    plt.stem(stems, leaves)
    plt.xlabel('Stems')
    plt.ylabel('Leaves')
    plt.title(f'Stem and Leaf Plot for dataset {file}' )
    plt.grid(True)  
    plt.show()
    
                
##This is the main function, where all of the functions come together to produce a final program. First, greetUser() runs.
##Next, the while loop runs that reads in the file value selected from selectFile(). If the file value selected is True for continueLoop(),
##there are two options. First, that the file value entered is not '1','2', or '3' and the user is informed that they did not make
##a valid selection and is prompted to enter a new value. Or, the file value entered is '1','2', or '3'. Then, the variable filepath
##is stored from the value returned from filePath(file), the variable data is stored from readFile(filepath), and a plot is created 
##from createPlot(data, file). However, if a '0' was entered, the function continueLoop() returns 'False', a message is printed
##to the user that they are exiting the function and 'break' ends the program. 
def main():
    """
    This is the main function, where all of the functions come together to produce a final program. 
    """
    greetUser()
    while True or False:
        file = selectFile()
        if continueLoop(file) == True:
            if file not in ("1,2,3"):
                print("User did not enter a valid selection. Please try again or select 0 to exit.")
            elif file in ('1,2,3'):
              data=readFile(filePath(file))
              createPlot(data, file)
        elif continueLoop(file) == False:
            print('The user wishes to exit the program. Goodbye.')
            break
main()
        

