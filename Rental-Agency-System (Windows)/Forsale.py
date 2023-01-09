import pyodbc
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *


class ForSale:
    
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
        c = Canvas(root, bg="white",
            height=1080, width=1080)
        global e1
        global e2
        global e3
        global e4
        global e5
        global e6
        global e7
        global e8
        global e9
        global e10
        global e11
        global e12
        
        root.config(bg = 'linen')

        root.title("For Sale House and Apartment Data")
         
        tk.Label(root,bg='linen', text="For Sale House and Apartments Information", fg="red", font=(None, 30)).place(x=400, y=20)
         
        tk.Label(root,bg='linen', text="Apartment ID").place(x=10, y=10)
        Label(root,bg='linen', text="Space").place(x=10, y=40)
        Label(root,bg='linen', text="Bedrooms").place(x=10, y=70)
        Label(root,bg='linen', text="House Number").place(x=10, y=100)
        Label(root,bg='linen', text="Sectors").place(x=10, y=130)
        Label(root,bg='linen', text="Street Number").place(x=10, y=160)
        Label(root,bg='linen', text="Owner Name").place(x=10, y=190)
        Label(root,bg='linen', text="Contract Years").place(x=10, y=220)
        Label(root,bg='linen', text="Price").place(x=10, y=250)
        Label(root,bg='linen', text="Sale Status").place(x=10, y=280)
        Label(root,bg='linen', text="Constructed In").place(x=10, y=310)
        Label(root,bg='linen', text="Society").place(x=10, y=340)


        scrollbar= ttk.Scrollbar(root, orient= 'vertical')
        scrollbar.pack(side= RIGHT, fill= BOTH)
        
        reg = root.register (self.correct)
        regs = root.register (self.correct_s)
        
         
        e1 = Entry(root,highlightbackground = 'linen')
        e1.place(x=150, y=10)
        e1.config(validate="key", validatecommand=(reg,'%P'))
        
         
        e2 = Entry(root,highlightbackground = 'linen')
        e2.place(x=150, y=40)
         
        e3 = Entry(root,highlightbackground = 'linen')
        e3.place(x=150, y=70)
        e3.config(validate="key", validatecommand=(reg,'%P'))
        
         
        e4 = Entry(root,highlightbackground = 'linen')
        e4.place(x=150, y=100)
        e4.config(validate="key", validatecommand=(reg,'%P'))

        e5 = Entry(root,highlightbackground = 'linen')
        e5.place(x=150, y=130)
        e5.config(validate="key", validatecommand=(regs,'%S'))
        
        
        e6 = Entry(root,highlightbackground = 'linen')
        e6.place(x=150, y=160)
        e6.config(validate="key", validatecommand=(reg,'%P'))
        
        
        e7 = Entry(root,highlightbackground = 'linen')
        e7.place(x=150, y=190)
        e7.config(validate="key", validatecommand=(regs,'%S'))
        
        
        
        e8 = Entry(root,highlightbackground = 'linen')
        e8.place(x=150, y=220)
        e8.config(validate="key", validatecommand=(reg,'%P'))
        
        
        e9 = Entry(root,highlightbackground = 'linen')
        e9.place(x=150, y=250)
        e9.config(validate="key", validatecommand=(reg,'%P'))
        
        
        e10 = Entry(root,highlightbackground = 'linen')
        e10.place(x=150, y=280)
        e10.config(validate="key", validatecommand=(regs,'%S'))
        
        
        e11 = Entry(root,highlightbackground = 'linen')
        e11.place(x=150, y=310)
        e11.config(validate="key", validatecommand=(reg,'%S'))
        
        
        e12 = Entry(root,highlightbackground = 'linen')
        e12.place(x=150, y=340)
        e12.config(validate="key", validatecommand=(regs,'%S'))
        

        def ext():
           # root.destroy()
            self.windows.destroy()
        
        
        
        Button(root,highlightbackground = 'linen', text="Add",command = self.For_sale_House_Apartment,height=2, width= 13).place(x=10, y=370)
        Button(root,highlightbackground = 'linen', text="Delete",command = self.delete ,height=2, width= 13).place(x=160, y=370)
        Button(root,highlightbackground = 'linen', text="Update",command = self.update ,height=2, width= 13).place(x=310, y=370)
        Button(root,highlightbackground = 'linen', text="Main Menu",command = ext ,height=2, width= 13).place(x=460, y=370)
        
        
        cols = ('Apartment_ID','Space','Bedrooms','House_number' , 'Sector', 'Street', 'Owner', 'Contract', 'Price', 'Sale_status','Year_of_construction','society')
        self.listBox = ttk.Treeview(root,height=13, columns=cols, show='headings')
        
        i = 1
        for col in cols:
            
            self.listBox.column("#{}".format(i),anchor=CENTER, stretch=NO, width=107)
            self.listBox.heading(col, text=col)
            #self.listBox.grid(row=1, column=0, columnspan=1)
            self.listBox.place(x=5, y=420)
            i = i + 1
         
       
       

        
        self.show()
        self.listBox.bind('<Double-Button-1>',self.GetValue)
        
        root.mainloop()  
        
    def For_sale_House_Apartment(self):
        
        messagebox.showinfo("Information", "For Sale Apartment Information Inserted successfully...")
       
            
        server = 'sql.bsite.net\MSSQL2016'
        database = 'fasihmuhammad_' 
        username = 'fasihmuhammad_' 
        password = 'fasih123@' 
        con = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)  
        print("Database Connected ")
    
        
        Apartment_ID = e1.get()
        Space = e2.get()
        Bedrooms= e3.get()
        House_number = e4.get()
        Sector= e5.get()
        Street= e6.get()
        Owner= e7.get()
        Contract= e8.get()
        Price= e9.get()
        Sale_status= e10.get()
        Year_of_construction= e11.get()
        society = e12.get()
        
        
        try:
        
            query_to_insert = """
        insert into for_sale_house_and_apartments values({},'{}','{}',{},'{}',{},'{}',{},{},'{}',{},'{}');
        """.format(
        
        Apartment_ID,
        Space,
        Bedrooms,
        House_number ,
        Sector,
        Street,
        Owner,
        Contract,
        Price,
        Sale_status,
        Year_of_construction,
        society
        
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
            e7.delete(0, END)
            e8.delete(0, END)
            e9.delete(0, END)
            e10.delete(0, END)
            e11.delete(0, END)
            e12.delete(0, END)
            e1.focus_set()
            
            
        except Exception as e:
            print(e)
            con.rollback()
            con.close()


    def delete(self):

        messagebox.showinfo("Information", "Record Deleteeeee successfully...")
        
        Apartment_ID = e1.get()
        Space = e2.get()
        Bedrooms= e3.get()
        House_number = e4.get()
        Sector= e5.get()
        Street= e6.get()
        Owner= e7.get()
        Contract= e8.get()
        Price= e9.get()
        Sale_status= e10.get()
        Year_of_construction= e11.get()
        society = e12.get()
        
        server = 'sql.bsite.net\MSSQL2016'
        database = 'fasihmuhammad_' 
        username = 'fasihmuhammad_' 
        password = 'fasih123@' 
        con = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)  
        print("Database Connected ")
    
        try:
           sql = "DELETE for_sale_house_and_apartments where Apartment_ID = '{}';".format(Apartment_ID)
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
           e7.delete(0, END)
           e8.delete(0, END)
           e9.delete(0, END)
           e10.delete(0, END)
           e11.delete(0, END)
           e12.delete(0, END)
           e1.focus_set()
            
        except Exception as e:
     
           print(e)
           con.rollback()
           con.close()


    def update(self):

        messagebox.showinfo("Information", "For Sale Apartment Information Updated successfully...")
       
            
        server = 'sql.bsite.net\MSSQL2016'
        database = 'fasihmuhammad_' 
        username = 'fasihmuhammad_' 
        password = 'fasih123@' 
        con = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)  
        print("Database Connected ")
    
        
        Apartment_ID = e1.get()
        Space = e2.get()
        Bedrooms= e3.get()
        House_number = e4.get()
        Sector= e5.get()
        Street= e6.get()
        Owner= e7.get()
        Contract= e8.get()
        Price= e9.get()
        Sale_status= e10.get()
        Year_of_construction= e11.get()
        society = e12.get()
        
        
        try:
        
            query_to_insert = """
        Update for_sale_house_and_apartments set Space = '{}',Bedrooms = '{}',House_number={},Sectors = '{}',Street_Number = {},Owner_Name = '{}',Contract_Years = {},Price = {},Sale_Status = '{}',year_of_construction = {},society = '{}' where Apartment_ID = {};
        """.format(
        
        Space,
        Bedrooms,
        House_number ,
        Sector,
        Street,
        Owner,
        Contract,
        Price,
        Sale_status,
        Year_of_construction,
        society,
        Apartment_ID
        
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
            e7.delete(0, END)
            e8.delete(0, END)
            e9.delete(0, END)
            e10.delete(0, END)
            e11.delete(0, END)
            e12.delete(0, END)
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
        e7.delete(0, END)
        e8.delete(0, END)
        e9.delete(0, END)
        e10.delete(0, END)
        e11.delete(0, END)
        e12.delete(0, END)
        
        row_id = self.listBox.selection()[0]
        select = self.listBox.set(row_id)
        e1.insert(0,select['Apartment ID'])
        e2.insert(0,select['space'])
        e3.insert(0,select['Bedroom'])
        e4.insert(0,select['House Number'])
        e5.insert(0,select['Sector'])
        e6.insert(0,select['Street Number'])
        e7.insert(0,select['Owner Name'])
        e8.insert(0,select['Contract yeaar'])
        e9.insert(0,select['Price'])
        e10.insert(0,select['Sale Status'])
        e11.insert(0,select['Year of Construction'])
        e12.insert(0,select['Society'])
        
    def show(self):

        
        server = 'sql.bsite.net\MSSQL2016'
        database = 'fasihmuhammad_' 
        username = 'fasihmuhammad_' 
        password = 'fasih123@' 
        con = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)  
        print("Database Connected ")
 
    
        cur = con.cursor()
        cur.execute("SELECT * from for_sale_house_and_apartments;")
        records = cur.fetchall()
        print(records)
 
        for i, ( Apartment_ID, Space,Bedrooms,House_number , Sector, Street, Owner, Contract,Price, Sale_status,Year_of_construction,society ) in enumerate(records, start=1):
            self.listBox.insert("", "end", values=(Apartment_ID, Space,Bedrooms,House_number , Sector, Street, Owner, Contract,Price, Sale_status,Year_of_construction,society))
            #con.close()    

