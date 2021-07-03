from tkinter import *
from tkinter import ttk
import functions



def GUI(rootwindow):
	rootwindow.title('Contact Book')					#title for the app
	rootwindow.geometry('380x300')						#specifing the size of the app
	rootwindow.resizable(False,False)					#Disabling the resizing
	panedWindow=ttk.PanedWindow(rootwindow,orient=HORIZONTAL)	#Creating a container for multiple windows
	panedWindow.pack(fill=BOTH,expand=True)

	frame1=ttk.Frame(panedWindow,relief=SUNKEN)		#Creating first frame inside the container in the name frame1

	#Entry boxes in the app
	labelName=Label(frame1,text='Full Name:')
	entryName=Entry(frame1)
	labelAddress=Label(frame1,text='Address:')
	entryAddress=Entry(frame1)
	labelNumber=Label(frame1,text='Phone:')
	entryNumber=Entry(frame1)
	labelEmail=Label(frame1,text='E-mail')
	entryEmail=Entry(frame1)
	buttonShow=Button(frame1,text='Show',padx=8,command=lambda: functions.Display(listContacts,
																					entryName,
																					entryAddress,
																					entryNumber,
																					entryEmail))
	buttonAdd=Button(frame1,text='Add',padx=8,command=lambda: functions.add(listContacts,
																			entryName,
																			entryAddress,
																			entryNumber,
																			entryEmail))
	buttonDelete=Button(frame1,text='Delete',padx=8,command=lambda: functions.delete(listContacts))
	buttonEdit=Button(frame1,text='Edit',padx=8,command=lambda: functions.edit(listContacts,
																			entryName,
																			entryAddress,
																			entryNumber,
																			entryEmail))

	labelName.grid(row=0,column=0,padx=(10,0),pady=(10,0),columnspan=3,sticky=W)
	entryName.grid(row=1,column=0,padx=(10,0),columnspan=3)
	labelAddress.grid(row=2,column=0,padx=(10,0),columnspan=3,sticky=W)
	entryAddress.grid(row=3,column=0,padx=(10,0),columnspan=3)
	labelNumber.grid(row=4,column=0,padx=(10,0),columnspan=3,sticky=W)
	entryNumber.grid(row=5,column=0,padx=(10,0),columnspan=3)
	labelEmail.grid(row=6,column=0,padx=(10,0),columnspan=3,sticky=W)
	entryEmail.grid(row=7,column=0,padx=(10,0),columnspan=3)
	buttonShow.grid(row=8,column=0,padx=(10,0),pady=(10,0))
	buttonAdd.grid(row=8,column=1,pady=(10,0))
	buttonDelete.grid(row=8,column=2,pady=(10,0))
	buttonEdit.grid(row=9,column=1,pady=(10,0))

	panedWindow.add(frame1,weight=1)							#end of the first frame(frame1)

	#------------------------------------------------------------------------

	frame2=ttk.Frame(panedWindow,relief=SUNKEN)				#creating second frame inside the container in the name frame2

	labelContacts=Label(frame2,text='Contacts')
	listContacts=Listbox(frame2)							#Adding list box to the frame2
	scrollbar=Scrollbar(frame2,orient=VERTICAL)				#Creating scrollbar in frame2

	functions.show_listbox(listContacts)
	

	labelContacts.grid(row=0,column=0,padx=(10,0),pady=(10,0))
	listContacts.grid(row=1,column=0,rowspan=8,padx=(10,0))
	scrollbar.grid(row=1,column=0,rowspan=8,sticky=N+S+E)

	listContacts.config(yscrollcommand=scrollbar.set)
	scrollbar.config(command=listContacts.yview)

	panedWindow.add(frame2,weight=4)						#end of the second frame(frame2)