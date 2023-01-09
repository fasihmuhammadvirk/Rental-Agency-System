import pyodbc
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *

class RENT:


    
    def correct (self,inp):

        if inp == '-' :
            return True 
        elif inp.isdigit():
            return True
        elif inp == "":
            return True  
        else:
            return False

    def correct_s (self,inp):

        if inp.isdigit():
            return False
        elif inp == "":
            return True  
        else:
            return True 



                
    
    def main(self):
              
        root = Tk()
        self.windows = root
        root.geometry("1300x1080")
        global e1
        global e2
        global e3
        global e4
        global e5
        global e6
        
        root.config(bg = 'linen')
         
        root.title("Rented House & Apartments Data")

         
        tk.Label(root, bg='linen',text="Rented Apartments Information", fg="red", font=(None, 30)).place(x=400, y=20)
         
        tk.Label(root, bg='linen',text="User Cnic").place(x=10, y=10)
        Label(root, bg='linen',text="Apartment ID ").place(x=10, y=40)
        Label(root, bg='linen',text="Owners Cnic").place(x=10, y=70)
        Label(root, bg='linen',text="Society Name").place(x=10, y=100)
        Label(root, bg='linen',text="Contract Statring Date").place(x=10, y=130)
        Label(root, bg='linen',text="Contract Ending Date").place(x=10, y=160)

        reg = root.register (self.correct)
        regs = root.register (self.correct_s)
        
        
         
        e1 = Entry(root,highlightbackground = 'linen')
        e1.place(x=150, y=10)
        e1.config(validate="key", validatecommand=(reg,'%S'))
        

        e2 = Entry(root,highlightbackground = 'linen')
        e2.place(x=150, y=40)
        e2.config(validate="key", validatecommand=(reg,'%P'))
        

        e3 = Entry(root,highlightbackground = 'linen')
        e3.place(x=150, y=70)
        e3.config(validate="key", validatecommand=(reg,'%S'))
         
        e4 = Entry(root,highlightbackground = 'linen')
        e4.place(x=150, y=100)
        e4.config(validate="key", validatecommand=(regs,'%S'))
        
        
        e5 = Entry(root,highlightbackground = 'linen')
        e5.place(x=150, y=130)
        e5.config(validate="key", validatecommand=(reg,'%S'))
        
        e6 = Entry(root,highlightbackground = 'linen')
        e6.place(x=150, y=160)
        e6.config(validate="key", validatecommand=(reg,'%S'))

        def ext():
           # root.destroy()
            self.windows.destroy()
        
        
        
        scrollbar= ttk.Scrollbar(root, orient= 'vertical')
        scrollbar.pack(side= RIGHT, fill= BOTH)

         


        Button(root,highlightbackground = 'linen', text="Add",command = self.Rented_Apartment,height=2, width= 13).place(x=10, y=190)
        Button(root,highlightbackground = 'linen', text="Delete",command = self.delete ,height=2, width= 13).place(x=160, y=190)
        Button(root,highlightbackground = 'linen', text="Update",command = self.update ,height=2, width= 13).place(x=310, y=190)
        Button(root,highlightbackground = 'linen', text="Main Menu",command = ext ,height=2, width= 13).place(x=460, y=190)
        
        
        
        cols = ('User Cnic', 'Apartment ID', 'Owners Cnic','Society Name','Contract Starting Date','Contract Endign Date')
        self.listBox = ttk.Treeview(root,height=23, columns=cols, show='headings' )
              
        i = 1
        for col in cols:
            self.listBox.column("#{}".format(i),anchor=CENTER, stretch=NO, width=220)
            self.listBox.heading(col, text=col)
            #self.listBox.grid(row=1, column=0, columnspan=1)
            self.listBox.place(x= 5, y=240)
            i = i + 1
 
        self.show()
        self.listBox.bind('<Double-Button-1>',self.GetValue)
         
        root.mainloop()  
        
    def Rented_Apartment(self):
        
        messagebox.showinfo("information", "Rented Apartment Information Inserted successfully...")
       
            
        server = 'sql.bsite.net\MSSQL2016'
        database = 'fasihmuhammad_' 
        username = 'fasihmuhammad_' 
        password = 'fasih123@' 
        con = pyodbc.connect('DRIVER={/usr/local/lib/libmsodbcsql.17.dylib};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)  
        print("Database Connected ")
        
        user_cnic = e1.get()
        apartment_id = e2.get()
        owner_cnic = e3.get()
        society_name = e4.get()
        contract_starting_date = e5.get()
        contract_ending_date = e6.get()
        
        try:
        
            query_to_insert = """
            insert into  Rented_Apartments_House values('{}','{}','{}','{}','{}','{}');  
            """.format(
            user_cnic ,
            apartment_id ,
            owner_cnic ,
            society_name ,
            contract_starting_date ,
            contract_ending_date 
            )
            cur = con.cursor()
            cur.execute(query_to_insert)
            con.commit()
            lastid = cur.lastrowid
            
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e5.delete(0, END)
            e6.delete(0, END)
            e1.focus_set()
            
            
        except Exception as e:
            print(e)
            con.rollback()
            con.close()
            
    def delete(self):

        messagebox.showinfo("information", "Record Deleteeeee successfully...")
        
        user_cnic = e1.get()
        apartment_id = e2.get()
        owner_cnic = e3.get()
        society_name = e4.get()
        contract_starting_date = e5.get()
        contract_ending_date = e6.get()
        
        server = 'sql.bsite.net\MSSQL2016'
        database = 'fasihmuhammad_' 
        username = 'fasihmuhammad_' 
        password = 'fasih123@' 
        con = pyodbc.connect('DRIVER={/usr/local/lib/libmsodbcsql.17.dylib};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)  
        print("Database Connected ")
        try:
           sql = "DELETE Rented_Apartments_House where User_Cnic = '{}' and Owner_Cnic ='{}';".format(user_cnic,owner_cnic)
           cur = con.cursor()
           cur.execute(sql)
           con.commit()
           lastid = cur.lastrowid
           
           e1.delete(0, END)
           e2.delete(0, END)
           e3.delete(0, END)
           e4.delete(0, END)
           e5.delete(0, END)
           e6.delete(0, END)
           e1.focus_set()
            
        except Exception as e:
     
           print(e)
           con.rollback()
           con.close()


    def update(self):
        messagebox.showinfo("information", "Rented Apartment Information Updated successfully...")
       
            
        server = 'sql.bsite.net\MSSQL2016'
        database = 'fasihmuhammad_' 
        username = 'fasihmuhammad_' 
        password = 'fasih123@' 
        con = pyodbc.connect('DRIVER={/usr/local/lib/libmsodbcsql.17.dylib};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)  
        print("Database Connected ")
  
        user_cnic = e1.get()
        apartment_id = e2.get()
        owner_cnic = e3.get()
        society_name = e4.get()
        contract_starting_date = e5.get()
        contract_ending_date = e6.get()
        
        try:
        
            query_to_insert = """
            update Rented_Apartments_House set User_Cnic = '{}',Owner_Cnic = '{}',Society_Name = '{}',Contract_Starting_Date = '{}',Contract_Expire_On'{}' where Apartment_ID = '{}';  
            """.format(
            user_cnic ,
            apartment_id ,
            owner_cnic ,
            society_name ,
            contract_starting_date ,
            contract_ending_date 
            )
            cur = con.cursor()
            cur.execute(query_to_insert)
            con.commit()
            lastid = cur.lastrowid
            
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e5.delete(0, END)
            e6.delete(0, END)
            e1.focus_set()
            
            
        except Exception as e:
            print(e)
            con.rollback()
            con.close()


        
    def GetValue(self,event):
        
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        row_id = self.listBox.selection()[0]
        select = self.listBox.set(row_id)
        e1.insert(0,select['User Cnic'])
        e2.insert(0,select['Apartment ID'])
        e3.insert(0,select['Owner Cnic'])
        e4.insert(0,select['Society Name'])
        e5.insert(0,select['Contract Starting Date'])
        e6.insert(0,select['Contract Ending Date'])
        
    def show(self):
        
            server = 'sql.bsite.net\MSSQL2016'
            database = 'fasihmuhammad_' 
            username = 'fasihmuhammad_' 
            password = 'fasih123@' 
            con = pyodbc.connect('DRIVER={/usr/local/lib/libmsodbcsql.17.dylib};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)  
            print("Database Connected ")
    
        
            cur = con.cursor()
            cur.execute("SELECT * from Rented_Apartments_House;")
            records = cur.fetchall()
            print(records)
     
            for i, ( user_cnic,apartment_id ,owner_cnic ,society_name ,contract_starting_date ,contract_ending_date ) in enumerate(records, start=1):
                self.listBox.insert("", "end", values=(user_cnic,apartment_id ,owner_cnic ,society_name ,contract_starting_date ,contract_ending_date))
                #con.close()    
 