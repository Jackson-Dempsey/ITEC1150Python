## Jackson Dempsey - Wage Calculator ##


##user input section

    ##input for regular work hours
userRegularWorkHours = float(input("How many REGULAR hours did you work this week?"))
userRegularPayRate = float(input("How much are you paid hourly?"))

    ##input for overtime work hours
userOvertimeWorkHours = float(input("How many OVERTIME hours did you work this week?"))
userOvertimePayIncrease = float(input("How many times MORE are you paid for overtime?"))

##calculations from data

regularPay = userRegularPayRate*userRegularWorkHours
overtimePay = round((userRegularPayRate*userOvertimePayIncrease)*userOvertimeWorkHours,2)
totalPay = regularPay + overtimePay

## print back to user

print("You earned a total of $",regularPay," in regular pay, and a total of $",overtimePay,"in overtime pay. In total, you earned $",totalPay,"in total pay this week.")