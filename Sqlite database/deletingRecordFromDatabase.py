import sqlite3

dbase=sqlite3.connect('Our_data.db')


print("Database Opens")



def readData():
    data=dbase.execute(''' SELECT ID,NAME,DEPT,RATING FROM emp_records ''')
    for record in data:
        print("ID:"+str(record[0]))
        print("NAME:"+str(record[1]))
        print("DEPT:"+str(record[2]))
        print("RATING:"+str(record[3])+'\n')     



readData()




def del_record():
    dbase.execute(''' DELETE FROM emp_records WHERE ID=6 ''')
    dbase.commit()
    print("Record Deleted")




del_record()

print('--------')

readData()






dbase.close()     

print("Database Closed")


