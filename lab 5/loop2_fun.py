"""docstring"""

## Jackson Dempsey,  Counting Program

print("Welcome to the Counting Program:")

#inputs

##ask user for starting and ending number -
##I wasn't able to quite understand what you where asking the user in the slides, but the program I made comes to roughly the same result given the given inputs

userBeginingNumber = int(input("Please enter a number you want to begin with, greater than 0:"))-1 #subtracting by one so the range works properly
userEndingNumber = int(input(f"Please enter a number you want to end with, which is greater than or less than {userBeginingNumber+1}, and still greater than 0:"))

userCountingTrack = 0 #declaring a variable to be used when summing the total numbers counted later

#code snippet to make sure the step parameter in the range function is correct for counting either up or down

#positive if we're counting up
if userBeginingNumber < userEndingNumber:
    stepDirectonIndicator = 1

    for count in range(userBeginingNumber,userEndingNumber,stepDirectonIndicator): #this code then will repeatedly iterate the following untill it reaches the specified end number:

        userBeginingNumber += 1 #it will add one to the the value stored in userBeginingNumber

        userCountingTrack += userBeginingNumber #it will add the sum of the current value of userBeginingNumber to userCountingTrack

        print(userBeginingNumber) #then print the current value stored in userBeginningNumber, before repeating again

#negative if we're counting down

else: #does everything above, except now subtracting instead of adding values untill it reaches the end
    stepDirectonIndicator = -1 

    for count in range(userBeginingNumber,userEndingNumber,stepDirectonIndicator): 

        userBeginingNumber -= 1 

        userCountingTrack -= userBeginingNumber 

        print(userBeginingNumber)


print(f"The total sum of the numbers counted is:{userCountingTrack}") ##after it completes it's for loop, it will print out the total sum (or negative sum) it found from counting all the numbers
