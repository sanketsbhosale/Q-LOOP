import sqlite3
b=""
a="sanketsbhosale2016@gmail.com"
connection=sqlite3.connect("loginDB.db")
rows=connection.execute("SELECT PASSWORD FROM LoginDBTable Where USERNAME=? AND EMAIL=?",(b,a))
connection.commit()
rows.fetchall()
 
for row in rows:
   print(row)


