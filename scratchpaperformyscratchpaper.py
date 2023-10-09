print("what number do you want to start with?")
beginingNumber = int(input("enter a whole number greater than 0: "))
print("what number do you want to end with?")
endingNumber = int(input("enter a whole number greater than 0: "))
print("how much do you want to count by? please only put positive values")
countAmt = int(input("enter a whole number greater than 0: "))








def nthTermInSeriesChecker(firstTermInSeries,lastTermInSeries,countRate):
    seriesList = []
    
    seriesList.append(firstTermInSeries)
    for count in range(firstTermInSeries,lastTermInSeries,countRate):
        firstTermInSeries += countRate
        seriesList.append(firstTermInSeries)

    print(seriesList)

    while lastTermInSeries != seriesList[-1]: ##series list * [-1] is finding the last element in the list, think of it like an offset
        print(f"Sorry, you can't get to {lastTermInSeries} by counting in {countRate}'s.")
        print(f"If you want to start with {seriesList[0]} and count in {countRate}'s:") ##in python you start with 0s when you count items in a list.
                                                                                        ##this is in no way confusing, and *definitely* has no possible ways to cause any bugs by confusion
        print(f"Try counting to {seriesList[-1]} instead.")
        exit()
    else:
        print(f"You can reach {lastTermInSeries} by counting in {countRate}'s. Here's the full count below:")

    return firstTermInSeries, lastTermInSeries, countRate

nthTermInSeriesChecker(beginingNumber,endingNumber,countAmt)
