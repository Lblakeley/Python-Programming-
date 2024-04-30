##Lauren Blakeley
##I have not given or received any unauthorized assistance on this assignment.

###This code is for Assignment 0101: Grading Logic. Each bullet, or criteria, for grading will receive its own 
    ###helper function, as shown by the professor in the 'Discuss A0101' section in D2L for the course. This approach emphasizes
    ##the importance of modular coding,
    ###Once each helper function is generated, use them to generate the computeGrade() function. 
###Because each of the helper functions are so small, and the comments looked very cluttered next to each corresponding line, 
    ###all comments for each function below can be found directly above.
###A note I address in my YouTube video- I would like to write code to handle errors in entering invalid inputs (exception-handling)
    ###into each helper function. However, I do not want to overcomplicate the first assignment so I left it out to follow instructions more closely. 
###As a final initial note, I followed camelCase for my naming conventions as it has been my preference since I began coding in Python.
    


###This function is based off of bullet point #1 in assignment A0101. This function is meant to address whether or not the student
    ###submitted the correct file type, a single uncompressed .py file, when they submitted their assignment.
###fileStatus asks the user to enter yes or no as to whether or not the student submitted a single, uncompressed.py file. 
    ###I implemented the built-in Python method '.lower()' to convert all strings in the yes or no answer to lowercase, 
    ###so that the if statement that follows can handle the input more easily.
###The two-way if statement serves two purposes, one for the user and one for the computer. In this case, if the user enters that the 
    ###student did submit the correct file type, the terminal prints that the student earned credit for the section. While this is what 
    ###is printed for the human user, on the computer's end, the computer stores a value of true since that is what is returned. 
    ###However, if the student did not submit the correct file type, the terminal prints that the student earned no points for the assignment and 
    ###specifies the reason. The value that is returned is false.
###Returning true or false (boolean values) for the helper functions makes the main function, computeGrade(), simpler to write.

def correctFile():
      fileStatus = input('Did the student submit their assignment using the correct file type (a single uncompressed .py file)? (Enter yes or no): ').lower()  ###asks user for input as to whether the student submitted the correct file type.
      if fileStatus in ('yes'):  
        print( 'Yes, they earned credit for this section.')
        return True
      else:
        print('No, they earned zero points for this assignment for not submitting the correct file type.')
        return False
    

###This function is based off of bullet point #2 in assignment A0101. This function is meant to address whether or not the student
    ###included their name in their submission.
###nameStatus asks the user to enter yes or no as to whether or not the student included their name in their submission.
    ###I implemented the built-in Python method .lower() to convert all strings in the yes or no answer to lowercase, 
    ###so that the if statement that follows can handle the input more easily.
###The two-way if statement serves two purposes, one for the user and one for the computer. In this case, if the user enters that the 
    ###student did include their name in their submission, the terminal prints that the student earned credit for the section. While this is what 
    ###is printed for the human user, on the computer's end, the computer stores a value of true since that is what is returned. 
    ###However, if the student did not include their name, the terminal prints that the student earned no points for the assignment and 
    ###specifies the reason. The value that is returned is false.
###Returning true or false (boolean values) for the helper functions makes the main function, computeGrade(), simpler to write.
def includesName():
      nameStatus = input('Did the student include their name in their submission? (Enter yes or no): ').lower()
      if nameStatus in ('yes'):
        print( 'Yes, they earned credit for this section.')
        return True
      else:
        print('No, they earned zero points for this assignment for not including their name in their submission.')
        return False
         

###This function is based off of bullet point #3 in assignment A0101. This function is meant to address whether or not the student
    ###included the Honor Statement in their submission.
###honorStatementStatus asks the user to enter yes or no as to whether or not the student included their name in their submission.
    ###I implemented the built-in Python method .lower() to convert all strings in the yes or no answer to lowercase, 
    ###so that the if statement that follows can handle the input more easily.
###The two-way if statement serves two purposes, one for the user and one for the computer. In this case, if the user enters that the 
    ###student did include the Honor Statement in their submission, the terminal prints that the student earned credit for the section. While this is what 
    ###is printed for the human user, on the computer's end, the computer stores a value of true since that is what is returned. 
    ###However, if the student did not include the Honor Statement, the terminal prints that the student earned no points for the assignment and 
    ###specifies the reason. The value that is returned is false.
###Returning true or false (boolean values) for the helper functions makes the main function, computeGrade(), simpler to write.
def includesHonorStatement():
      honorStatementStatus = input('Did the student include the honor statement in their submission? (Enter yes or no): ').lower()
      if honorStatementStatus in ('yes'):
        print( 'Yes, they earned credit for this section.')
        return True
      else:
        print('No, they earned zero points for this assignment for not including the honor statement in their submission.')
        return False
         

###This function is based off of bullet point #4 in assignment A0101. This function is meant to address whether or not the student
    ###included a link to their YouTube presentation of the code in their submission.
###presentationLinkStatus asks the user to enter yes or no as to whether or not the student included their name in their submission.
    ###I implemented the built-in Python method .lower() to convert all strings in the yes or no answer to lowercase, 
    ###so that the if statement that follows can handle the input more easily.
###The two-way if statement serves two purposes, one for the user and one for the computer. In this case, if the user enters that the 
    ###student did include a link to their YouTube presentation of the code in their submission, the terminal prints that the student earned credit for the section. While this is what 
    ###is printed for the human user, on the computer's end, the computer stores a value of true since that is what is returned. 
    ###However, if the student did not include a link to their presentation, the terminal prints that the student earned no points for the assignment and 
    ###specifies the reason. The value that is returned is false.
###Returning true or false (boolean values) for the helper functions makes the main function, computeGrade(), simpler to write.
def includesPresentationLink():
      presentationLinkStatus = input('Did the student include a link to an unlisted 3-minute YouTube video presenting the code and answering the assigned questions? (Enter yes or no): ').lower()
      if presentationLinkStatus in ('yes'):
        print( 'Yes, they earned credit for this section.')
        return True
      else:
        print('No, they earned zero points for this assignment for not including a link to their YouTube video presenting the code and answering the assigned questions.')
        return False
         
###There is a fifth bullet point with 4 sub-bullet points that address each of the 4 ways students are graded as long as they met the above conditions.
      ###I created 4 additional helper functions, each based on one of the sub-bullet points, to make it easier to compute the final grade
      ###in the main function. These four helper functions are as follows:

###codeCorrectness asks the user to enter a number, out of ten, that accurately assesses the correctness of the student's code. 
      ###I converted the entered value into an integer, as nothing in the assignment indicated a float type would be more accurate.
      ###If it was made clear that decimal points could be entered, such as 9.5, I would have made this a float type. However, 
      ###with nothing to indicate otherwise, I assumed whole number integers would look neater.
###I printed the value entered by the user and converted to an integer so that the user could quickly and easily see if they entered
      ###an incorrect value (like 50 instead of 5). These functions would also benefit from exception-handling for this reason. 
###Finally, I wrote for the function to return the same value printed, the variable correctnessOfCode.      
def codeCorrectness():
    correctnessOfCode = int(input('Out of ten points, how would you evaluate the correctness of the code? : '))
    print(correctnessOfCode)
    return correctnessOfCode


###codeElegance asks the user to enter a number, out of ten, that accurately assesses the elegance of the student's code. 
      ###Again, I converted the entered value to an integer, this time in the variable eleganceOfCode.
###I printed the value entered by the user and converted to an integer so that the user could quickly and easily see if they entered
      ###an incorrect value (like 50 instead of 5). These functions would also benefit from exception-handling for this reason. 
###Finally, I wrote for the function to return the same value printed, the variable eleganceOfCode. 
def codeElegance():
    eleganceOfCode = int(input('Out of ten points, how would you evaluate the elegance of the code?: '))
    print(eleganceOfCode)
    return eleganceOfCode


###codeHygiene asks the user to enter a number, out of ten, that accurately assesses the hygiene of the student's code. 
      ###Again, I converted the entered value to an integer, this time in the variable hygieneOfCode.
###I printed the value entered by the user and converted to an integer so that the user could quickly and easily see if they entered
      ###an incorrect value (like 50 instead of 5). These functions would also benefit from exception-handling for this reason. 
###Finally, I wrote for the function to return the same value printed, the variable hygieneOfCode. 
def codeHygiene():
    hygieneOfCode = int(input('Out of ten points, how would you evaluate the hygiene of the code?: '))
    print(hygieneOfCode)
    return hygieneOfCode

###discussionQuality asks the user to enter a number, out of ten, that accurately assesses the quality of the discussion in the student's video. 
      ###Again, I converted the entered value to an integer, this time in the variable qualityOfDiscussion.
###I printed the value entered by the user and converted to an integer so that the user could quickly and easily see if they entered
      ###an incorrect value (like 50 instead of 5). These functions would also benefit from exception-handling for this reason. 
###Finally, I wrote for the function to return the same value printed, the variable qualityOfDiscussion. 
def discussionQuality():
    qualityOfDiscussion = int(input('Out of ten points, how would you evaluate the quality of the discussion?: '))
    print(qualityOfDiscussion)
    return qualityOfDiscussion

###This final helper function addresses the last bullet point- handling late assignments. For every hour an assignment is late,
    ###a student loses 1% of their total possible score. I knew when writing this function I would want to multiply the total grade
    ###a student earns by this factor, Meaning, I would want this value to be 1 if the assignment is not late, and 0 if it is 100 hours late.
###My assumption is that the professor stops accepting late assignments by 100 hours- or else I would write a statement saying if
###numberOfHoursLate is more than 100, return 0, else:
def hoursLate():
    numberOfHoursLate = int(input('How many hours late was the assignment?: '))
    print((100-numberOfHoursLate)/100)
    return((100-numberOfHoursLate)/100)


###This is where all of the individual helper functions come together to assess a student's grade for an assignment. 
###If no is entered for any of the first four functions, the code immediately stops and a 0 is both printed to the terminal and
    ###returned to the computer. 
###If yes is entered for the first four questions, the grade is computed by asking for how many hours late the submission was, 
    ###Then the scores, out of ten, for codeCorrectness, codeElegance, codeHygiene, and discussionQuality. Those four scores are added together
    ###before being multiplied by the factor returned for how many hours late the submission is, if late at all. 
###The final calculated grade is assigned to variable grade, which is stored as a float type. I did not reassign this value to int as, 
    ###since all other numeric types are assigned to int, the final product should be an integer. 
###I returned the grade to the computer but printed a statement that says "This student scored (grade) points out of 40 possible points."
    ###I chose to print that statement to make it more comprehensive for the user. I had to convert the grade to string type in the print
    ###statement to get the statement to populate in the terminal.
def computeGrade():
    if correctFile() is False:
        print(0)
        return 0
    if includesName() is False:
        print(0)
        return 0
    if includesHonorStatement() is False:
        print(0)
        return 0
    if includesPresentationLink() is False:
        print(0)
        return 0
    else:
        grade = ((hoursLate() * (codeCorrectness() + codeElegance() + codeHygiene() + discussionQuality())))
        print('This student scored '+str(grade)+' points out of 40 possible points')
        return(grade)
computeGrade()

