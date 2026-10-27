import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv('matches.csv')
delivery=pd.read_csv('deliveries.csv')
# print (a.head())
# print(a.tail())
# print(a.shape)
# print(a.info())
# print(a.describe())
# print(a['winner'])
# print(a[['winner','team1','team2']])
# print(a.iloc[1:4])
# mask=a['city']=='Hyderabad'
# print(a[mask])
# def ipl_max_match_winner(team):
#     mask=a["winner"]==teams
#     return a[mask].shape[0]
# name=input("Enter the team name :")
# print(ipl_max_match_winner(name))
# (a['winner'].value_counts().plot(kind='bar'))
# plt.show()
# team=input("Enter the name of the team")
# a=data['team1'].value_counts()
# b=data['team2'].value_counts()
# print("Your team played",a[team]+b[team])
# c=(data.drop_duplicates(subset=['city','team1'], keep='last'))
# print(c)

#to find the season winner of each year
# c=data.drop_duplicates(subset=['season'], keep='last')
# print(c[['season','winner']].sort_values('season'))

#Groupby object 

#winner_collection=data.groupby('winner')
# print(winner_collection.size())
#print(winner_collection.get_group('Chennai Super Kings'))
#print(delivery.head())

#runs=delivery.groupby("batsman")
# mask=delivery['batsman_runs']==3
# new_delivery=delivery[mask]
# print(new_delivery.groupby('batsman')['batsman_runs'].count().sort_values(ascending=False).head(10))
# vk=delivery[delivery['batsman']=='V Kohli']
# print(vk.groupby('bowling_team')['batsman_runs'].sum().sort_values(ascending=False).head())

# new=delivery.merge(data , left_on='match_id' , right_on='id')
# print(new.groupby(['season','batsman'])['batsman_runs'].sum().sort_values(ascending= False).reset_index().drop_duplicates(subset='season').sort_values('season'))

six=delivery[delivery['batsman_runs']==6]
pt=six.pivot_table(index='over' , columns='batting_team' , values='batsman_runs' , aggfunc='count')
sns.heatmap(pt)
plt.show()
