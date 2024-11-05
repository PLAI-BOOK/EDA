from DB.engine_DB import get_db_engine
import pandas as pd
import os
from datetime import datetime

def SQLtoDF(table_name):
    # Create a database connection
    engine = get_db_engine()
    # Query the table and load it into a DataFrame
    df = pd.read_sql_table(table_name, con=engine)
    return df

def DFtoCSVandSAVE(table_name,file_path):
    df = SQLtoDF(table_name)
    file_name = table_name + ".csv"
    full_file_path = os.path.join(file_path, file_name)
    csv = df.to_csv(str(full_file_path),index=False)

def DB_backup_low_version():
    print("This is for the first backup - until Shapira fixes Postgres backup")
    # Get today's date in YYYY-MM-DD format
    today_date = datetime.today().strftime('%Y-%m-%d')
    # Create a directory named "backup_<today's date>"
    backup_dir = f"backup_{today_date}"
    os.makedirs(backup_dir, exist_ok=True)
    # List of table names to back up
    tables_names = ['events', 'fixtures', 'players', 'teams', 'game_possession', 'whoscored_events']
    # Save each table as a CSV in the backup directory
    for table_name in tables_names:
        file_path = os.path.join(backup_dir, f"{table_name}.csv")
        DFtoCSVandSAVE(table_name)
        print(f"{table_name} backup is done and saved as {file_path}")

    print(f"All backups are saved in the '{backup_dir}' directory.")







