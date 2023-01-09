import pyodbc
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
import login as l



def main():

    
	#window
	tkWindow = Tk()  
	tkWindow.geometry('1300x1080')  
	tkWindow.title('Registetion Form')
	windows = tkWindow
	
	load = Image.open('images/pic1.png')
	render = ImageTk.PhotoImage(load)

	img = Label (tkWindow, image = render)
	img.place(x=0,y=0,relwidth = 1, relheight = 1)
    
	frame = LabelFrame(tkWindow,bg = 'linen',padx=30,pady =10)
	frame.pack(padx=400,pady=150)
    
	def ext():
		tkWindow.destroy()
		l.main()
        
        
    


	title =   Label(frame,bg = 'linen',text = "Register HERE",font=("times new roman",20,"bold"),fg = "red").pack()
	Label(frame,text="").pack()
	
			
	global e1
	global e2
    
    
    
    
    
    
	#username label and text entry box
	usernameLabel = Label(frame,bg = 'linen',text = "Username",font=("times new roman",15,"bold")).pack()
	username = StringVar()
	e1 = Entry(frame,highlightbackground = 'linen')
	e1.pack()


	#password label and password entry box
	passwordLabel = Label(frame,bg = 'linen',text = "Password",font=("times new roman",15,"bold")).pack()
	password = StringVar()
	e2 =  Entry(frame, show='*',highlightbackground = 'linen')
	e2.pack()

	def register():


		server = 'sql.bsite.net\MSSQL2016'
		database = 'fasihmuhammad_'
		username = 'fasihmuhammad_'
		password = 'fasih123@'
		con = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password) 
		print("Database connected")



		messagebox.showinfo("Registered", "User Name and Password Created successfully...")
       
        

		u = e1.get()
		p = e2.get()
  
		try:
		

			query_to_insert = """
			INSERT into usertable values('{}','{}');  
			""".format( u,p )
			
			cur = con.cursor()
			cur.execute(query_to_insert)
			con.commit()
			#lastid = cur.lastrowid
			e1.delete(0,END)
			e2.delete(0,END)
			e1.focus_set()
			
			
		except Exception as e:
			print(e)
			con.rollback()
			con.close()


	#login button

	Button(frame,highlightbackground = 'linen',height = 1, width = 17,text = "Entre",command=register).pack()
	Label(tkWindow,text="",bg = 'linen').pack()
	Button(frame,highlightbackground = 'linen',height = 1,width = 10, text = "Exit",command=ext).pack()  
	  
	tkWindow.mainloop()