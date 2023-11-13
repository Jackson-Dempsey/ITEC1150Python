""" doctring JACKSON DEMPSEY,  """

## honestly crazy man, this litterally took less than 15 min

##notes, this doesn't match the prompt to an exact extent, but i made my first happy little acident today!
    ##, copying the line : print ("🤔 ".join([str(x) for x in generatedListInput_fancyPrintStatement])) from a preveious project, i thought i was gonna make a line seperator
    ## turns out the way it's implemented in the code now turns all periods in the text into emojis
    ## absotultely rockin, i'm assusming i could prolly do one of these with just a *liiiiiiiiitle* more effort and overall work
    ## https://lingojam.com/VaporwaveTextGenerator

def main():
    print(" welcome to the sentence splicer! ")
    fancyPrintStatement((sentenceSplicer(getSentence())))
    

def getSentence():
    userSentenceInput_getSentence = str(input("what sentance do you want me to splice up?"))
    return userSentenceInput_getSentence

def sentenceSplicer(userSentenceInput_sentenceSplicer):
    listedSentence_sentenceSplicer = userSentenceInput_sentenceSplicer.split(".",)
    return listedSentence_sentenceSplicer

def fancyPrintStatement(generatedListInput_fancyPrintStatement):

    print("here they are, but without the default python list brackets:")
    print ("🤔 ".join([str(x) for x in generatedListInput_fancyPrintStatement]))


    
main()