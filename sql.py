import pymysql
import sqlite3

conn = sqlite3.connect('database.db') 

"""conn = pymysql.connect(user='sql7545459', password='1lEUskSrmn',
                              host='sql7.freesqldatabase.com',
                              database='sql7545459')"""

curs = conn.cursor()

#curs.execute("DROP TABLE users")


curs.execute("CREATE TABLE users (felhasznalonev TEXT, jelszo TEXT)")
print("Sikeres")

conn.close()    