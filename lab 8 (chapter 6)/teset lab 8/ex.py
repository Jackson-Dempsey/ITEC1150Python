


#def main ():

   # print("this is main")

    #exFunc()

    #exNumber = exFunc()

    #print(exNumber)




#def exFunc ():

 #   exNumber = str(input("give me a word!"))

  #  return exNumber


# example code on how to switch one instance of something in a list to another, could be optimised a hell of a lot more but it works man.

test_list = [1, 6, 4, 3, 5, 3, 4]

indexCounter = int(-1)
 
# Checking if 4 exists in list
for i in test_list:

    indexCounter += 1

    if(i == 4):

        print(indexCounter)
        
        test_list[indexCounter] = "this works"


print(test_list)




