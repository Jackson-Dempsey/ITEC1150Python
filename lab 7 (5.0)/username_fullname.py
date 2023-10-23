"""docstring, JACKSON DEMPSEY 10/22/23, username_fullname.py, managing a sudo-database of users using a python dictionary"""

def main():
    try:
        users = {

            'msmouse': 'Mouse, Minnie', 
            'mrmouse': 'Mouse, Mickey'

            } #initial dictonary

        display_menu()

        while True:
            command = input('Command: ')
            command = command.lower() #method to make all strings lowercase - clever!
            if command == 'view':
                view(users)
            elif command == 'add':
                add(users)
            elif command == 'edit':
                edit(users)
            elif command == 'del':
                delete(users)
            elif command == 'exit':
                print('Bye!')
                break
            else:
                print('Not a valid command. Please try again. \n')
    except KeyError:
        print('Key Error ')


def displayUsernames(userDictInput_displayUsernames): #function which will outputs all usernames in the dictonary
    
    usernameList_displayUsernames = list(userDictInput_displayUsernames.keys())
    usernameList_displayUsernames.sort() 
    
    line = str('Users: ')
    for username in usernameList_displayUsernames:
        line += username + ' '
    print(line)

    
    
    return usernameList_displayUsernames 


def display_menu(): #function to print out all the diffrent commmands
    print('COMMAND MENU')
    print('view - view all users and their coresponding full names')
    print('add - Add a new user')
    print('edit - Edit an existing user')
    print('del - Delete a user')
    print('exit - Exit program')
    print()

def view(userDictInput_view):

    displayUsernames(userDictInput_view) # will run this code for every function the user will end up using for refrence

    usernameInput_view = str(input("please enter the username you would like to see the full name of:"))

    if usernameInput_view in userDictInput_view:
        print(userDictInput_view[usernameInput_view]) #prints the value which results from the user spescified key
    else:
        print("there is no such username in the file")


def add(userDictInput_add):
    displayUsernames(userDictInput_add)
    usernameInput_add = input("please enter the username you would like to add.")

    while usernameInput_add in userDictInput_add :#while loop, to avoid namespace colision between usernames 
        print("there is already a user with this username, please choose a diffrent name")
        usernameInput_add = input("please enter a diffrent username.")

    actualName_Input = input('what is the full name of this user?')

    userDictInput_add.update({usernameInput_add:actualName_Input}) #updates the main dictionary with user specified strings, using the .update method
    print(userDictInput_add.get(usernameInput_add), "was added to users.") #uses the .get() method from the inital list in the function

def edit(userDictInput_edit):

    displayUsernames(userDictInput_edit) # will run this code for every function the user will end up using for refrence

    usernameInput_edit = str(input("please enter the username you would like to edit:"))

    if usernameInput_edit in userDictInput_edit:

        usernameCorrection_edit = str(input("please enter the full name you wish to change this username to:"))
        userDictInput_edit[usernameInput_edit] = usernameCorrection_edit #edits the value portion from the specified key in the dictionary

    else:
        print("there is no such username to edit in the file")

    print("the full name of the user has been changed to:",usernameCorrection_edit)


def delete(userDictInput_delete):

    displayUsernames(userDictInput_delete)

    usernameInput_delete = input("please enter the username you would like to delete:")

    if usernameInput_delete in userDictInput_delete:

        print(userDictInput_delete[usernameInput_delete], "will be deleted, is this ok?") #prints the message for the warning

        userConfirmation_delete = str("") #my guess is this code is probably redundant, but I'm keeping it in because I've gotten errors when commenting it out

        userConfirmation_delete = input("enter Y or N:") #if loop for validation for deletion

        #while userConfirmation_view != "Y" or userConfirmation_view != "N" or userConfirmation_view != "n" or userConfirmation_view != "y": #making sure the user is *actually* saying yes or no
            #userConfirmation_view = input("enter Y or N:") TODO - fix this, currently results in Unbound Local Error : "UnboundLocalError: local variable 'userConfirmation_view' referenced before assignment"
            #not fixing yet because this wasn't required for assigment
            
        if userConfirmation_delete == "Y":
            del userDictInput_delete[usernameInput_delete]  #deleting both key and value from the dictionary using the .pop method

        else:
            pass

        print("the user", usernameInput_delete, "has been deleted") #verifcation statement, printing out the username the user wanted deleted

    else:
        print("there is no such username to delete in the file")

main()
