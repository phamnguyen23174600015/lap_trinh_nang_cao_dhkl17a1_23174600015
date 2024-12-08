import sqlite3  
conn = sqlite3.connect('mydatabase.db')  
conn.execute("UPDATE bang1 SET 'name' = 'Nguyễn Vân Anh' where id='4'")  
conn.commit()  
cursor = conn.execute("SELECT * FROM bang1")  
for row in cursor:  
   print(row)   
conn.close() 