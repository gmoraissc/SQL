!pip install db-sqlite3

import pandas as pd
import sqlite3
from datetime import date

db = sqlite3.connect("testing.db")
db.execute('create table results(Name text, Date datetime, Mobile text, Mail text)')

def pushtoDB(Name,Mobile,Mail):

  db = sqlite3.connect('testing.db')
  from datetime import date
  Date = date.today().strftime("%d-%m-%Y")
  cmd = "insert into results(Name,Mobile,Date,Mail) values('{}','{}','{}','{}')".format(Name,Mobile,Date,Mail)
  db.execute(cmd)
  db.commit()
  
  df = pd.read_csv(f'/content/drive/MyDrive/data science/SQL/sqlteste.txt')
  
  for i in range(0, len(df)):
  pushtoDB(df.iloc[i][0],df.iloc[i][1],df.iloc[i][2])

qry = """
SELECT * FROM results
"""
df = pd.read_sql_query(qry, db)
df.head()
