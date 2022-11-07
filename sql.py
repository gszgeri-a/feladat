import pymysql

conn = pymysql.connect(user='sql7545459', password='1lEUskSrmn',
                              host='sql7.freesqldatabase.com',
                              database='sql7545459')

curs = conn.cursor()

curs.execute("CREATE TABLE users (felhasznalonev TEXT, jelszo TEXT)")
print("Sikeres")

conn.close()    