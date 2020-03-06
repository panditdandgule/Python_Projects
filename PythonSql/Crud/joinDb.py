import sqlite3
import mysql.connector
print('connected')

mydb=mysql.connector.connect(host='localhost',
                             user='root',
                             password='root',
                             database='testdb')

print(mydb)
table_name='russell3000'

#Create a cursor (an instance) to manipulate your SQL Database
mycursor=mydb.cursor(buffered=True)