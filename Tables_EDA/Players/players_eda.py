from SQLtoDF import SQLtoDF
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# players_df = SQLtoDF('players')
# players_csv = players_df.to_csv('players.csv',index=False)

# Load the CSV file
data = pd.read_csv('players.csv')
numeric_data = data.select_dtypes(include='number')

print (data.head())

# Check for null values
print(data.isnull().sum())
# the values that are missing are age-3, hight-316, weight-608, raiting-1195
# there are actually players that doesnt have any raiting
# same with the rest... idk why

# Select only numerical columns and calculate the mean
numerical_data = data.select_dtypes(include=['number'])
averages = numerical_data.mean()

print("Average for each numerical column:")
print(averages)

# looks like i have a problem in dribbled past
# penalties_won     , penalties_committed    , they are all 0

# Get the IDs where the rating is NaN
nan_rating_ids = data.loc[data['rating'].isnull(), 'player_id']
print("IDs of players with missing ratings:")
print(nan_rating_ids)

# Get the IDs where the height is NaN
nan_height_ids = data.loc[data['height'].isnull(), 'player_id']
print("\nIDs of players with missing heights:")
print(nan_height_ids)

# Get the IDs where the weight is NaN
nan_weight_ids = data.loc[data['weight'].isnull(), 'player_id']
print("\nIDs of players with missing weights:")
print(nan_weight_ids)

# Get the IDs where the age is NaN
nan_age_ids = data.loc[data['age'].isnull(), 'player_id']
print("\nIDs of players with missing ages:")
print(nan_age_ids)

# Example: Plotting histograms of numerical columns
data.hist(figsize=(50, 50))
plt.tight_layout()
# Save the figure as an image file (e.g., PNG format)
plt.show()

plt.figure(figsize=(50,50))
sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm')
plt.show()

