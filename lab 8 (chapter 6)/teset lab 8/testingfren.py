def main():
    userInput = input("Enter your book name: ")
    corrected_text = validateInput(userInput)
    print(corrected_text)


def validateInput(userInput, isBookName = False):

    words = userInput.split() #Split the Text: It breaks your sentence into separate words, like slicing a cake into pieces.
    correctedText = [] #Make an Empty List: We create a place to store the fixed words

    for index, word in (words):
        if isBookName and index != 0:
            word = word.lower() if word.lower() in ["the", "a", "an", "of", "in", "on", "at", "for"] else word.capitalize()
    else:
        word = word.lower() if word.lower() in ["van", "der", "de", "di"] else word.capitalize()
    correctedText.append(word)

    return ' '.join(correctedText)




main()