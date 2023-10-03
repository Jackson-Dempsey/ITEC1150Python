"""docstring"""

## Jackson Dempsey,  🐑 Counter (for loop 1.py)


print("a loop that prints all of the numbers from 0 through 5.")
for count in range (6): #range with default perimiters outputing integers from 0 to 5. 
    print(f"{count}🐑")

print("a loop that prints all of the numbers from 1 through 20.")
for count in range (1,21): #range with start and stop values to count to 1 to 20 respectivley. 
    print(f"{count}🐑")

print("a loop that prints all of the even numbers from 0 through 24.")
for count in range (2,26,2): #range which starts by counting 2, and stepping by 2 using the step parameter until it reaches 24 this way
    print(f"{count}🐑")

print(" a loop that prints all of the odd numbers from 37 through 53.")
for count in range (37,55,2): #same idea as previous counting, just starting with an odd integer this time
    print(f"{count}🐑")

print(" a loop that prints 10, 20, 30, 40, 50, 60.")
for count in range (10,60,10): #same idea as previous two, just using diffrent start and stop parameters and a diffrent step parameter
    print(f"{count}🐑")

print(" a loop that prints numbers counting down from 30 through 20")
for count in range (30,19,-1): #same idea as the previous iterations, only diffrence is a negtive step parameter which has the program subtract in iterations of 10 instead of add.
    print(f"{count}🐑")

