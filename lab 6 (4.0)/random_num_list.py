"""docstrings - JACKSON DEMPSEY - random number game"""

import random 
#importing random for the time being, if i have to redo this code later so be it...

def main():
    input()

##restarting loop code to put in later
    #restart = input('Continue? Enter y or n: ')
    #if restart == 'y':
            #print('OK, let\'s calculate volume of another box.')
            #main()
    #else:
            #print('Thanks for using the program.')
    



def inputs():
    noOfIntegersTogenerate_inputs = int(input("How many random integers should be generated?"))
    if noOfIntegersTogenerate_inputs < -1 or beginingNumber % 1 != 0:
        #checks if the number is negative or a decimal by comparing the variable to -1 and using a modulo to find a remainder
        noOfIntegersTogenerate_inputs = int(input("please enter a positive number, non decimal number: "))


#def processing():
   
#def outputs():



main()