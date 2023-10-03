## Jackson Dempsey - Monthly Bus Fare Calculator ##

 ##bus fare costs

regularFare = float(1.75)
rushFare = float(3.00)

##rider freqency

riderFrequencyRegular = int(7)
riderFrequencyRush = int(12)

##maths

totalBusCost = (regularFare*riderFrequencyRegular)+(rushFare*riderFrequencyRush)

##console output

print ("With the data provided your total bus cost this month will be : $",totalBusCost)
