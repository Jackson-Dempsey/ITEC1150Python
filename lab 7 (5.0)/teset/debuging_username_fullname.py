def main():
    try:
        users = {'allen': 'julius',}  # Create an empty dictionary to store user names and countries

        while True:
            command = input('Command: ')
            command = command.lower()
            if command == 'view':
                view(users)
            elif command == 'add':
                add(users)
            elif command == 'del':
                delete(users)
            elif command == 'edit':
                edit(users)
            elif command == 'exit':
                print('Bye!')
                break
            else:
                print('Not a valid command. Please try again. \n')
    except KeyError:
        print('Key Error ')

def view(users):
    display_keys(users)
    userName = input('Enter user name to view: ')
    userName = userName.lower()
    if userName in users:
        fullName = users[userName]
        print('User name: ' + fullName + '.\n')
    else:
        print('There is no user with that code. \n')

def add(users):
    display_keys(users)
    userName = input('Enter new user name to add: ')
    userName = userName.lower()
    if userName in users:
        fullName = users[userName]
        print(fullName + ' is already using this code. \n')
    else:
        fullName = input('Enter user name: ')
        fullName = fullName.title()
        users[userName] = fullName
        print (fullName + ' was added. \n')

def edit(users):
    display_keys(users)
    userName = input('Enter the new user name: ')
    fullName = input('Enter the new full name: ')
    users.update({'userName': 'fullName'})  # Use the update method to edit the entry
    print(f'User name updated to: {userName} Full name updated to: {fullName}.\n')

def delete(users):
    display_keys(users)
    fullName = input('Enter user name to delete: ')
    fullName = fullName.lower()
    if fullName in users:
        fullName = users.pop(userName)
        print (fullName + ' was deleted. \n')
    else:
        print ('There is no user with that code. \n')

def display_keys(users):
    userNames = list(users.keys())
    userNames.sort()
    line = 'User names: '
    for userName in userNames:
        line += userName + ' '
    print(line)


main()