"""docstring JACKSON DEMPSEY 10/3, redesign of the "loop 2" program, a number counter, using MIPO design (main, input, processing, outputs) """

## The Main part, which executes all the things we've created in the bottom IPO part

def main():



    #this refrences the variables which the inputs and processing functions "returned" to us below
    beginingNumber, endingNumber, countAmt = inputs()

    #because we refrenced them, we can now input them like the variables we've done before
    
    processing(beginingNumber,endingNumber, countAmt)

    #outputs() #outputs here is essentially a fancy print statment, since that function only has a print statement inside it

    
## IPO part, where main gets it's stuff to do

def inputs():

    print("what number do you want to start with?")
    beginingNumber = int(input("enter an integer: "))
    while isinstance(beginingNumber, int) == False:
        print("Please input an integer for the number you want to start with.")

    print("what number do you want to end with?")
    endingNumber = int(input("enter an integer"))
    while isinstance(endingNumber, int) == False:
        print("Please input an integer for the number you want to end with.")

    countAmt = int(input("enter a whole number greater than 0: "))
    while countAmt < 0 or isinstance(countAmt,int)==False: 
        print("please input a positive integer for the number you want to count by")
        countAmt = int(input("enter a whole number greater than 0: "))

    ## if statment which both will swap the direction the program counts if the ending number is smaller than the begining number
   
    if endingNumber <= beginingNumber:

        countAmt = countAmt*int(-1)

    

    else:
        pass

    nthTermInSeriesChecker(beginingNumber,endingNumber,countAmt)


    return beginingNumber, endingNumber, countAmt

##this function checks to see if the given number the user wants to count to can actually be counted to by the number they wanted to count by
def nthTermInSeriesChecker(firstTermInSeries,lastTermInSeries,countRate):

    ## checking to see if the first term in the series and the last term in the series are the same, so that I don't run into incorrect statements later.
    if firstTermInSeries == lastTermInSeries:
        print("You can't count up or down between two numbers that are the same.")
        print("Please input two diffrent numbers")
        exit()

    seriesList = []
    
    seriesList.append(firstTermInSeries)
    for count in range(firstTermInSeries,lastTermInSeries,countRate):
        firstTermInSeries += countRate
        seriesList.append(firstTermInSeries)

    print(seriesList)

    while lastTermInSeries != seriesList[-1]: ##series list * [-1] is finding the last element in the list, think of it like an offset

        
        print(f"Sorry, you can't get to {lastTermInSeries} by counting in {countRate}'s.")
        if countRate < 0:
            print("(- means we're counting backwards)") ##info statment so user get's what i'm doing with the negative count rate
        print(f"If you want to start with {seriesList[0]} and count in {countRate}'s:") ##in python you start with 0s when you count items in a list.
                                                                                        ##this is in no way confusing, and *definitely* has no possible ways to cause any bugs by confusion
        print(f"Try counting to the integer closest to it: | {seriesList[-1]} | instead.")
        exit()
        
    else:
        print(f"Starting from {seriesList[0]}, you can reach {lastTermInSeries} by counting in {countRate}'s. Here's the full count below:")

    return firstTermInSeries, lastTermInSeries, countRate


def processing(startNumber,endNumber,countAmt):
    
    #defining and setting a user counting track variable equal to zero so python can add the sum of the numbers later
    userCountingTrack = 0

    print(startNumber) # this prints the starting number before the rest of the loop is done
        #i know there is a way to fix the loop so i don't need to do this, but i'm lazy, so you're getting this.

    for count in range(startNumber,endNumber,countAmt): #this code then will repeatedly iterate the following untill it reaches the specified end number:

        startNumber += countAmt #it will add one to the the value stored in userBeginingNumber

        userCountingTrack += startNumber #it will add the sum of the current value of userBeginingNumber to userCountingTrack

        print(startNumber)


    print(f"the total sum of these numbers is: {userCountingTrack}")

    return startNumber, endNumber, userCountingTrack

def outputs(outputNumber):
    
    print(outputNumber)
    
main()






#def outputs():
    #print("main")


#def getPosInt():

    #posInt = input("please enter a whole number greater than 0: ")

   # return posInt