# Rental Agency System

# Abstract
Today we are living in an advance era surrounded with technology. So, every system needs a database in which we can store its data and we can retrieve it easily. So does a rental agency for its data to be store and retrieve smoothly. Just think if a rent agency agent must keep the record of more that 1000 houses and their owners and whom he has rented the house it would be hard to keep the record and to retrieve data from those record. So many data would be lost just because of it.
Thus, we applied the knowledge of Database System that we gained in the class and using our previous experience with python we develop an App that cover up such a problem in a Rental Agency.
Introduction
This project is designed to manage the record in a rental agency. The records of Societies, Rented Houses, House for Sale, Customers, Owners etc are being stored in the database. We can perform all basic three function on these record Addition, Deletion, Updating. We can also individually search for the record of anything from the database easily. The agent can easily maintain the record of everything easily and can also retrieve them for them database. We also provide graphic user interface so that the user can easily use the Application.

# Objective
- The main objective of our rental system is to maintain the records of Societies, Owner, Customer, House, or Apartments on rent, also for sale and those who are rented to a customer
- It helped the user who is a property agent to main the records of all entities easily.
- It helps the user to get the record faster for their client without any delay.
- This system increases the efficiency in a rental agency and better management of the agency.
- Adding a new record and fetching the old record in the records is easy.
- This system completely automates all your agency activities.
    
# Project Description
The backend was created by using SQL Server as IDE and SQL as the programming language. For our frontend, we use python programming language. In which we use tkinter library which give us many options to create an interactive interface for the user. We connect our local host database with python code and using python user interface we are performing queries on the database.
We have main seven Entities in which we are storing our Data. We can perform Addition, Deletion, Updating, Searching on these 6 Entities while the 7th Entity Usertable only store the username and password data of the admin required for the login.
 - Society:
  This table will store the information of all the Societies and description of the societies. Primary Key: Society_name
 - Owner:
This table will store the information of all the Societies and description of the societies. Primary Key: Society_name
 - Customer:
This table will store the information of all the owner who owned a house or an apartment Primary Key: cnic
  This table will store the information of all the customer who has rented a house or an apartment Primary Key: cnic
 - For Sale House and Apartment:
  This table will store the information of all the houses and apartments that are for sale. Primary Key: Apartment_ID
 - For Rent House and Apartment:
  This table will store the information of all the houses and apartments that are for sale. Primary Key: Apartment_ID
 - Rented House and Apartment:
  This table will store the information of all the houses and apartments that are rented. Primary Key: None
  
 - Usertable
This table will store the information of all the houses and apartments that are rented. Primary Key: None
  This table will store the information of the admin Username and his login Password that are required for login.
Primary Key: password
 
# Conclusion
The project computerizes the work in a rental agency, it is more convenient than manual system. The computerization makes the managing process fast, safe, and reliable. The program is thoroughly checked by entering dummy data, it works as per the requirement performing all function. The program is great for a small rental agency. In future we will make this program more efficient by creating proper relationship between the data, gave it a better user interface and creating a user window from which user can also easily rent an apartment rather than coming to the rental agency and more features like this.
