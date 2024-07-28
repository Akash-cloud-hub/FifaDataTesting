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

# create a bar graph for the top 5 highest wages
plt.bar(list(player_salary['short_name'][0:5]) , list(player_salary['wage_eur'][0:5]) , color=['green','orange','blue','pink','black'] )
# plt.show()
plt.clf()

german_players = fifa[fifa['nationality']=='Germany']
ic(german_players)
# sort german players by there height

german_players = german_players.sort_values(by=['height_cm'],ascending=True)
ic(german_players[['short_name','height_cm']].head())

# sort the german players by there weight
german_players = german_players.sort_values(by=['weight_kg'],ascending=False)
ic(german_players[['short_name','weight_kg']].head())

# store the short name and shooting capabilities in a variable

stats = fifa[['short_name','shooting']]
stats = stats.sort_values(by=['shooting'],ascending=False)
ic(stats.head())

# create a variable that contains , name , nationality , club , defending capabilities
defense = fifa[['short_name','nationality','club','defending']]
defense = defense.sort_values(by=['defending'] , ascending = False)
ic(defense.head())

# get data of all real madrid players
real_madrid = fifa[fifa['club']=='Real Madrid']
real_madrid_wage = real_madrid.sort_values(by='wage_eur',ascending = False )
ic(real_madrid_wage[['short_name' , 'wage_eur']].head())

real_madrid = fifa[fifa['club']=='Real Madrid']
real_madrid_shooting = real_madrid.sort_values(by='shooting',ascending = False )
ic(real_madrid_shooting[['short_name' , 'wage_eur']].head())

# find all the nationalities in real madrid
real_madrid_nationalities = real_madrid['nationality']
ic(real_madrid_nationalities.value_counts())