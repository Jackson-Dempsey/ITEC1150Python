"""docstring"""
## Jackson Dempsey - Pennies in a Jar Calculator ##

#ask user for the number 

userPenniesInJar = (input("how many pennies are in your jar?"))

# whole number validator, stops program if false, continues in the else statement if true

if userPenniesInJar.isnumeric() is False: {

print('Try again, you can only have a whole number of pennies!')

}

else:

    if int(userPenniesInJar) > 100: print("You have more than 100 pennies, more than a dollar you're rich!")

    ##inital if is checking for more than 100, will output subsequent more than 100 message

    elif int(userPenniesInJar) == 100: print("you have 100 pennies, that's a whole dollar!")

    ##the second elif is checking for *exactly* 100, will output subsequent exactly 100 message

    ##note the int statements in the front for the first two, 
    #this because the is numeric method will only be able to work if the data's a string, ergo needing to declare it back to an int again later

    else: print("you have less than 100 pennies, less than a dollar...")

print(float(userPenniesInJar)*.01,"$ to be exact.")

## output the user's inital amount of pennies, times by .01 to get the dollar amount
   






