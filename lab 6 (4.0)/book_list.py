"""DOCSTRING Jackson Dempsey - 10/15, book list, takes generates a list of book prices names based on user input, and returns the input back to the user in a print statment"""

def main():  # call functions and save results under key variable names.
    try:  # generic exception handling - turn off during development
        num_books, price_list, name_list = inputs()
        total, average = processing(price_list)
        outputs(num_books, price_list, name_list, total, average)
        restart = input('Need more books? Enter y or n: ')  # restart feature
        if restart == 'y':
            print('OK, let\'s create a new list.')
            main()
        else:
            print('Thanks for using the program.')
    except Exception as err:  # turn off during development
        print(err)  # turn off during development


def inputs():  # collect info needed from the user.
    print('Enter the number of books that you need ')  # user sets the list length/ repetitions of the for loop
    num_books = get_pos_int()  # call validation function to collect int > 0

    price_list = []  # create list to save prices
    name_list = [] # create a list to save names

    for index in range(num_books):  # for loop runs user-specified number of times & collects info on each book

        print(f'Enter the name of your book:')
        book_name = get_book_name()  # call validation function to collect int > 0
        name_list.append(book_name)  # build list of names


        print(f'Enter the cost of book #{index +1}, to the nearest dollar: ')
        book_cost = get_pos_int()  # call validation function to collect int > 0
        price_list.append(book_cost)  # build price list
        
    return num_books, price_list, name_list


def get_pos_int():  # collect and validate an int > 0
    pos_int = input('Please enter a whole number: ')
    while pos_int.isnumeric() is False or int(pos_int) == 0:
        pos_int = input('Enter a number greater than 0: ')
    pos_int = int(pos_int)
    return pos_int

def get_book_name():  # collect and validate an int > 0
    #same as get pos int, except built to work with strings, not positive integers
    book_name = input('Please enter the name of your book')
    #I'll be honest I have no clue how we would get input for anything other than a string
    #but for the sake of completion anyways, string validation
    while isinstance(book_name,str) == False:
        book_name = input('please give me a string! - book name:')
        
    str(book_name)
    return book_name


def processing(price_list):  # use the list to calculate summary data
    total = sum(price_list)
    average = round(total / len(price_list), 2)
    return total, average


def outputs(num_books, price_list, name_list, total, average):  # display information about each book, and summary info
    print(f'Info on {num_books} Books Needed')
    print(f'{"Book:":<10}{"Price":>10}')


    for index in range(len(price_list)):
        #name list is ok to work in tandem with pricelist, their indexes will always be the same length, and always have each number from the index corespond with each other
        print(f'{name_list[index]}\t\t   ${price_list[index]:>8.2f}')
    print(f'{"Total":<10} ${total:>8.2f}')
    print(f'{"Average":<10} ${average:>8.2f}')


main()  # call main to start or restart program.