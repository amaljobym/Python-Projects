from tkinter import *
from tkinter import ttk
import GUI
import functions

class Contact_book:
	def __init__(self,mainFrame):
		self._rootwindow=mainFrame

		self.name=StringVar()
		self.address=StringVar()
		self.ph=StringVar()
		self.email=StringVar()

		#importing the GUI
		GUI.GUI(self._rootwindow)
		#creating the database
		functions.create_db()



root=Tk()
rootwindow=Contact_book(root)
root.mainloop()