import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from icecream import ic

fifa = pd.read_csv('players_20.csv')
ic(fifa.head())

# Find the number of rows and columns in the data set
ic(fifa.shape)

# Print the name of all columns name with the help of for loop
for i in fifa.columns: # fifa.columns creates a list of all the columns
    ic(i)

# calculate the total number of players in the by their nationalities
ic(fifa['nationality'].value_counts()[0:5])

# Find the number of players in Fifa from vietnam
vietnam_players = fifa[fifa['nationality'] == 'India']
ic(vietnam_players.head())

ic(fifa['nationality'].value_counts().head(10))

# Top 5 countries with most players using keys
ic(fifa['nationality'].value_counts().head().keys())

plt.figure(figsize=(8,5))
plt.bar(list(fifa['nationality'].value_counts().head().keys()) , list(fifa['nationality'].value_counts().head()) , color='g')
# plt.show()
plt.clf()

# Get the name and wage of each player
player_salary = fifa[['short_name','wage_eur']]
ic(player_salary.head())

player_salary= player_salary.sort_values(by=['wage_eur'], ascending=False)
ic(player_salary.head())

plt.bar(list(player_salary['short_name'][0:5]) , list(player_salary['wage_eur'][0:5]) )
plt.show()