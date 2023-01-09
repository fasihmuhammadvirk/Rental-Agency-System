import pyodbc
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import menu as m 
from PIL import Image , ImageTk
import registration as r 



#connecting to the database
server = 'sql.bsite.net\MSSQL2016'
database = 'fasihmuhammad_' 
username = 'fasihmuhammad_' 
password = 'fasih123@' 
con = pyodbc.connect('DRIVER={/usr/local/lib/libmsodbcsql.17.dylib};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)  
print("Database Connected ")

cursordb = con.cursor()


def main():
    
   global root2 
   root2 = Tk()
   root2.title("Login System")
   root2.geometry("1300x1080")
   
   def Exit():
      root2.destroy()
   
   global username_verification
   global password_verification
   

   
   load = Image.open('images/pic1.png')
   render = ImageTk.PhotoImage(load)
   img = Label (root2, image = render)
   img.place(x=0,y=0,relwidth = 1, relheight = 1)
   
   frame = LabelFrame(root2,bg = 'linen',padx=30,pady =10)
   frame.pack(padx=400,pady=150)
   
   


   Label(frame,text='Login to Rent and Sale',bg = 'linen', bd=20, font=('times new roman', 20, 'bold'), relief="groove",width=300).pack( padx=10, pady=10)
   
   username_verification = StringVar()
   password_verification = StringVar()
   
   
   Label(frame, bg = 'linen',text="").pack()
   Label(frame, bg = 'linen',text="Username :", font=('times new roman',12, 'bold')).pack()
   Entry(frame, textvariable=username_verification,highlightbackground = 'linen').pack()
   
   Label(frame,text= "",bg = 'linen').pack()
   
   Label(frame, bg = 'linen',text="Password :", font=('times new roman', 12, 'bold')).pack()
   Entry(frame, textvariable=password_verification, show="*",highlightbackground = 'linen').pack()
   
   Label(frame,text= "",bg = 'linen').pack()

   
    
   def reg():
       root2.destroy()
       r.main()
       
   Button(frame,highlightbackground = 'linen',text='Log In', height=1,width= 20 , bd=8, font=('times new roman', 12, 'bold'), relief="groove",command= login_verification).pack()
   Button(frame, highlightbackground = 'linen',text="Register",height = 1 ,width = 20, relief="groove", font=('times new roman', 12, 'bold'),command= reg ).pack()
   Button(frame,highlightbackground = 'linen',text='Exit', height="1",width="20", bd=8, font=('times new roman', 12, 'bold'), relief="groove",command=Exit).pack()
   
   root2.mainloop()
   
def logged_destroy():
   logged_message.destroy()
   root2.destroy()
 
def failed_destroy():
   failed_message.destroy()


def call_again():
   root2.destroy()
   m.main()

   
def logged():
   global logged_message
   logged_message = Toplevel(root2)
   logged_message.title("Welcome")
   logged_message.config(bg = 'linen')
   logged_message.geometry("500x100+390+350")
   Label(logged_message, bg = 'linen',text="Login Successfully!... Welcome {} ".format(username_verification.get()), fg="green", font="bold").pack()
   Label(logged_message, bg = 'linen',text="").pack()
   Button(logged_message, highlightbackground = 'linen',text="Welcome", relief="groove", font=('times new roman', 12, 'bold'), command=call_again).pack()
    
 
def failed():
   global failed_message
   failed_message = Toplevel(root2)
   failed_message.config(bg = 'linen')
   failed_message.title("Invalid Message")
   failed_message.geometry("500x100+390+350")
   Label(failed_message,bg = 'linen', text="Invalid Username or Password", font="bold").pack()
   Label(failed_message, bg = 'linen',text="").pack()
   Button(failed_message,highlightbackground = 'linen',text="Ok", relief="groove", font=('times new roman', 12, 'bold'), command=failed_destroy).pack()
    
 
def login_verification():
   user_verification = username_verification.get()
   pass_verification = password_verification.get()
   sql = "SELECT * from usertable where username = '{}' and user_password = '{}';".format(user_verification,pass_verification)
   cursordb.execute(sql)
   results = cursordb.fetchall()
   if results:
      for i in results:
         logged()
         break
   else:
      failed()
