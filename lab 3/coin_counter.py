"""docstring"""
## Jackson Dempsey - Coin Counter ##

##asks user for each of the 4 coin types

UserQuarterCount = input("How many quarters do you have? - please enter a whole number")
UserDimeCount = input("How many dimes do you have? - please enter a whole number")
UserNickleCount = input("How many nickles do you have? - please enter a whole number")
UserPennyCount = input("How many pennies do you have? - please enter a whole number")


# whole number validator, stops program if any values are false, continues in the else statement if true

if UserQuarterCount.isnumeric() and UserDimeCount.isnumeric() and UserNickleCount.isnumeric and UserPennyCount is False: 
    print('Please input your coin counts again, one or more of your variables are not whole numbers')

else:
    
    ## defining "actual money amounts" from the number of coins

    userQuarterFloat = float(UserQuarterCount)*.25
    userDimeFloat = float(UserDimeCount)*.10
    userNickelFloat = float(UserNickleCount)*.05
    userPennyFloat = float(UserPennyCount)*.01

    userTotalCoinValue = userQuarterFloat+userDimeFloat+userNickelFloat+userPennyFloat


    ##formats the relevent data for the user

    #print('{:<20}{:>3}{:>8,.2f}'.format('Coin Type', 'Amount', "Value"))
    print('{:<20}{:>3}{:>8,.2f}'.format('Quarter', UserQuarterCount , userQuarterFloat))
    print('{:<20}{:>3}{:>8,.2f}'.format('Dime', UserDimeCount , userDimeFloat))
    print('{:<20}{:>3}{:>8,.2f}'.format('Nickel', UserNickleCount , userNickelFloat))
    print('{:<20}{:>3}{:>8,.2f}'.format('Penny', UserPennyCount , userPennyFloat))
    print("Total Coins", userTotalCoinValue)

if userTotalCoinValue < 10:
    print("good job on saving, you've got more than 10 dollars in those coins!")
else:
    print("keep on saving, you're not quite close to 10 dollars yet")
