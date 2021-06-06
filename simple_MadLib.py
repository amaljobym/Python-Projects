import random

Menu="""---MAD LIBS---
1)start
2)exit
----------------------"""

#main function
def main():
	print(Menu)
	command=input('Enter the command=')
	if(command=='1' or command=='start'):
		number=int(input('Enter the number of times:'))
	else:
		return
	count=1
	while(count<=number):
		randm=random.randint(1,2)
		if randm==1:
			madLib1()
		elif randm==2:
			madLib2()
		count+=1

#To store info which is being inputed
def info():
	noun=input("noun=")
	adjective=input("adjective=")
	verb=input("verb=")
	adverb=input("adverb=")
	place=input("place=")
	return noun,adjective,verb,adverb,place

#Mad Lib stories 1
def madLib1():
	print("---------------------------")
	print("I saw a <noun> who looks so <adjective> and he can <verb>")
	print("He was <adverb> hardworking")
	print("He lives at <place>")
	print("---------------------------")
	noun,adjective,verb,adverb,place=info()
	print("++Result++")
	print("---------------------------")
	print("I saw a {} who looks so {} and he can {}".format(noun,adjective,verb))
	print("He was {} hardworking.".format(adverb))
	print("I think he lives at {}".format(place))
	print("---------------------------")

#Mad Lib stories 2
def madLib2():
	print("---------------------------")
	print("I'm a <noun> who is very <adjective>")
	print("I can <verb> <adverb>")
	print("I hate going to <place>")
	print("---------------------------")
	noun,adjective,verb,adverb,place=info()
	print("++Result++")
	print("---------------------------")
	print("I'm a {} who is very {}".format(noun,adjective))
	print("I can {} {}".format(verb,adverb))
	print("I hate going to {}".format(place))
	print("---------------------------")


main()