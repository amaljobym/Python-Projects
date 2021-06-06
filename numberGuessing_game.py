#!/usr/bin/python3
import random
mssge="""Enter a number between 1 and 10"""
print(mssge)

#To input lower and upper bound
while True:
    try:
        lowerBound=int(input('Enter the lower bound='))
        upperBound=int(input('Enter the upper bound='))
        break
    except:#if inputed bound is wrong
        print('\nSorry, wrong input')

print('\n\t--You have total of 5 chances--\n')

#for setting guess number of computer
computrGuess=random.randint(lowerBound,upperBound)

#checking the guesses
count=1
while(count<=5):
    
    try:
        myCount=int(input('Enter your count='))#inputting our guess
        if myCount==computrGuess:
            print('Congratz....You nailed it')
            break
        elif myCount<computrGuess:
            print('Sorry, your guess is lower than my guess')
        elif myCount>computrGuess:
            print('Sorry, your guess is larger than my guess')
        count+=1
    except:#If inputed guess is wrong
        print('\nSorry, wrong input')
if count>5:
    print('Hmm, You are out of chances see you next time')
