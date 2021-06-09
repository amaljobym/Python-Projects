from tkinter import *
from tkinter import ttk 		#ttk contains modern styles needed for the program
import sqlite3


def save():
	con=sqlite3.connect('database.db')
	cursr=con.cursor()
	cursr.execute("INSERT INTO profiles VALUES(:fname,:address,:ph,:email)",
		{'fname':entryName.get(),
		'address':entryAddress.get(),
		'ph':entryPhone.get(),
		'email':entryEmail.get()})

	con.commit()
	con.close()

def edit():
	pass

def delete():
	pass

root=Tk()
root.title('Contact Book')
root.geometry('400x300')

#creating paned window for adding seperate multiple widgets/window 
panedwindow=ttk.PanedWindow(root,orient=HORIZONTAL)
panedwindow.pack(fill=BOTH,expand=True)

#first frame(left side window)
frame1=ttk.Frame(panedwindow,width=100,height=100,relief=SUNKEN)

LabelName=Label(frame1,text='Name:')
entryName=Entry(frame1)
LabelAddress=Label(frame1,text='Address:')
entryAddress=Entry(frame1)
LabelPhone=Label(frame1,text='Phone:')
entryPhone=Entry(frame1)
LabelEmail=Label(frame1,text='E-mail:')
entryEmail=Entry(frame1)
addButton=Button(frame1,text='add',command=save)

LabelName.grid(row=0,column=0,padx=(10,0),pady=(10,0),sticky=W)
entryName.grid(row=2,column=0,padx=(10,0))
LabelAddress.grid(row=3,column=0,padx=(10,0),sticky=W)
entryAddress.grid(row=4,column=0,padx=(10,0))
LabelPhone.grid(row=5,column=0,padx=(10,0),sticky=W)
entryPhone.grid(row=6,column=0,padx=(10,0))
LabelEmail.grid(row=7,column=0,padx=(10,0),sticky=W)
entryEmail.grid(row=8,column=0,padx=(10,0))
addButton.grid(row=9,column=0,pady=(10,0))


panedwindow.add(frame1,weight=1)									#Ending of frame1

#second frame(right side window)
frame2=ttk.Frame(panedwindow,width=100,height=100,relief=SUNKEN)

LabelContact=Label(frame2,text='Contacts')
contactList=Listbox(frame2)						#Adding list box and attaching it in the frame2
scrollBar=Scrollbar(frame2,orient=VERTICAL)		#Creating scrollbar and attaching it in the fram2 then orienting it vertical 
contactList.insert(1,'Amal')
contactList.insert(2,'Alex')
contactList.insert(3,'Jes')
contactList.insert(4,'saf')
contactList.insert(5,'adsfdf')
contactList.insert(6,'sfdf')
contactList.insert(7,'fdfZ')
contactList.insert(8,'sdfff')
contactList.insert(9,'dsfgrg')
contactList.insert(10,'rrg')
contactList.insert(11,'rtgrg')



LabelContact.grid(row=0,column=0,padx=(10,0),pady=(10,0),sticky=W)
contactList.grid(row=1,column=0,padx=(10,0),sticky=NSEW,rowspan=8)
scrollBar.grid(row=1,column=0,rowspan=8,sticky=N+S+E)				#gridding(packing) the scrollbar
contactList.config(yscrollcommand=scrollBar.set)					#Attaching contactList to ScrollBar,
																	#Since we need to have a vertical scroll we use yscrollcommand.

scrollBar.config(command=contactList.yview)							#setting scrollBar command parameter to contactList.
																	#yview method its yview because we need to have a vertical view
  
panedwindow.add(frame2,weight=1)									#End of frame2

root.mainloop()