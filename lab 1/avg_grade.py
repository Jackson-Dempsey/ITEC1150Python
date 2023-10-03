## Jackson Dempsey, Average Grade Calculator ##


#input variables


studentScore1 = float(input("what was student 1's score?"))

studentScore2 = float(input("what was student 2's score?"))

studentScore3 = float(input("what was student 3's score?"))

##internal maths

averageScore = round((studentScore1+studentScore2+studentScore3)/3.0,2)

##user output

print("the average score is", averageScore)

