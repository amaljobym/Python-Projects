import random

caption="""
\t\t--Welcome--
\t--To Dice Rolling Simulator--\n"""

yes=['Y','y','yes']
no=['N','n','no']


def number():
	roll=random.randint(1,6)
	if roll == 1:
		result="""
			[-----]
			[     ]
			[  0  ]
			[     ]
			[-----]"""
	elif roll==2:
		result="""
			[-----]
			[0    ]
			[     ]
			[    0]
			[-----]"""
	elif roll==3:
		result="""
			[-----]
			[0    ]
			[  0  ]
			[    0]
			[-----]"""
	elif roll==4:
		result="""
			[-----]
			[0   0]
			[     ]
			[0   0]
			[-----]"""
	elif roll==5:
		result="""
			[-----]
			[0   0]
			[  0  ]
			[0   0]
			[-----]"""
	elif roll==6:
		result="""
			[-----]
			[0   0]
			[0   0]
			[0   0]
			[-----]"""
	return result


print(caption)
while True:
	choice=input("Press Y to continue and N to exit=")
	if choice in yes:
		print(number())
	elif choice in no:
		print('Ok!, See you next time...')
		break