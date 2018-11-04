import sqlite3

dbase=sqlite3.connect('Our_data.db')       #this creates a database file
                                           #extension can be .db, .sqlite3, .dbase, .manu(your name also)
                                            #opens a database File


print("Database Opens")


dbase.close()     #closing the database

print("Database Closed")


