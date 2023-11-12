# this should find consecutive composite integers

import math # importing math because i do NOT feel like reinventing the definition of a factorial when a library has done it for me

def main ():
    print("let's find some consecutive composite numbers")

    userDesiredNoOfConsecutiveCompositeNumbers = int(input("how many consecutive primes do ya want?"))

    compositeList = []

    #setIsFound = False

    #initalize the list first:


    for numbers in range(0,userDesiredNoOfConsecutiveCompositeNumbers):
            compositeList.append(numbers)
            print(compositeList)

    print(listChecker(compositeList))

    loopCounterForPenultimateWhileLoop = 0 # didn't definite the counter outside the loop spent an hour trying to make a counter that would work inside the loop -_-
                                            #the worst part is i've made this exact same mistake before

    while listChecker(compositeList) == False:
    
        print("debug, composite list before modifcation",compositeList)
        print(listChecker(compositeList),"true or false before modification")


        compositeList.pop(0) #remove the first item from the list which has an index of 0, which starts at zero. how inutitive!

        loopCounterForPenultimateWhileLoop += 1

        #print(iterator, "should not be staying same")

        compositeList.insert(-1,userDesiredNoOfConsecutiveCompositeNumbers+loopCounterForPenultimateWhileLoop)

        print("debug, composite list after modificaion",compositeList)
        print(listChecker(compositeList),"true or false *after* modification")

    print(compositeList)


def listChecker (listToBeChecked):

    trueOrFalseList = [primeChecker(possiblePrimes) for possiblePrimes in listToBeChecked]

    #print((trueOrFalseList), "debug, what any(trueorfalse list sees)")
    
    if any (flag == True for flag in trueOrFalseList): # if anythings true(prime) in the list 
        #print("the if any flag thing triggered")
         return False
    else:
         return True # other wise, what we have *must* be what we want

    #for possiblePrimes in listToBeChecked:

        #print(possiblePrimes, "prime numbers python sees")

        #if primeChecker(possiblePrimes) == True:
                #return False # feels redundant
                #break
                
        #else: 
            #return True
            
    
#function looper

    #loopyloop = True

    #while loopyloop == True:
        #exNumber = int(input("what number should we test?"))

        #theTruth = primeChecker(exNumber)
        #print(theTruth)

        #loopStopper = True

        #loopStopper = bool(input("continue? if not just say exit"))
        #if loopStopper == False:
        #    exit
        #else:
        #    True




    # thankfully for our purposes, checking between primeness and compositeness is binary

def primeChecker (n): 

    #elif-ing the heck out of this in a terribly suboptimal fashion because this doesn't need to be optimal, just understandable



    compositeHitter = False
        
    for multiples in range(2,n,1): # range configuration: start with 2, end with n (not n-1 like normal because n makes the second to last which we want here)
                                        
        #print(n, multiples, "debug")
        #print(n % multiples)
        if n % multiples == 0:
            compositeHitter = True
            return False
            break 


    if compositeHitter == False:
        return True
            

        
        #the question stands, if we're making a composite checker, how do we loop until find something that proves it's composite 

    #finally, spagetti code but this thing works!


    
            

main()

## STUFF FROM THE PRIME CHECKER

## code graveyard 👻👻👻

    #if n.is_integer == False: #non-integers cannot be primes
        #print("it was not an integer")
        #return  False
        

    #if n < 2: #anything below 2 is either negative, 0, or 1, thus not really helping us here, for our purposes at least
        #print("it was not greater than 2")
        #return False
        

    #elif n == 2:
        #print("it's 2 lol")
        #return True
    


