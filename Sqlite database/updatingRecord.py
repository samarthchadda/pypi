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



def update_data():
    dbase.execute(''' UPDATE emp_records SET DEPT='Electronics'
                WHERE ID=6
        ''')

    dbase.commit()
    print("Record Updated")


update_data()
print('-----------------------')
readData()







dbase.close()     

print("Database Closed")


