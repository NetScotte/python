import pymysql

db = pymysql.connect("localhost","root","520Oracle1314","test")
cursor = db.cursor()

cursor.execute("select version()")
data = cursor.fetchone()
print("database version:%s"%data)

db.close()
