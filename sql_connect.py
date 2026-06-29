import sqlite3
a = sqlite3.connect('data.db')
b = a.cursor()
# b.execute("create table Student (sid number,sname varchar,phno number,marks number)")
# b.execute("insert into Student values(101,'kiran',1234567891,35)")
# b.execute("insert into Student values(102,'manik',1234567892,100)")
# b.execute("insert into Student values(103,'sang',1234567893,100)")
b.execute("insert into Student values(103,'sang',1234567893,100)")
a.commit()


data = b.execute('select * from Student')
# print(data.fetchall()[1][0])
print(data.fetchone())
b.close()