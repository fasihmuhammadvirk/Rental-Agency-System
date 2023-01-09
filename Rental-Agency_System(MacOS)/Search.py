import pyodbc 
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
import goto as g




def main():

    root2 = Tk()
    root2.geometry("1300x1080")
    windows = root2

    bg = Image.open('images/pic1.png')
    ic = ImageTk.PhotoImage(bg)

    bgimg = Label (root2, image = ic)
    bgimg.place(x=0,y=0,relwidth = 1, relheight = 1)
    
    root = LabelFrame(root2,bg = 'linen',padx=30,pady =10)
    root.pack(padx=400,pady=150)
    def ext():
        windows.destroy()
        
    def call():
        root2.destroy()
        g.main()
        
    root2.title("Search")
    
    
    tk.Label(root,bg = 'linen',text='Search Data Here', bd=20, font=('times new roman', 20, 'bold'), relief="groove",width=300).pack()
    Label(root,text="",bg = 'linen').pack()


    Button(root,highlightbackground = 'linen', text="Societies",command =select_s ,height=1, width= 16).pack()
    Button(root,highlightbackground = 'linen', text="Customer Information",command = select_c,height=1, width= 16).pack()
    Button(root,highlightbackground = 'linen', text="Owner Information",command = select_o,height=1, width= 16).pack()
    Button(root,highlightbackground = 'linen', text="Rented Apartment",command = select_r,height=1, width= 16).pack() 
    Button(root,highlightbackground = 'linen', text="Sale Information",command = select_fs,height=1, width= 16).pack()
    Button(root,highlightbackground = 'linen', text="Rent Information",command = select_fr ,height=1, width= 16).pack()
    Button(root,highlightbackground = 'linen', text="Quit",command = call,height=1, width= 7).pack()
    
    root2.mainloop()


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
    elif inp == '-' :
        return True 
    elif inp.isupper() or inp.islower():
        return True 
    elif inp == "":
        return True  
    else:
        return False




#------- For rent A/H search ----------------



def select_fr():

    root = Tk()
    root.geometry("1300x1080")
    windows = root

    root.config(bg = 'linen')
    
    def ext():
        windows.destroy()

    def call_other():
        windows.destroy()
        search_fr()

 
    root.title("Searched Data")
   

    global r_id
    


    tk.Label(root,bg = 'linen',text='Search For Rent A/H Information', bd=20, font=('times new roman', 20, 'bold'), relief="groove",width=300).pack()
    Label(root,bg = 'linen',text="").pack()


    tk.Label(root,bg = 'linen', text="Enter Apartment / House ID",font=('times new roman', 20, 'bold')).pack()
    Label(root,bg = 'linen',text="").pack()



    
    r_id  = Entry(root,highlightbackground = 'linen')
    r_id.pack()
    reg = root.register (correct)
    r_id.config(validate="key", validatecommand=(reg,'%P'))
         


    
    Button(root,highlightbackground = 'linen', text="Search",command = search_fr ,height=1, width= 10).pack()  
    Button(root,highlightbackground = 'linen', text="Go Back",command = ext ,height=1, width= 10).pack()

    root.mainloop()  

def search_fr():


    root = Tk()
    root.geometry("1300x1080")
    windows = root

    root.config(bg = 'linen')

    root.title("Searched Data")


    def ext():
        windows.destroy()
    
    Button(root,highlightbackground = 'linen', text="Go Back",command = ext ,height=1, width= 10).pack() 
    Label(root,bg = 'linen',text="").pack()



    cols = ('Apartment_ID','Space','Bedrooms','House_number' , 'Sector', 'Street', 'Owner', 'Contract', 'Rent', 'Year_of_construction','Rent Status','Rented_to','society')
    listBox = ttk.Treeview(root, columns=cols, show='headings')
               
    i = 1
    for col in cols:
        listBox.column("#{}".format(i),anchor=CENTER, stretch=NO, width=220)
        listBox.heading(col, text=col)
        #listBox.grid(row=1, column=0, columnspan=1)
        listBox.place(x= 5, y=40)
        i = i + 1

        server = 'sql.bsite.net\MSSQL2016'
        database = 'fasihmuhammad_' 
        username = 'fasihmuhammad_' 
        password = 'fasih123@' 
        con = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)  
        print("Database Connected ")

    fr_id = r_id.get()

    query = """
        SELECT * from for_rent_house_and_apartments where Apartment_ID = '{}';
        """.format(fr_id)


    cur = con.cursor()
    cur.execute(query)
    records = cur.fetchall()
    print(records)

    
    for i, ( Apartment_ID, Space,Bedrooms,House_number , Sector, Street, Owner, Contract,Rent, Year_of_construction,rent_status,rented_to,society ) in enumerate(records, start=1):

        listBox.insert("", "end", values=(Apartment_ID, Space,Bedrooms,House_number , Sector, Street, Owner, Contract,Rent, Year_of_construction,rent_status,rented_to,society))
        #con.close()    
   





#------ For sale A/H Search ------------------


def select_fs():

    root = Tk()
    root.geometry("1300x1080")
    windows = root
    root.config(bg = 'linen')
    def ext():
        windows.destroy()
    
    def call_other():
        windows.destroy()
        search_fs()

    global s_id
 
    root.title("Searched Data")
   

    tk.Label(root,bg = 'linen',text='Search For Sale A/H Information', bd=20, font=('times new roman', 20, 'bold'), relief="groove",width=300).pack()
    Label(root,bg = 'linen',text="").pack()


    tk.Label(root, bg = 'linen',text="Enter Apartment / House ID",font=('times new roman', 20, 'bold')).pack()
    Label(root,bg = 'linen',text="").pack()



    s_id  = Entry(root,highlightbackground = 'linen')
    s_id.pack()
    reg = root.register (correct)
    s_id.config(validate="key", validatecommand=(reg,'%P'))


    
    Button(root,highlightbackground = 'linen', text="Search",command = search_fs ,height=1, width= 10).pack() 
    Button(root,highlightbackground = 'linen', text="Go Back",command = ext ,height=1, width= 10).pack()  



    root.mainloop()  

def search_fs():


    root = Tk()
    root.geometry("1300x1080")
    windows = root

    root.config(bg = 'linen')        

    root.title("Searched Data")


    def ext():
        windows.destroy()

    
    Button(root,highlightbackground = 'linen', text="Go Back",command = ext ,height=1, width= 10).pack()  
    Label(root,bg = 'linen',text="").pack()



    cols = ('Apartment_ID','Space','Bedrooms','House_number' , 'Sector', 'Street', 'Owner', 'Contract', 'Price', 'Sale_status','Year_of_construction','society')
    listBox = ttk.Treeview(root, columns=cols, show='headings')
                  
    i = 1
    for col in cols:
        listBox.column("#{}".format(i),anchor=CENTER, stretch=NO, width=220)
        listBox.heading(col, text=col)
        #listBox.grid(row=1, column=0, columnspan=1)
        listBox.place(x= 5, y=40)
        i = i + 1

            
        server = 'sql.bsite.net\MSSQL2016'
        database = 'fasihmuhammad_' 
        username = 'fasihmuhammad_' 
        password = 'fasih123@' 
        con = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)  
        print("Database Connected ")

    fs_id = s_id.get()

    query = """
        SELECT * from for_sale_house_and_apartments where Apartment_ID = '{}';
        """.format(fs_id)


    cur = con.cursor()
    cur.execute(query)
    records = cur.fetchall()
    print(records)

    
    for i, ( Apartment_ID, Space,Bedrooms,House_number , Sector, Street, Owner, Contract,Price, Sale_status,Year_of_construction,society ) in enumerate(records, start=1):
        listBox.insert("", "end", values=(Apartment_ID, Space,Bedrooms,House_number , Sector, Street, Owner, Contract,Price, Sale_status,Year_of_construction,society))
        #con.close()      



#--------- Rented Apartment Search ------------

def select_r():

    root = Tk()
    root.geometry("1300x1080")
    windows = root
    root.config(bg = 'linen')
    def ext():
        windows.destroy()

    def call_other():
        windows.destroy()
        search_r()

 
    root.title("Searched Data")

   

    global A_ID
    

    tk.Label(root,bg = 'linen',text='Search Rented A/H Information', bd=20, font=('times new roman', 20, 'bold'), relief="groove",width=300).pack()
    Label(root,text="").pack()


    tk.Label(root,bg = 'linen', text="Enter Apartment / House ID",font=('times new roman', 20, 'bold')).pack()
    Label(root,bg = 'linen',text="").pack()




    A_ID  = Entry(root,highlightbackground = 'linen')
    A_ID.pack()
    reg = root.register (correct)
    A_ID.config(validate="key", validatecommand=(reg,'%P'))

    
    Button(root,highlightbackground = 'linen', text="Search",command = search_r ,height=1, width= 10).pack()  
    Button(root, highlightbackground = 'linen',text="Go Back",command = ext ,height=1, width= 10).pack()



    root.mainloop()  

def search_r():


    root = Tk()
    root.geometry("1300x1080")
    windows = root

    root.config(bg = 'linen')

    root.title("Searched Data")

    def ext():
        windows.destroy()
    
    Button(root,highlightbackground = 'linen', text="Go Back",command = ext ,height=1, width= 10).pack()
    Label(root,bg = 'linen',text="").pack()
  


    cols = ('User Cnic', 'Apartment ID', 'Owners Cnic','Society Name','Contract Starting Date','Contract Endign Date')
    listBox = ttk.Treeview(root, columns=cols, show='headings' )
                  
    i = 1
    for col in cols:
        listBox.column("#{}".format(i),anchor=CENTER, stretch=NO, width=220)
        listBox.heading(col, text=col)
        #listBox.grid(row=1, column=0, columnspan=1)
        listBox.place(x= 5, y=40)
        i = i + 1

    
        server = 'sql.bsite.net\MSSQL2016'
        database = 'fasihmuhammad_' 
        username = 'fasihmuhammad_' 
        password = 'fasih123@' 
        con = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)  
        print("Database Connected ")

    ap_id = A_ID.get()

    query = """
        SELECT * from Rented_Apartment_House where Apartment_ID = '{}';
        """.format(ap_id)


    cur = con.cursor()
    cur.execute(query)
    records = cur.fetchall()
    print(records)

    
    for i, ( user_cnic,apartment_id ,owner_cnic ,society_name ,contract_starting_date ,contract_ending_date ) in enumerate(records, start=1):
        listBox.insert("", "end", values=(user_cnic,apartment_id ,owner_cnic ,society_name ,contract_starting_date ,contract_ending_date))
        #con.close()    



# -------Owner Search --------------


def select_o():

    root = Tk()
    root.geometry("1300x1080")
    windows = root
    root.config(bg = 'linen')
    def ext():
        windows.destroy()

    def call_other():
        windows.destroy()
        search_o()

    root.title("Searched Data")

    

    global cnic_o 
    

    tk.Label(root,bg = 'linen',text='Search Owner Information', bd=20, font=('times new roman', 20, 'bold'), relief="groove",width=300).pack()
    Label(root,bg = 'linen',text="").pack()


    tk.Label(root,bg = 'linen', text="Enter Owner Cnic",font=('times new roman', 20, 'bold')).pack()
    Label(root,bg = 'linen',text="").pack()


    cnic_o  = Entry(root,highlightbackground = 'linen')
    cnic_o.pack()
    reg = root.register (correct)
    cnic_o.config(validate="key", validatecommand=(reg,'%S'))


    
    Button(root, highlightbackground = 'linen',text="Search",command = search_o ,height=1, width= 10).pack() 
    Button(root, highlightbackground = 'linen',text="Go Back",command = ext ,height=1, width= 10).pack() 



    root.mainloop()  

def search_o():


    root = Tk()
    root.geometry("1300x1080")
    windows = root


    root.config(bg = 'linen')
    root.title("Searched Data")


    def ext():
        windows.destroy()
    
    Button(root, highlightbackground = 'linen',text="Go Back",command = ext ,height=1, width= 10).pack()
    Label(root,bg = 'linen',text="").pack()
  


    cols = ('Owner Name', 'Father Name', 'Contact Information','Age','Date Of Birth','Cnic')
    listBox = ttk.Treeview(root, columns=cols, show='headings' )
              
    i = 1
    for col in cols:
        listBox.column("#{}".format(i),anchor=CENTER, stretch=NO, width=220)
        listBox.heading(col, text=col)
        #listBox.grid(row=1, column=0, columnspan=1)
        listBox.place(x= 5, y=40)
        i = i + 1

    
        server = 'sql.bsite.net\MSSQL2016'
        database = 'fasihmuhammad_' 
        username = 'fasihmuhammad_' 
        password = 'fasih123@' 
        con = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)  
        print("Database Connected ")

    owner = cnic_o.get()

    query = """
        SELECT * from owners_information where cnic = '{}';
        """.format(owner)


    cur = con.cursor()
    cur.execute(query)
    records = cur.fetchall()
    print(records)

    
    for i, (owner_name ,father_name ,contact_information ,age ,date_of_birth ,cnic ) in enumerate(records, start=1):
        listBox.insert("", "end", values=(owner_name ,father_name ,contact_information ,age ,date_of_birth ,cnic))
        #con.close()    


    
#-------- Society search ------------


def select_s():

    root = Tk()
    root.geometry("1300x1080")
    windows = root
    root.config(bg = 'linen')
    def ext():
        windows.destroy()

    
    

    root.title("Searched Data")

    global society 
    
    tk.Label(root,bg = 'linen',text='Search Society Information', bd=20, font=('times new roman', 20, 'bold'), relief="groove",width=300).pack()
    Label(root,bg = 'linen',text="").pack()


    tk.Label(root, bg = 'linen',text="Enter Society Name",font=('times new roman', 20, 'bold')).pack()
    Label(root,bg = 'linen',text="").pack()


    society  = Entry(root,highlightbackground = 'linen')
    society.pack()
    
    
    Button(root,highlightbackground = 'linen', text="Search",command = search_s,height=1, width= 10).pack()  
    Button(root,highlightbackground = 'linen', text="Go Back",command = ext ,height=1, width= 10).pack()  



    root.mainloop()  

def search_s():

    root = Tk()
    root.geometry("1300x1080")
    windows = root
    root.config(bg = 'linen')
    def ext():
        windows.destroy()
    
    Button(root, highlightbackground = 'linen',text="Go Back",command = ext ,height=1, width= 10).pack()
    Label(root,bg = 'linen',text="").pack()
  

    root.title("Searched Data")


    cols = ('Society Name', 'Rating', 'Sector','Market','Location','Consist Of')
    listBox = ttk.Treeview(root, columns=cols, show='headings' )
              
    i = 1
    for col in cols:
        listBox.column("#{}".format(i),anchor=CENTER, stretch=NO, width=220)
        listBox.heading(col, text=col)
        #listBox.grid(row=1, column=0, columnspan=1)
        listBox.place(x= 5, y=40)
        i = i + 1

    
        server = 'sql.bsite.net\MSSQL2016'
        database = 'fasihmuhammad_' 
        username = 'fasihmuhammad_' 
        password = 'fasih123@' 
        con = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)  
        print("Database Connected ")


    society_name = society.get()

    query = """
        SELECT * from society_information where society_name  = '{}';
        """.format(society_name)


    cur = con.cursor()
    cur.execute(query)
    records = cur.fetchall()
    print(records)

    
    for i, (society_name,rating,sectors,Markets,Address,Consist_of) in enumerate(records, start=1):
        listBox.insert("", "end", values=(society_name,rating,sectors,Markets,Address,Consist_of))
 


#--------- customer search ----------


def select_c():

    root = Tk()
    root.geometry("1300x1080")
    windows = root
    root.config(bg = 'linen')
    def ext():
        windows.destroy()


    
    root.title("Searched Data")


    global cnic_c 
    

    tk.Label(root,bg = 'linen',text='Search Customer Information', bd=20, font=('times new roman', 20, 'bold'), relief="groove",width=300).pack()
    Label(root,bg = 'linen',text="").pack()


    tk.Label(root,bg = 'linen', text="Enter Customer Cnic",font=('times new roman', 20, 'bold')).pack()

    Label(root,bg = 'linen',text="").pack()


    cnic_c = Entry(root,highlightbackground = 'linen')
    cnic_c.pack()
    reg = root.register (correct)
    cnic_c.config(validate="key", validatecommand=(reg,'%S'))


    
    Button(root,highlightbackground = 'linen', text="Search",command = search_c ,height=1, width= 10).pack()
    Button(root, highlightbackground = 'linen',text="Go Back",command = ext ,height=1, width= 10).pack() 



    root.mainloop()  

def search_c():


    root = Tk()
    root.geometry("1300x1080")
    windows = root

    root.config(bg = 'linen')
    root.title("Searched Data")


    def ext():
        windows.destroy()
    
    Button(root,highlightbackground = 'linen',text="Go Back",command = ext ,height=1, width= 10).pack()
    Label(root,bg = 'linen',text="").pack()
  


    cols = ('Customer Name', 'Father Name', 'Contact Information','Age','Date Of Birth','Cnic')
    listBox = ttk.Treeview(root, columns=cols, show='headings' )
          
    i = 1
    for col in cols:
        listBox.column("#{}".format(i),anchor=CENTER, stretch=NO, width=220)
        listBox.heading(col, text=col)
        #listBox.grid(row=1, column=0, columnspan=1)
        listBox.place(x= 5, y=40)
        i = i + 1

    
        server = 'sql.bsite.net\MSSQL2016'
        database = 'fasihmuhammad_' 
        username = 'fasihmuhammad_' 
        password = 'fasih123@' 
        con = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)  
        print("Database Connected ")

    customer = cnic_c.get()

    query = """
        SELECT * from customer_information where cnic = '{}';
        """.format(customer)


    cur = con.cursor()
    cur.execute(query)
    records = cur.fetchall()
    print(records)

    
    for i, (customer_name ,father_name ,contact_information ,age ,date_of_birth ,cnic ) in enumerate(records, start=1):
        listBox.insert("", "end", values=(customer_name ,father_name ,contact_information ,age ,date_of_birth ,cnic))
