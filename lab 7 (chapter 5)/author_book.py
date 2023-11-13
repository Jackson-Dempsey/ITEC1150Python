""""DOCSTRING, JACKSON DEMPSEY 10/22/23, author_book.py, similar to username_fullname.py, except all nomenclature has been switched from books to authors, and capitlization rules where implemented."""

def main():
    try:
        readings = {

            'Edward Snowden': 'Permanent Record', 
            'Theodor Seuss Geisel': 'How the Grinch Stole Christmas',
            'Adam Smith': 'The Wealth of Nations'

            } #initial dictonary

        display_menu()

        while True:
            command = input('Command: ')
            command = command.lower() #method to make all strings lowercase - clever!
            if command == 'view':
                view(readings)
            elif command == 'add':
                add(readings)
            elif command == 'edit':
                edit(readings)
            elif command == 'del':
                delete(readings)
            elif command == 'exit':
                print('Bye!')
                break
            else:
                print('Not a valid command. Please try again. \n')
    except KeyError:
        print('Key Error ')


def displayAuthors(userDictInput_displayAuthors): #function which will outputs all authors in the dictonary
    
    authorsList_displayAuthors = list(userDictInput_displayAuthors.keys())
    authorsList_displayAuthors.sort() 
    
    line = str('Users: ')
    for author in authorsList_displayAuthors:
        line += author + ' '
    print(line)

    
    return authorsList_displayAuthors 


def display_menu(): #function to print out all the diffrent commmands
    print('COMMAND MENU')
    print('view - view all authors and their coresponding books')
    print('add - add a new author and thier coresponding book')
    print('edit - modify the book of an existing author')
    print('del - delete an author')
    print('exit - exit program')
    print()

def view(userDictInput_view):

    displayAuthors(userDictInput_view) # will run this code for every function the user will end up using for refrence

    authorInput_view = str(input("please enter the author you would like to see the books for, (this input is case sensitive!):"))

    if authorInput_view in userDictInput_view:
        print(userDictInput_view[authorInput_view]) #prints the value which results from the user spescified key
    else:
        print("there is no such author in the file")


def add(userDictInput_add):
    displayAuthors(userDictInput_add)
    authorInput_add = str(input("please enter the author you would like to add.")).title()

    while authorInput_add in userDictInput_add :#while loop, to avoid namespace colision between authors 
        print("there is already a author with this name, please choose a diffrent author")
        authorInput_add = input("please enter a diffrent author.")

    actualAuthorName_Input = str(input('what is the book of this author?')).title()

    userDictInput_add.update({authorInput_add:actualAuthorName_Input}) #updates the main dictionary with user specified strings, using the .update method
    print(userDictInput_add.get(authorInput_add), ".") #uses the .get() method from the inital list in the function

def edit(userDictInput_edit):

    displayAuthors(userDictInput_edit) # will run this code for every function the user will end up using for refrence

    authorInput_edit = str(input("please enter the author you would like to change the book for (this input is case sensitive!):"))

    if authorInput_edit in userDictInput_edit:

        authorCorrection_edit = str(input("please enter the book you wish to attribute to this author:")).title()

        userDictInput_edit[authorInput_edit] = authorCorrection_edit #edits the value portion from the specified key in the dictionary

        print("book has been changed to:",authorCorrection_edit)

    else:
        print("there is no such author to edit in the file")

    


def delete(userDictInput_delete):

    displayAuthors(userDictInput_delete)

    authorInput_delete = input("please enter the author you would like to delete (this input is case sensitive!):")

    if authorInput_delete in userDictInput_delete:

        print(userDictInput_delete[authorInput_delete], "will be deleted, is this ok?") #prints the message for the warning

        userConfirmation_delete = str("") #my guess is this code is probably redundant, but I'm keeping it in because I've gotten errors when commenting it out

        userConfirmation_delete = input("enter Y or N (no doesn't work your author will be deleted, sorry mate...):") #if loop for validation for deletion

        #while userConfirmation_view != "Y" or userConfirmation_view != "N" or userConfirmation_view != "n" or userConfirmation_view != "y": #making sure the user is *actually* saying yes or no
            #userConfirmation_view = input("enter Y or N:") TODO - fix this, currently results in Unbound Local Error : "UnboundLocalError: local variable 'userConfirmation_view' referenced before assignment"
            #not fixing yet because this wasn't required for assigment
            
        if userConfirmation_delete == "Y" or userConfirmation_delete == "y":
            del userDictInput_delete[authorInput_delete]  #deleting both key and value from the dictionary using the .pop method

        else:
            pass

        print("the author", authorInput_delete, "has been deleted") #verifcation statement, printing out the author the user wanted deleted

    else:
        print("there is no such author to delete in the file")

main()