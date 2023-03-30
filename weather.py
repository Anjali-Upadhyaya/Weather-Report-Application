
import pymysql
conn = pymysql.connect(
        host= 'weather-database.cfjyiixk1ade.us-west-2.rds.amazonaws.com', 
        port = 3306,
        user = 'admin', 
        password = 'database-1',
        db = 'weather',
    )

#Table Creation
#cursor=conn.cursor()
#create_table="""
#create table Details (country varchar(200),state varchar(200),city varchar(200),pressure float,humidity float )
#
#"""
#cursor.execute(create_table)

#insert query
def insert_details(country,state,city,pressure,humidity):
    cur=conn.cursor()
    cur.execute("INSERT INTO Details (country,state,city,pressure,humidity) VALUES (%s,%s,%s,%f,%f)", (country,state,city,pressure,humidity))
    conn.commit()

#read the data
def get_details():
    cur=conn.cursor()
    cur.execute("SELECT *  FROM Details")
    details = cur.fetchall()
    return details

