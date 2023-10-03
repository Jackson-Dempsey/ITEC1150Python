"""docstring"""
## Jackson Dempsey - Trip Gas Calculator

## user inputs

userMilesDriven = float(input("How many miles did you drive on your trip?"))
userGasUsed = float(input("How many gallons of gas did you use on your trip?"))
userGascost = float(input("How much did you spend on gas per gallon?"))

## calculating user inputs

userMPG = round(userMilesDriven/userGasUsed,2)
userTripCost = round(userGascost*userGasUsed,2)

## user output
print("here is some relevent information about your trip")

print("Your Miles Per Gallon on this trip where:" , userMPG)
print("This total trip cost you : $", userTripCost)