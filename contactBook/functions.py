import sqlite3
import GUI

def create_db():
	con=sqlite3.connect('database.db')
	cursr=con.cursor()
	cursr.execute("""CREATE TABLE IF NOT EXISTS profiles(
		name TEXT,
		address TEXT,
		phone TEXT,
		email TEXT)""")

	con.commit()
	con.close()

def add():
	con=sqlite3.connect('database.db')
	cursr=con.cursor()
	cursr.execute("INSERT INTO profiles VALUES(:fname,:address,:ph,:email)",
		{'fname':name,
		'address':address,
		'ph':phone,
		'email':email})
	con.commit()
	con.close()
