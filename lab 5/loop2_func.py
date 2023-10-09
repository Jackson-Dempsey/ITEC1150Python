"""docstring JACKSON DEMPSEY 10/3, redesign of the "loop 2" program, a number counter, using MIPO design (main, input, processing, outputs) """

# The Main part, which executes all the things we've created in the bottom IPO part

def main():

    #these two lines refrence the variables which the inputs and processing functions "returned" to us below
    beginingNumber, endingNumber = inputs()
    userCountingTrack = processing(beginingNumber, endingNumber)

    outputs(userCountingTrack) #outputs here is essentially a fancy print statment, since that function only has a print statement inside it

# IPO part, where main gets it's stuff to do

def inputs():

    print("what number do you want to start with?")
    beginingNumber = int(input("enter a whole number greater than 0: "))
    if beginingNumber < -1 or beginingNumber % 1 != 0:
        #checks if the number is negative or a decimal by comparing the variable to -1 and using a modulo to find a remainder
        beginingNumber = int(input("please enter a positive number, non decimal number: "))

    else:
        pass

    print("what number do you want to end with?")
    endingNumber = int(input("enter a whole number greater than 0: "))
    if endingNumber < -1 or endingNumber % 1 != 0:
        #checks if the number is negative or a decimal by comparing the variable to -1 and using a modulo to find a remainder
        endingNumber = int(input("please enter a positive number, non decimal number: "))

    else:
        pass

    if beginingNumber == endingNumber:
        print("these two numbers should be diffrent, you can't count the two same numbers")
        exit()

    return beginingNumber, endingNumber


def processing(startNumber,endNumber):

    userCountingTrack = 0

    if startNumber < endNumber:
        stepDirectonIndicator = 1
    else:
        stepDirectonIndicator = 1


    #this prints the intial value stored in start number before the for loop modifies it

    for count in range(startNumber-1,endNumber,stepDirectonIndicator): #this code then will repeatedly iterate the following untill it reaches the specified end number:

        print(startNumber) #then print the current value stored in userBeginningNumber, before repeating again
        #the argument for startnumber is subtracted by one in order to offset the adding done and include all the numbers counted toghter

        startNumber += 1 #it will add one to the the value stored in userBeginingNumber

        userCountingTrack += startNumber #it will add the sum of the current value of userBeginingNumber to userCountingTrack


    return userCountingTrack

def outputs(outputNumber):

    print("the sum of the numbers is:")
    print(outputNumber)
    
main()