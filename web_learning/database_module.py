import sqlite3

connction = sqlite3.connect('test.db')
cursor = connction.cursor()
#cursor.execute('create table user (id varchar(20) primary key,name varchar(20))')
cursor.execute('insert into user (id,name) values (\'140301066\',\'gavin\')')
cursor.execute('insert into user (id,name) values (\'140301067\',\'gavin\')')
cursor.execute('insert into user (id,name) values (\'140301068\',\'gavin\')')
#cursor.execute('drop table user')

cursor.execute('select * from user')

values = cursor.fetchall()

print values[0][1]

cursor.close()

connction.close()