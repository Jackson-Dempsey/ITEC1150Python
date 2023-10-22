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
    print(usernameList_displayUsernames,"debug")
    
    return usernameList_displayUsernames 


def display_menu(): #function to print out all the diffrent commmands
    print('COMMAND MENU')
    print('view - View country name')
    print('add - Add a country')
    print('del - Delete a country')
    print('exit - Exit program')
    print()

def view(userDictInput_view):

    print(displayUsernames(userDictInput_view))

    usernameInput_view = str(input("please enter the username you would like to see the full name of:"))

    if usernameInput_view in userDictInput_view:
        print(userDictInput_view[usernameInput_view]) #prints the value which results from the user spescified key
    else:
        print("there is no such username in the file")


def add(userDictInput_add):
    print(displayUsernames(userDictInput_add))
    usernameInput_add = input("please enter the username you would like to add.")

    while usernameInput_add in userDictInput_add :#while loop, to avoid namespace colision between usernames 
        print("there is already a user with this username, please choose a diffrent name")
        usernameInput_add = input("please enter a diffrent username.")

    actualName_Input = input('what is the full name of this user?')

    userDictInput_add.update({usernameInput_add:actualName_Input}) #updates the main dictionary with user specified strings, using the .update method
    print(userDictInput_add.get(usernameInput_add), "was added to users.") #uses the .get() method from the inital list in the function
    

def delete(userDictInput_delete):

    print(displayUsernames(userDictInput_delete))

    usernameInput_delete = input("please enter the username you would like to delete:")

    if usernameInput_delete in userDictInput_delete:
        print(userDictInput_delete[usernameInput_delete], "will be deleted, is this ok?") #prints the message for the warning
        userConfirmation_delete = input("enter Y or N:") #if loop for validation for deletion
        userConfirmation_delete.upper
        while userConfirmation_view != "Y" or userConfirmation_view != "N":
            userConfirmation_view = input("enter Y or N:")
            
        if userConfirmation_view == "Y":
            userDictInput_delete.pop(usernameInput_delete)
        else:
            pass

        print("the user", usernameInput_delete, "has been deleted")

    else:
        print("there is no such username to delete in the file")

main()
