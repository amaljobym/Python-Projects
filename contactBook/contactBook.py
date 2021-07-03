from tkinter import *
from tkinter import ttk
import GUI
import functions

class Contact_book:
	def __init__(self,mainFrame):
		self._rootwindow=mainFrame

		#creating the database
		functions.create_db()

		#importing the GUI
		GUI.GUI(self._rootwindow)



root=Tk()
rootwindow=Contact_book(root)
root.mainloop()