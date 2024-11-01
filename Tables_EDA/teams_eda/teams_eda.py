import pandas as pd
import numpy as np
from SQLtoDF import SQLtoDF

# teams table to df
teams_df = SQLtoDF('teams')

# get basic overview data
print(teams_df.head())

# Get a quick summary of the DataFrame (data types, non-null values, memory usage)
print(teams_df.info())

# View basic statistics (mean, std, min, 25%, 50%, 75%, max) for numerical columns
print(teams_df.describe())

# checking missing values
# Count missing values in each column
print(teams_df.isnull().sum())





