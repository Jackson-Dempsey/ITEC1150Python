"""docstring JACKSON DEMPSEY 10/3, redesign of the "loop 2" program, a number counter, using MIPO design (main, input, processing, outputs) """

## The Main part, which executes all the things we've created in the bottom IPO part

def main():



    #these two lines refrence the variables which the inputs and processing functions "returned" to us below
    beginingNumber, endingNumber = inputs()
    userCountingTrack = processing

    #because we refrenced them, we can now input them like the variables we've done before
    
    processing(beginingNumber,endingNumber) 
    outputs(userCountingTrack) #outputs here is essentially a fancy print statment, since that function only has a print statement inside it

    
## IPO part, where main gets it's stuff to do

def inputs():

    print("what number do you want to start with?")
    beginingNumber = int(input("enter a whole number greater than 0: "))
    print("what number do you want to end with?")
    endingNumber = int(input("enter a whole number greater than 0: "))

    return beginingNumber, endingNumber



def processing(startNumber,endNumber):
    

    userCountingTrack = 0

    if startNumber < endNumber:
        stepDirectonIndicator = 1

    for count in range(startNumber,endNumber,stepDirectonIndicator): #this code then will repeatedly iterate the following untill it reaches the specified end number:

        startNumber += 1 #it will add one to the the value stored in userBeginingNumber

        userCountingTrack += startNumber #it will add the sum of the current value of userBeginingNumber to userCountingTrack

        print(startNumber) #then print the current value stored in userBeginningNumber, before repeating again


    return startNumber, endNumber, userCountingTrack

def outputs(outputNumber):
    
    print(outputNumber)
    
main()






#def outputs():
    #print("main")


#def getPosInt():

    #posInt = input("please enter a whole number greater than 0: ")

   # return posInt