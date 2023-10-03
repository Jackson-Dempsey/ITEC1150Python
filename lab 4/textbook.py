"""docstring"""
## Jackson Dempsey,  Textbook Cost Calculator


##todos
## -figure out how to check if the number is whole, using the modulo %, or prolly just by the is_integer method 
## -figure out why the the for range on the bottom is being dumb for some use cases, and not outputting the total

books_needed = int(input('How many textbooks do you have to buy? Please only enter a whole number.'))
#if books_needed % 1 != 0 and books_needed < 0:
    #print("this calculator doesn't take negitive or non-whole values for books, please try again")
    #quit()


##inital whole number for use in the for loop later
total_cost = 0.0

for book in range(books_needed):
    price = float(input(f'Enter price in dollars, formatted as: ($1.00) for book #{book+1}: '))
    ##if statement which cuts off program is a negitive number is input
    if price < 0:
        print("this calculator doesn't take negitive values for books, please try again")
        quit()
        
total_cost = total_cost + price # shorthand version... total_cost += price
print(f'\tRunning subtotal = ${total_cost :<.2f}.')
print(f'Grand total = ${total_cost :<.2f}.')

