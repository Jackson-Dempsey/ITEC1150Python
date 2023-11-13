""" doctring JACKSON DEMPSEY,  """


def main():
    print(" welcome to the ! phrase splicer ")
 
    fancyPrintStatement((sentenceSplicer(getSentence())))


    

def getSentence():
    userSentenceInput_getSentence = str(input("what ! phrases do you want me to splice up, be sure to put a ! in between each phrase")) #standard input statment

    ## exclamation mark validation, if else which looks at the string the user gave, does nothing if it's got a !, tells user to re input if there's no !

    if "!" in userSentenceInput_getSentence:
        pass
    else:
        userSentenceInput_getSentence = str(input("be sure to put a ! behind your sentances, try again"))
    return userSentenceInput_getSentence


def sentenceSplicer(userSentenceInput_sentenceSplicer):
    listedSentence_sentenceSplicer = userSentenceInput_sentenceSplicer.split("!") #.split method, with the seperator perameter being a "!"
    print(listedSentence_sentenceSplicer)
    return listedSentence_sentenceSplicer


def fancyPrintStatement(generatedListInput_fancyPrintStatement):

    formattedList_fancyPrintStatment = [ unformattedListItems.capitalize()+"!" for unformattedListItems in generatedListInput_fancyPrintStatement ] # both uses the .capitalize method to capitalize list items
                                                                                                                                                    # as well as using string addition to add ! back again
    print(formattedList_fancyPrintStatment)


    print (" \n ".join([str(x) for x in formattedList_fancyPrintStatment])) # adds a \n after every line 


    
main()