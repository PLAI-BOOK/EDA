import os
from dotenv import find_dotenv, load_dotenv
load_dotenv()
from db_connect.connectDB import get_db_connection as get_db_connection_out



con=get_db_connection_out(db_name="second_league")
print(con)
con.close()
con=get_db_connection_out(db_name="workingdb")
print(con)
con.close()