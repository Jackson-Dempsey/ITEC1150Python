"""docstring JACKSON DEMPSEY 10/3, redesign of the rainfall problem using MIPO design (main, input, processing, outputs) """

def main():
    userNoOfYearInput = inputs()

    yearlyRainTrackingList = processing(userNoOfYearInput)

    #print("the total annual inches of rain this year was",totalYearlyRain)
    
    #yearlyRainAverage = totalYearlyRain/12

    #print("the the average inches over this year was", yearlyRainAverage) 

    outputs(yearlyRainTrackingList)


def inputs():

    userNoOfYearInput = int(input("how many years are in your sample"))
    if userNoOfYearInput < -1 or userNoOfYearInput % 1 != 0:
                #checks if the number is negative or a decimal by comparing the variable to -1 and using a modulo to find a remainder - INPUT VALIDATION
                userNoOfYearInput = int(input("please enter a positive, non decimal number: "))

    return userNoOfYearInput


def processing(noOfYear):

    yearlyRainTrackingList = [] #defining an empty list to help me keep track of each year so I can manipulate this data later for display in main()
    #

    for noOfYear in range(1, noOfYear+1): # outer for loop to define the years

        totalYearlyRain = int(0) #definining variable to track total yealy rain, in the outer year loop so it doesn't reset everytime a new iteratation of the month loop is called
        
        print("year: ",noOfYear)
        
        for months in range(1,12+1):
            print("month:", months)
            monthlyRainAmt = float(input("enter inches of rain for the following month:"))
            if monthlyRainAmt < -1:
                #checks if the number is negative or a decimal by comparing the variable to -1 and using a modulo to find a remainder - INPUT VALIDATION
                monthlyRainAmt = int(input("please enter a positive number "))

            totalYearlyRain = totalYearlyRain + monthlyRainAmt

        yearlyRainTrackingList.append(totalYearlyRain)
            
        #print(yearlyRainTrackingList)
        #just in case i need to see what the list's doing

    return yearlyRainTrackingList



def outputs(outputlist):

    for years in range(1, len(outputlist)+1):
        print("the total yearly rain for year", years, "was", round((outputlist[years-1]),2))
        print("the average yearly rain for year", years, "was", round(((outputlist[years-1])/12),2))
        
        
main()


