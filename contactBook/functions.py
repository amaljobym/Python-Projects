import sqlite3
from tkinter import *
from tkinter import messagebox
import GUI

def create_db():
	con=sqlite3.connect('database.db')
	cursr=con.cursor()
	cursr.execute("""CREATE TABLE IF NOT EXISTS profiles(
		rowid INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT,
		address TEXT,
		phone TEXT,
		email TEXT)""")

	con.commit()
	con.close()

def delete_entry(name,address,phone,email):
	name.delete(0,END)
	address.delete(0,END)
	phone.delete(0,END)
	email.delete(0,END)


def add(box,name,address,phone,email):
	if len(name.get()) == 0 and len(phone.get())==0:
		response=messagebox.showerror("fields")
		delete_entry(name,address,phone,email)
	else:
		con=sqlite3.connect('database.db')
		cursr=con.cursor()
		cursr.execute("""INSERT INTO profiles(name,address,phone,email) VALUES
			(:fname,:address,:ph,:email)""",
			{'fname':name.get(),
			'address':address.get(),
			'ph':phone.get(),
			'email':email.get()})
		con.commit()
		con.close()
		con=sqlite3.connect('database.db')
		cursr=con.cursor()
		cursr.execute("SELECT * FROM profiles")
		row=cursr.fetchall()
		print(row)
		con.commit()
		con.close()
		delete_entry(name,address,phone,email)
	show_listbox(box)

def show_listbox(box):
	box.delete(0,END)
	contctList=[]
	con=sqlite3.connect('database.db')
	cursr=con.cursor()
	cursr.execute("SELECT * FROM profiles")
	data=cursr.fetchall()
	con.commit()
	con.close()
	for i in data:
		contctList.append(i)
	for i in contctList:
		box.insert(END,'{} {}'.format(i[0],i[1]))
	#Display(id_s,name,address,number,email)

def select_item(contacts):
	global person_id
	selected_item=contacts.curselection()
	profile=contacts.get(selected_item)
	person=profile.split(' ')
	person_id=person[0]
	print(person_id)

def Display(contacts,name,address,number,email):
	select_item(contacts)
	dataList=[]
	#global person_id
	con=sqlite3.connect('database.db')
	cursr=con.cursor()
	cursr.execute('SELECT * FROM profiles WHERE rowid=?',(person_id,))
	data=cursr.fetchall()
	con.commit()
	con.close()
	for i in data:
		for j in i:
			dataList.append(j)
	print(dataList)

	delete_entry(name,address,number,email)

	name.insert(0,dataList[1])
	address.insert(0,dataList[2])
	number.insert(0,dataList[3])
	email.insert(0,dataList[4])

def edit(contacts,name,address,number,email):
	select_item(contacts)
	con=sqlite3.connect('database.db')
	cursr=con.cursor()
	cursr.execute("""UPDATE profiles SET
		name=:fname,
		address=:address,
		phone=:ph,
		email=:email WHERE rowid=:id""",
		{'fname':name.get(),
		'address':address.get(),
		'ph':number.get(),
		'email':email.get(),
		'id':person_id})
	con.commit()
	con.close()

def delete(contacts):
	select_item(contacts)
	con=sqlite3.connect('database.db')
	cursr=con.cursor()
	cursr.execute("DELETE FROM profiles WHERE rowid="+person_id)
	con.commit()
	con.close()
	show_listbox(contacts)


