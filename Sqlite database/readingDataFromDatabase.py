import sqlite3

dbase=sqlite3.connect('Our_data.db')


print("Database Opens")




#def insert_record(id,nm,dpt,rtng):
#    dbase.execute('''INSERT INTO emp_records(ID,NAME,DEPT,RATING)
 #                           VALUES(?,?,?,?)''',(id,nm,dpt,rtng))


#    dbase.commit()

#    print("Records Inserted")





def readData():
    data=dbase.execute(''' SELECT ID,NAME,DEPT,RATING FROM emp_records ''')
    for record in data:
        print("ID:"+str(record[0]))
        print("NAME:"+str(record[1]))
        print("DEPT:"+str(record[2]))
        print("RATING:"+str(record[3])+'\n')
        



readData()



dbase.close()     

print("Database Closed")


