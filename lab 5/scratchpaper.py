def main():

    beginingNumber, endingNumber = inputs()
    userCountingTrack = processing
    processing(beginingNumber,endingNumber) 
    print(userCountingTrack)
    


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
    
main()






#def outputs():
    #print("main")


#def getPosInt():

    #posInt = input("please enter a whole number greater than 0: ")

   # return posInt