
#brief note, the (f"{}") notation for some reason doesn't work on my version of pycharm, so print statements are a bit longer.

userYearInput = int(input("how many years are in your sample"))


for userYearInput in range(1, userYearInput+1): # outer for loop to define the years

    totalYearlyRain = int(0) #definining variable to track total yealy rain, in the outer year loop so it doesn't reset everytime a new iteratation of the month loop is called
#spent 30 minutes debugging this :(

    for months in range(1,12):
        print("month:", months)
        monthlyRainAmt = int(input("enter inches of rain for the following month:"))

        #three print statements I used to monitor the console input
        ##print(monthlyRainAmt)
        ##print(monthlyInputList)

        totalYearlyRain = totalYearlyRain + monthlyRainAmt

        #print(totalYearlyRain)

    else: ##adding the else at the end of this for statment, so that it knows to do the final code when the loop finishes

        print("the total annual inches of rain this year was",totalYearlyRain)
        yearlyRainAverage = totalYearlyRain/12 # Remember to calculate it in this part of the loop, so it knows what variables are being used in the inputs
        print("the the average inches over this year was",yearlyRainAverage)









