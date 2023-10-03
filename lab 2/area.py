"""docstring"""
## Jackson Dempsey - Area of a Rectangle Calculator ##

print("Welcome to the Rectangle Area Calculator:")

##user input section, takes all relevant rectangle information for calculation 
userUnitInput = input("what units is your rectangle measured in? (inches, meters, ect...)?") 
userRectangleLengthInput = int(input(f"what is the length of your rectangle in {userUnitInput}?"))
userRectangleWidthInput = int(input(f"what is the width of your rectangle in{userUnitInput}"))

rectangleArea = userRectangleLengthInput*userRectangleWidthInput

print("Your Rectangle is", rectangleArea,"sqare",userUnitInput)


