"""docstring"""
## Jackson Dempsey - Apollo 11 Quiz Question ##

year = int(input('What year did Apollo 11 land on the moon? '))
correctAnswerYear = 1969

if year == correctAnswerYear:
    print(f'Correct! {year} is right!')

elif year >= 1968 and year <= 1970:
    print(f"{year} was so close! {correctAnswerYear} was ther right year.")
##additonal else if statment to tell them to try again if they're within a year of the correct date

else:
    print(f'Sorry, {year} is the wrong answer, it was the year {correctAnswerYear}')