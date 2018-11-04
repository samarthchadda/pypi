import sqlite3

dbase=sqlite3.connect('Our_data.db')       #this creates a database file
                                           #extension can be .db, .sqlite3, .dbase, .manu(your name also)
                                            #opens a database File


print("Database Opens")




#execute() function executes the SQL commands 
#dbase.execute('''CREATE TABLE IF NOT EXISTS emp_records(
#    ID INT PRIMARY KEY NOT NULL,
 #   NAME TEXT NOT NULL,
  #  DEPT TEXT NOT NULL,
   # RATING INT NOT NULL

#)''')    


#print("Table created")


dbase.execute('''INSERT INTO emp_records(ID,NAME,DEPT,RATING)
                        VALUES(1,'Samarth','Software',4)
                        ''')

dbase.execute('''INSERT INTO emp_records(ID,NAME,DEPT,RATING)
                        VALUES(2,'Manu','Manager',5)
                        ''')


dbase.commit()     #apply the above changes(insertion of data) to database

print("Records Inserted")




dbase.close()     #closing the database

print("Database Closed")


