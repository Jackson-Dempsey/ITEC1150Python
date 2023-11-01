"""DOCSTRINGS JACKSON DEMPSEY, 10/30 text_validator.py, program that validates that we entered a string with the nomenclature of a title, including some edge cases """


### note, for capitalization exemption, since it would take all day to find all the prepostions/parts of names for english capitalization conventions, eg. (a, and, in, ...)
    ### the primary capitalization cases I'll check for will be the ones from the example (the, of) / (van, der, di)

def main():
    print("welcome to the text validator")
    print(titleValidator()) #when called, the function will output our desired naming style on our string

def titleValidator():

    givenUserTitle_titleValidator = str(input("please input a book title, with each word capitalized (or don't... this program will do it for you.)"))

    

    while givenUserTitle_titleValidator.isnumeric() == True :
        givenUserTitle_titleValidator = input("please try your input again, if your book title has numbers in it, write them out... (apologies in advance if you put in 1984.)") #broad check to make sure there are no numbers in the title 
    
    titleWordList_titleValidator = givenUserTitle_titleValidator.split(" ") #splits the words from the user's given title into a list, with the whitespace (spaces) dictating where things should be split

    properCapitalTitleList_titleValidator = [posibleNonCapitals.capitalize() for posibleNonCapitals in titleWordList_titleValidator] ## will capitalize each word in the list

    #running all exemptions required from the prompt in the exception handler function I made below
    #note that as it currently stands, the "exception word" string *has* to be uppercase
    titleCapitalExceptionHandler(properCapitalTitleList_titleValidator, "The")
    titleCapitalExceptionHandler(properCapitalTitleList_titleValidator, "Of")
    titleCapitalExceptionHandler(properCapitalTitleList_titleValidator, "Van")
    titleCapitalExceptionHandler(properCapitalTitleList_titleValidator, "Der")
    titleCapitalExceptionHandler(properCapitalTitleList_titleValidator, "Di")
    
    outputString = (" ".join([str(x) for x in properCapitalTitleList_titleValidator]))

    return outputString

# function for handling exemptions in capitalization

def titleCapitalExceptionHandler(userSpecifiedList : list, exceptionWord : str): #takes a list and the exception word in the form of a string

    exemptionIndexCounter = int(-1) #counter here to track progress through the list, important later to find the index of the exemption words

    for possibleExemptions in userSpecifiedList:

        exemptionIndexCounter = exemptionIndexCounter + 1

        if possibleExemptions == exceptionWord and exemptionIndexCounter != 0: # checking in the loop for the exemption word, 
                                                                                # also checking for the index being 0, because that's equivlient to the start of our title here

            userSpecifiedList[exemptionIndexCounter] =  exceptionWord.lower() #replaces the uppercase word with the lowercase word using the .lower method
main()