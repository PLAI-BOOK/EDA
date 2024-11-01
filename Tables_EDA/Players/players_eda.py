from SQLtoDF import SQLtoDF

players_df = SQLtoDF('players')
players_csv = players_df.to_csv('players.csv',index=False)
