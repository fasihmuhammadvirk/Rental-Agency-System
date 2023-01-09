import pyodbc
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *




class Society:
    

    
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
 
        root.title("Society Data")


        tk.Label(root,bg='linen',text="Society Information", fg="red", font=(None, 30)).place(x=400, y=20)
         
        tk.Label(root,bg = 'linen', text="Society Name").place(x=10, y=10)
        Label(root, bg='linen',text="Rating").place(x=10, y=40)
        Label(root, bg='linen',text="Sector").place(x=10, y=70)
        Label(root, bg='linen',text="Market").place(x=10, y=100)
        Label(root, bg='linen',text="Location").place(x=10, y=130)
        Label(root, bg='linen',text="Consist Of").place(x=10, y=160)
 
        
        scrollbar= ttk.Scrollbar(root, orient= 'vertical')
        scrollbar.pack(side= RIGHT, fill= BOTH)

        reg = root.register (self.correct)
        regs = root.register (self.correct_s)
        
         
        e1 = Entry(root,highlightbackground = 'linen')
        e1.place(x=140, y=10)
        
 
        e2 = Entry(root,highlightbackground = 'linen')
        e2.place(x=140, y=40)
        e2.config(validate="key", validatecommand=(reg,'%P'))
        
         
        e3 = Entry(root,highlightbackground = 'linen')
        e3.place(x=140, y=70)
        e3.config(validate="key", validatecommand=(reg,'%P'))
        
         
        e4 = Entry(root,highlightbackground = 'linen')
        e4.place(x=140, y=100)
        e4.config(validate="key", validatecommand=(reg,'%P'))
        
        
        e5 = Entry(root,highlightbackground = 'linen')
        e5.place(x=140, y=130)
        e5.config(validate="key", validatecommand=(regs,'%S'))
        
        
        e6 = Entry(root,highlightbackground = 'linen')
        e6.place(x=140, y=160)
        e6.config(validate="key", validatecommand=(regs,'%S'))
        
        
        def ext():
           # root.destroy()
            self.windows.destroy()
        
        
        Button(root,highlightbackground = 'linen', text="Add",command = self.society_information,height=2, width= 13).place(x=10, y=190)
        Button(root,highlightbackground = 'linen', text="Delete",command = self.delete ,height=2, width= 13).place(x=160, y=190)
        Button(root,highlightbackground = 'linen', text="Update",command = self.update ,height=2, width= 13).place(x=310, y=190)
        Button(root,highlightbackground = 'linen', text="Main Menu",command = ext ,height=2, width= 13).place(x=460, y=190)
        
        
        
        
        cols = ('Society Name', 'Rating', 'Sector','Market','Location','Consist Of')
        self.listBox = ttk.Treeview(root,height=23, columns=cols, show='headings' )
              
        i = 1
        for col in cols:
            self.listBox.column("#{}".format(i),anchor=CENTER, stretch=NO, width=215)
            self.listBox.heading(col, text=col)
            #self.listBox.grid(row=1, column=0, columnspan=1)
            self.listBox.place(x= 5, y=240)
            i = i + 1

         
        self.show()
        self.listBox.bind('<Double-Button-1>',self.GetValue)
         
        root.mainloop()  
        
        
        
    def society_information(self):
        
        messagebox.showinfo("information", "Information Inserted successfully...")
       
            
        server = 'sql.bsite.net\MSSQL2016'
        database = 'fasihmuhammad_' 
        username = 'fasihmuhammad_' 
        password = 'fasih123@' 
        con = pyodbc.connect('DRIVER={/usr/local/lib/libmsodbcsql.17.dylib};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)  
        print("Database Connected ")

    
        society_name = e1.get()
        rating = e2.get()
        sectors = e3.get()
        Markets = e4.get()
        Address = e5.get()
        Consist_of = e6.get()
        
        try:
        
            query_to_insert = """
            insert into society_information values('{}',{},{},{},'{}','{}');  
            """.format(
            society_name,
            rating,sectors,
            Markets,
            Address,
            Consist_of
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
        
        society_name = e1.get()
        rating = e2.get()
        sectors = e3.get()
        Markets = e4.get()
        Address = e5.get()
        Consist_of = e6.get()
        
        server = 'sql.bsite.net\MSSQL2016'
        database = 'fasihmuhammad_' 
        username = 'fasihmuhammad_' 
        password = 'fasih123@' 
        con = pyodbc.connect('DRIVER={/usr/local/lib/libmsodbcsql.17.dylib};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)  
        print("Database Connected ")
    
        try:
           sql = "delete society_information  where Society_name = '{}';".format(society_name)
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

        messagebox.showinfo("information", "Society Information Updated successfully...")
       
            
        server = 'sql.bsite.net\MSSQL2016'
        database = 'fasihmuhammad_' 
        username = 'fasihmuhammad_' 
        password = 'fasih123@' 
        con = pyodbc.connect('DRIVER={/usr/local/lib/libmsodbcsql.17.dylib};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)  
        print("Database Connected ")
    
        society_name = e1.get()
        rating = e2.get()
        sectors = e3.get()
        Markets = e4.get()
        Address = e5.get()
        Consist_of = e6.get()
        
        try:
        
            query_to_insert = """
            update  society_information set Rating = {},Sectors ={},Markets = {},Locations = '{}',Consist_of =  '{}' where Society_name = '{}';  
            """.format(
            rating,
            sectors,
            Markets,
            Address,
            Consist_of,
            society_name
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
        e1.insert(0,select['Society Name'])
        e2.insert(0,select['Rating'])
        e3.insert(0,select['Sectors'])
        e4.insert(0,select['Markets'])
        e5.insert(0,select['Location'])
        e6.insert(0,select['Consist Of'])
        
    def show(self):
        
            server = 'sql.bsite.net\MSSQL2016'
            database = 'fasihmuhammad_' 
            username = 'fasihmuhammad_' 
            password = 'fasih123@' 
            con = pyodbc.connect('DRIVER={/usr/local/lib/libmsodbcsql.17.dylib};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)  
            print("Database Connected ")
    
        
            cur = con.cursor()
            cur.execute("SELECT * from society_information")
            records = cur.fetchall()
            print(records)
     
            for i, (society_name,rating,sectors,Markets,Address,Consist_of) in enumerate(records, start=1):
                self.listBox.insert("", "end", values=(society_name,rating,sectors,Markets,Address,Consist_of))
 
