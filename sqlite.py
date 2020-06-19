import sqlite3
clientsql=sqlite3.connect(r'D:\GALLANT DECOY\Documents\#Python\miniproject\user.db')
cu=clientsql.cursor()
try:
    cu.execute('create table student(id int(12) unique,name varchar(50),tech varchar(20),fee floaat)')
except:
    pass
cu.execute('insert into student values(%d,%r,%r,%f)'%(3,'iamshivendra','java',4000))
cu.execute('select * from student')
cu.fetchall()
