import mysql.connector

conn = mysql.connector.connect(user = 'root', password='123456',database = 'learning',use_unicode=True)
cursor = conn.cursor()
cursor.execute('create table user (id varchar(20) primary key,name varchar(20))')
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
conn.commit()
cursor.close()
conn.close()