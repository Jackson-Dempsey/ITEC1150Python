"""docstrings - JACKSON DEMPSEY - random number generator + adder, creates a user spesified count of numbers, and displays them back with some extra relevant information, such as the lowest number in the list, the highest number, and the combined total of the items in the list."""

import random 
#importing random so I can make sudo-random numbers

def main():
    #inputs - has the user give us some parameters to output a list of random numbers to us
    listForRandInts_inputs = inputs()
    #processing - has the list we grabbed from inputs have it's lowest number and it's highest number returned to us 
    minimumListVal_processing, maximumListVal_processing = processing(listForRandInts_inputs)
    #outputs - outputs this user list in all the diffrent fancy ways python can output a list, along with the min and max values calculated in processing
    outputs(listForRandInts_inputs, minimumListVal_processing, maximumListVal_processing)


    restart = input('Continue? Enter y or n: ')
    if restart == 'y':
            print('OK, let\'s make some more random numbers!')
            main()
    else:
            print('Dasvidaniya...')
    



def inputs():
    noOfIntegersToGenerate_inputs = int(input("How many random integers should be generated?"))
    while noOfIntegersToGenerate_inputs < -1 or noOfIntegersToGenerate_inputs % 1 != 0:
        #checks if the number is negative or a decimal by comparing the variable to -1 and using a modulo to find a non zero remainder (thus meaning its' a decimal)
        noOfIntegersToGenerate_inputs = int(input("please enter a positive number, non decimal number: "))

    maxSizeOfIntegersThatCanBeGenerated_inputs = int(input("What's the highest random integer you would like this program to be able to generate"))
    while maxSizeOfIntegersThatCanBeGenerated_inputs < -1 or maxSizeOfIntegersThatCanBeGenerated_inputs % 1 != 0:
        #checks if the number is negative or a decimal by comparing the variable to -1 and using a modulo to find a non zero remainder (thus meaning its' a decimal)
        maxSizeOfIntegersThatCanBeGenerated_inputs = int(input("please enter a positive number, non decimal number: "))

    listForRandInts_inputs = []
    
    for count in range(1,noOfIntegersToGenerate_inputs+1,1):
        #for loop which will repeatedly iterate the function to add random integers to our list
        # adding +1  to the end term in the range, because otherwise it won't iterate the final specified time (this still confuses me quite a bit...)
        listForRandInts_inputs.append(random.randint(1,maxSizeOfIntegersThatCanBeGenerated_inputs))

    listForRandInts_inputs.sort()

    return listForRandInts_inputs
        

def processing(userGeneratedRandomlist):

    #uses the min function on our list to find the smallest variable in our list, and then set it to a variable for later
    minimumListVal_processing = min(userGeneratedRandomlist)
    #same process, but for the largest variable
    maximumListVal_processing = max(userGeneratedRandomlist)

    return minimumListVal_processing, maximumListVal_processing

   
def outputs(userFinalList,userMinOfList,userMaxOfList):

    #list printed directly with the print statment
    print(f"Here are your {len(userFinalList)} random integers, sorted, in a list:")
    print(userFinalList)

    #printing list without brackets
    #using the join method to have each list item get printed in one single line with a ", " pasted behind each value
    #note that setting the x to str is needed because the .join method only takes strings 

    print("here they are, but without the default python list brackets:")
    print (", ".join([str(x) for x in userFinalList]))

    # addition loop
    
    print("here they are, added up:")

    loopSumnation = 0
    loopCount = 0

    for loopCount in range(len(userFinalList)):

        loopSumnation =+ userFinalList[loopCount]

        print(" +", loopSumnation, end="")

    print("=", sum(userFinalList))
    
         
         

    print(f"The smallest item in the list was {userMinOfList} and the largest was {userMaxOfList}")



main()