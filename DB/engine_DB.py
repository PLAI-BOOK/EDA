import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
# Load environment variables from .env file
load_dotenv()
from db_connect.connectDB import get_db_connection as get_db_connection_out


def get_db_engine(db_name=None):
    """Establish a connection to the database using SQLAlchemy."""
    return get_db_connection_out()
    # DB_HOST = os.getenv("DB_HOST")
    # DB_USER = os.getenv("DB_USER")
    # DB_PASSWORD = os.getenv("DB_PASSWORD")
    # DB_PORT = os.getenv("DB_PORT", "5432")  # Set a default port if not in .env
    # db_name = db_name or os.getenv("DB_NAME").lower()
    #
    # try:
    #     # Create an SQLAlchemy engine
    #     engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{db_name}')
    #     return engine
    # except Exception as e:
    #     print(f"Error while connecting to the {db_name} database: {e}")
    #     return None


