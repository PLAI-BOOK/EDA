from DB.engine_DB import get_db_engine
import pandas as pd

def SQLtoDF(table_name):
    # Create a database connection
    engine = get_db_engine()
    # Query the table and load it into a DataFrame
    df = pd.read_sql_table(table_name, con=engine)
    return df
