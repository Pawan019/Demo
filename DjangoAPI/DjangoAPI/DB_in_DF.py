import pandas as pd
import sqlite3  as db
import sqlalchemy
#engine =sqlalchemy.create_engine('sqlite:///db.sqlite3')

#df = pd.read_sql_table("TestMyApp_departments", engine)
#df_emp = pd.read_sql_table("TestMyApp_employees", engine)

con = db.connect("db.sqlite3")
data = pd.read_sql_query('Select * from TestMyApp_departments', con)

print(data)


#print (df,'\n', df_emp)
