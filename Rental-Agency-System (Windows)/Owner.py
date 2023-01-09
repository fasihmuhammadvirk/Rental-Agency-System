import pyodbc
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *

class Owner:
    
    
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
      
        root.title("Owner Data")

        tk.Label(root, bg='linen',text="Owner Information", fg="red", font=(None, 30)).place(x=400, y=20)
         
        tk.Label(root, bg='linen',text="Owner Name").place(x=10, y=10)
        Label(root,bg='linen', text="Father Name").place(x=10, y=40)
        Label(root,bg='linen', text="Contact Information").place(x=10, y=70)
        Label(root,bg='linen', text="Age").place(x=10, y=100)
        Label(root,bg='linen', text="Date Of Birth").place(x=10, y=130)
        Label(root,bg='linen', text="Cnic").place(x=10, y=160)
        
        scrollbar= ttk.Scrollbar(root, orient= 'vertical')
        scrollbar.pack(side= RIGHT, fill= BOTH)
        reg = root.register (self.correct)
        regs = root.register (self.correct_s)
                


         
        e1 = Entry(root,highlightbackground = 'linen')
        e1.place(x=140, y=10)
        e1.config(validate="key", validatecommand=(regs,'%S'))
         

        e2 = Entry(root,highlightbackground = 'linen')
        e2.place(x=140, y=40)
        e1.config(validate="key", validatecommand=(regs,'%S'))
        

        e3 = Entry(root,highlightbackground = 'linen')
        e3.place(x=140, y=70)
        e3.config(validate="key", validatecommand=(reg,'%S'))
        
         
        e4 = Entry(root,highlightbackground = 'linen')
        e4.place(x=140, y=100)
        e4.config(validate="key", validatecommand=(reg,'%P'))
        
        
        e5 = Entry(root,highlightbackground = 'linen')
        e5.place(x=140, y=130)
        e5.config(validate="key", validatecommand=(reg,'%S'))
        
        
        e6 = Entry(root,highlightbackground = 'linen')
        e6.place(x=140, y=160)
        e6.config(validate="key", validatecommand=(reg,'%S'))
        
        
        def ext():
           # root.destroy()
            self.windows.destroy()
        
        
        Button(root,highlightbackground = 'linen', text="Add",command = self.Owner_information,height=2, width= 13).place(x=10, y=190)
        Button(root,highlightbackground = 'linen', text="Delete",command = self.delete ,height=2, width= 13).place(x=160, y=190)
        Button(root,highlightbackground = 'linen', text="Update",command = self.update ,height=2, width= 13).place(x=310, y=190)
        Button(root,highlightbackground = 'linen', text="Main Menu",command = ext ,height=2, width= 13).place(x=460, y=190)
        
        cols = ('Owner Name', 'Father Name', 'Contact Information','Age','Date Of Birth','Cnic')
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
        
    def Owner_information(self):
        
        messagebox.showinfo("information", "Owner Information Inserted successfully...")
       
        server = 'sql.bsite.net\MSSQL2016'
        database = 'fasihmuhammad_' 
        username = 'fasihmuhammad_' 
        password = 'fasih123@' 
        con = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)  
        print("Database Connected ")
 
        owner_name = e1.get()
        father_name = e2.get()
        contact_information = e3.get()
        age = e4.get()
        date_of_birth = e5.get()
        cnic = e6.get()
        
        try:
        
            query_to_insert = """
            insert into owners_information values('{}','{}',{},{},'{}','{}');  
            """.format(
            owner_name ,
            father_name ,
            contact_information ,
            age ,
            date_of_birth ,
            cnic 
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
        
        owner_name = e1.get()
        father_name = e2.get()
        contact_information = e3.get()
        age = e4.get()
        date_of_birth = e5.get()
        cnic = e6.get()
        
        server = 'sql.bsite.net\MSSQL2016'
        database = 'fasihmuhammad_' 
        username = 'fasihmuhammad_' 
        password = 'fasih123@' 
        con = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)  
        print("Database Connected ")
 
        try:
           sql = "DELETE owners_information where cnic = '{}';".format(cnic)
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

        messagebox.showinfo("Information", "Owner Information Updated successfully...")
       
            
        server = 'sql.bsite.net\MSSQL2016'
        database = 'fasihmuhammad_' 
        username = 'fasihmuhammad_' 
        password = 'fasih123@' 
        con = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)  
        print("Database Connected ")
 
        owner_name = e1.get()
        father_name = e2.get()
        contact_information = e3.get()
        age = e4.get()
        date_of_birth = e5.get()
        cnic = e6.get()
        
        try:
        
            query_to_insert = """
            update owners_information set  owner_name =  '{}',father_name = '{}',contact_information = {},age = {},date_of_birth = '{}' where cnic = '{}';  
            """.format(
            owner_name ,
            father_name ,
            contact_information ,
            age ,
            date_of_birth ,
            cnic 
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
        e1.insert(0,select['Owner Information'])
        e2.insert(0,select['Father Name'])
        e3.insert(0,select['Contact Information'])
        e4.insert(0,select['Age'])
        e5.insert(0,select['Date Of Birth'])
        e6.insert(0,select['Cnic'])
        
    def show(self):
        
            server = 'sql.bsite.net\MSSQL2016'
            database = 'fasihmuhammad_' 
            username = 'fasihmuhammad_' 
            password = 'fasih123@' 
            con = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)  
            print("Database Connected ")

            cur = con.cursor()
            cur.execute("SELECT * from owners_information")
            records = cur.fetchall()
            print(records)
     
            for i, (owner_name ,father_name ,contact_information ,age ,date_of_birth ,cnic ) in enumerate(records, start=1):
                self.listBox.insert("", "end", values=(owner_name ,father_name ,contact_information ,age ,date_of_birth ,cnic))
                #con.close()    
