import pyodbc
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from PIL import Image , ImageTk
import login as l


def main():

   root2 = Tk()
   root2.title("Login System")
   root2.geometry("1300x1080")
   
   def Exit():
      root2.destroy()
     
   

   def call():   
       root2.destroy()
       l.main()

   
   load = Image.open('images/pic1.png')
   render = ImageTk.PhotoImage(load)
   img = Label (root2, image = render)
   img.place(x=0,y=0,relwidth = 1, relheight = 1)
   
   frame = LabelFrame(root2,bg = 'linen',padx=30,pady =10)
   frame.pack(padx=400,pady=150)
   
   


   Label(frame,text='Welcome to Rent and Sale',bg = 'linen', bd=20, font=('times new roman', 20, 'bold'), relief="groove",width=300).pack( padx=10, pady=10)
   

   Label(frame,text= "",bg = 'linen').pack()

   
   
   Button(frame,highlightbackground = 'linen',text='Log In', height=1,width= 20 , bd=8, font=('times new roman', 12, 'bold'), relief="groove",command= call).pack()
   Label(frame,text= "",bg = 'linen').pack()
   Button(frame,highlightbackground = 'linen',text='Exit', height="1",width="20", bd=8, font=('times new roman', 12, 'bold'), relief="groove",command=Exit).pack()
   
   root2.mainloop()
   
main()
