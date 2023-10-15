"""docstring JACKSON DEMPSEY 10/3, redesign of the rainfall problem using MIPO design (main, input, processing, outputs) """

def main():
    userNoOfYearInput = inputs()

    processing(userNoOfYearInput)

    totalYearlyRain = processing

    print("the total annual inches of rain this year was",totalYearlyRain)
    
    yearlyRainAverage = totalYearlyRain/12 ## everything in this function works except for the end here where i have no clue how to get python to actually tell me the variable instead of a the memory adress of that functions
    #but REJOICE! i get to go to bed an hour early perhaps!

    print("the the average inches over this year was",yearlyRainAverage) 


def inputs():
    userNoOfYearInput = int(input("how many years are in your sample"))

    return userNoOfYearInput


def processing(noOfYear):

    for noOfYear in range(1, noOfYear+1): # outer for loop to define the years

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


main()


