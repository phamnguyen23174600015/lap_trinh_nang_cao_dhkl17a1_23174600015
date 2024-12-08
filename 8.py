import sqlite3  
     
conn = sqlite3.connect('mydatabase.db')  
conn.execute("DELETE from bang1 where id=1")  
conn.commit()  
print("Tổng số bản ghi được xóa :", conn.total_changes ) 
   
cursor = conn.execute("SELECT * FROM bang1")  
for row in cursor:  
   print(row)    
  
conn.close() 