import sqlite3
import pandas as pd
import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='testdb'

)

#Create a cursor (an instance) to manipulate your SQL
mycursor=mydb.cursor(buffered=True)

##SELECT only certain fields
table_name='russell3000'
mycursor.execute(f'SELECT * FROM {table_name}')

result=mycursor.fetchall()

result = mycursor.fetchall()

df = pd.DataFrame.from_records(
    result,
    columns=[i[0] for i in mycursor.description]
)

df.to_csv(r"E:\\PYTHON\\Python_Aim\\PYTHON\\PY_Projects\\PythonSql\\Company_Names.csv")