import pandas as pd
import mysql.connector
print('connected!')

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='testdb'

)
print(mydb)

#Create a cursor (an instance) to manipulate SQL Database
mycursor=mydb.cursor(buffered=True)

##SELECT ONLY CERTAIN FIELDS=

table_name = 'ec_universe_20191231'
mycursor.execute(f'SELECT un_adj_ticker, record_date, dividend_yield, abv_gics_sector, mkt_cap_class  FROM {table_name}')

result=mycursor.fetchall()

df=pd.DataFrame.from_records(result,
    columns=[i[0] for i in mycursor.description])

sector_yield=df.groupby('abv_gics_sector')['dividend_yield'].mean()

print(sector_yield)
