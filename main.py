from db_connect.connectDB import get_db_connection

con=get_db_connection()
print(con)
con.close()
