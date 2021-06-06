import time


true=['True','T','t','true']
false=['False','F','f','true']
score=0

def checker1(choice):
	global score
	if choice in true:
		score+=1
	else:
		score+=0

def checker2(choice):
	global score
	if choice in false:
		score+=1
	else:
		score+=0


name=input('Enter your name=')
print('Welcome, {} to this small quiz.'.format(name))
time.sleep(1)												#To delay the next display for one sec
print('Answers should be entered in either True or false.')
time.sleep(1)

print('\nLinus Torvalds developed Linux.')
time.sleep(1)
choice=input('>>>')
checker1(choice)

print('\nLinux is not Open Source.')
time.sleep(1)
choice=input('>>')
checker2(choice)

print('\nDennis Ritchie developed C language.')
time.sleep(1)
choice=input('>>')
checker1(choice)

print('\nC langage in developed in Bells Laboratory.')
time.sleep(1)
choice=input('>>')
checker1(choice)

print('\nLinux mint is not based on Ubuntu.')
time.sleep(1)
choice=input('>>')
checker2(choice)
print('\nC language is not the successor of B')
time.sleep(1)
choice=input('>>')
checker2(choice)

print('Congratz...!,You have got {} points from total of 6 points'.format(score))