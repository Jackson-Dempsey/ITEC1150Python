"""docstring"""

## Jackson Dempsey - Coffee Bar Sales Code

##  example coffee bar code

coffeeCups = int(input('How many cups of coffee sold? '))
coffeePrice = float(input('Price of coffee? '))
coffee_sales = coffeeCups * coffeePrice
print(f'Total sales = ${coffee_sales:,.2f}')

print(f'Gross sales today, for {coffeeCups} cups of coffee: ')
print('{:<20}{:>3}{:>8,.2f}'.format('Price per cup', '$', coffeePrice))
print('{:<20}{:>3}{:>8,.2f}'.format('Total sales', '$', coffee_sales))