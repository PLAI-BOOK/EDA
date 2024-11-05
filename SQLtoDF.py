from DB.engine_DB import get_db_engine
import pandas as pd

def SQLtoDF(table_name):
    # Create a database connection
    engine = get_db_engine()
    # Query the table and load it into a DataFrame
    df = pd.read_sql_table(table_name, con=engine)
    return df

def DFtoCSVandSAVE(table_name):
    df = SQLtoDF(table_name)
    file_name = table_name + ".csv"
    csv = df.to_csv(file_name,index=False)

def DB_backup_low_version():
    print("this is for first backup - until Shapira will fix postgres backup")
    tables_names = ['events', 'fixtures', 'players', 'teams', 'game_possession', 'whoscored_events']
    for table_name in tables_names:
        DFtoCSVandSAVE(table_name)
        print(f"{table_name} is done")





