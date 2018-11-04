import sqlite3

dbase=sqlite3.connect('Our_data.db')


print("Database Opens")




def insert_record(id,nm,dpt,rtng):
    dbase.execute('''INSERT INTO emp_records(ID,NAME,DEPT,RATING)
                            VALUES(?,?,?,?)''',(id,nm,dpt,rtng))


    dbase.commit()

    print("Records Inserted")



insert_record(6,'Bob','Marketing',4)

dbase.close()     

print("Database Closed")


