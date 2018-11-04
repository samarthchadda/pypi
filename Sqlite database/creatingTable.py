import sqlite3

dbase=sqlite3.connect('Our_data.db')       #this creates a database file
                                           #extension can be .db, .sqlite3, .dbase, .manu(your name also)
                                            #opens a database File


print("Database Opens")




#execute() function executes the SQL commands 
dbase.execute('''CREATE TABLE IF NOT EXISTS emp_records(
    ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    DEPT TEXT NOT NULL,
    RATING INT NOT NULL

)''')    


print("Table created")




dbase.close()     #closing the database

print("Database Closed")


