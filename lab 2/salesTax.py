"""docstring"""
## Jackson Dempsey - Sales Tax Calculator


## User Input Data

userTotalPurchaseOrder = float(input("what is the total price of your purchase?"))


##Maths for output

stateSalesTax = round(.05 * userTotalPurchaseOrder,2) 
countySalesTax = round(.025 * userTotalPurchaseOrder,2)
totalCost = userTotalPurchaseOrder + stateSalesTax + countySalesTax

## Output back to the user data calculated

print(f'Here are the total taxes incrued in your purchase of {userTotalPurchaseOrder}:')
print('{:<20}{:>3}{:>8,.2f}'.format('Initial Purchase', '$', userTotalPurchaseOrder))
print('{:<20}{:>3}{:>8,.2f}'.format('State Sales Tax', '$', stateSalesTax))
print('{:<20}{:>3}{:>8,.2f}'.format('County Sales Tax', '$', countySalesTax))
print('{:<20}{:>3}{:>8,.2f}'.format('Total Cost', '$', totalCost))
