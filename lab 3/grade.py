"""docstring"""
## Jackson Dempsey - Grade Calculator ##

score = input('Enter quiz score – whole number 0-100: ')
# validation block - checking if the user is both putting in a whole number, AND a number that's between 1 and 100 
if score.isnumeric() is False:
    print('Please input again, this program will only take whole numbers')
elif int(score) > 100 and int(score)<=0:
    print('Please input again, this calculator will only take scores from 1 to 100')

else:

    ##runs the rest of the program, running through the else ifs if it can't match the score to the inital if

    score = int(score)
    if score >= 90: print('Grade: A')
    elif score >= 80: print('Grade: B')
    elif score >= 70: print('Grade: C')
    elif score >= 60: print('Grade: D')
    elif score >= 50: print('Grade: F')
    else: print("Grade: F")


## another if statement used to check if the score is passable, (i'm assuming a D is passible?)

if int(score) >= 60:
    print("This is a passing grade.")

else: 
    print("This is NOT a passing grade.")





    