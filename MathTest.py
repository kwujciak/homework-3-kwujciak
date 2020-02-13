# My partner was Sami Rothstein.
# Kate Wujciak

import random

def addition(x,y):
# This function generates an addition problem.
# It asks a question, determines if it matches the corrrect answer,
# and then appropriately marks it correct or incorrect.
# It takes two arguments, x and y, which are the random numbers generated.
# This function has no return value.
    print("What is ", x, "+", y , "?")
    answer1 = int(input(''))
    if (answer1) == (x + y):
        print("Nice work!")
        print('')
        correct = True
        return correct
    else:
        print("Incorrect!")
        print('')
        correct = False
        return correct

def multiplication(x,y):
# This function generates a multiplication problem.
# It asks a question, determines if it matches the corrrect answer,
# and then appropriately marks it correct or incorrect.
# It takes two arguments, x and y, which are the random numbers generated.
# This function has no return value.
    print ("What is ", x, " x ", y , "?")
    answer2=int(input())
    if (answer2) == (x * y):
        print("You got it right!")
        print('')
        correct = True
        return correct
    else:
        print("Oops! Try again.")
        print('')
        correct = False
        return correct

def subtraction(x,y):
# This function generates a subtraction problem.
# It asks a question, determines if it matches the corrrect answer,
# and then appropriately marks it correct or incorrect.
# It takes two arguments, x and y, which are the random numbers generated.
# This function has no return value.
    print("What is ", x, " - ", y , "?")
    answer3=int(input())
    if (answer3) == (x - y):
        print("Awesome job!")
        print('')
        correct = True
        return correct
    else:
        print("Hmmm... not quite.")
        print('')
        correct = False
        return correct


def math_test():
# This function uses a for loop to run the three above questions 7 times.
# This ensures that there are 21 questions total (since 3 are randomly generated
# from the functions above). It calls each function above (addition, subtraction, and multiplication.)
# Depending on the questions that were correct, it will count those and return a score out of 21.
# Based on that score, if statments will generate certain print statements to be presented.
# It doesn't take any parameters. It has no return value.
    score = 0
    for i in range(7):
        x = random.randint(0,12)
        y = random.randint(0,12)
        mark = multiplication(x,y)
        if mark == True:
            score = score+1
        mark = subtraction(x,y)
        if mark == True:
            score = score+1
        mark = addition(x,y)
        if mark == True:
            score = score+1
    print('You scored a ', score, '/21')
    if score == 21:
        print('Congratulations! You received an A+')
        print(' ')
        print('BONUS QUESTION!!!')
        print('How many sides does this shape have?')
        print('+ '+('- '*4)+'+ ')
        print('|'+' '*9+'|')
        print('+ '+('- '*4)+'+ ')
        shape = int(input(''))
        if (shape) == (4):
            print("Correct! You got the bonus question right.")
            print("Since you got the extra bonus, +1 for you... and +1 for us! :)")
            correct = True
            return correct
    if score < 21 and score >= 19:
        print('You got an A!')
    if score < 19 and score >= 17:
        print('You received a B')
    if score < 17 and score >=15:
        print('You received a C')

math_test()