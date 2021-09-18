import numpy as np
import pandas as pd

column_names = ['user_id', 'item_id', 'rating', 'timestamp']
users = pd.read_csv('u.data', sep='\t', names=column_names)

# print(users.head())

movie_titles = pd.read_csv("Movie_Id_Titles")
# print(movie_titles.head())

dataset = pd.merge(users, movie_titles, on="item_id")

#print(dataset.head())

# mean_rating = dataset.groupby('title')['rating'].mean().sort_values(ascending=False)
# print(mean_rating.head())

count_rating = dataset.groupby('title')['rating'].count().sort_values(ascending=False)
print(count_rating.head())

ratings = pd.DataFrame(dataset.groupby('title')['rating'].mean())
# print(ratings.head())

ratings['num of ratings'] = pd.DataFrame(dataset.groupby('title')['rating'].count())
# print(ratings.head())

moviemat = dataset.pivot_table(index='user_id',columns='title',values='rating')
# print(moviemat.head())


# important code
# print(ratings.sort_values('num of ratings',ascending=False).head(10))


# print(ratings.head())


# choose two movies
starwars_user_ratings = moviemat['Star Wars (1977)']
liarliar_user_ratings = moviemat['Liar Liar (1997)']
# print(starwars_user_ratings.head())

similar_to_starwars = moviemat.corrwith(starwars_user_ratings)
similar_to_liarliar = moviemat.corrwith(liarliar_user_ratings)

corr_starwars = pd.DataFrame(similar_to_starwars,columns=['Correlation'])
corr_starwars.dropna(inplace=True)
# print(corr_starwars.head())

# star_wars co-relation movies
corr_starwars.sort_values('Correlation',ascending=False).head(10)

corr_starwars = corr_starwars.join(ratings['num of ratings'])
# print(corr_starwars.head())

# print(corr_starwars[corr_starwars['num of ratings']>100].sort_values('Correlation',ascending=False).head())


# liar liar movie related movies
corr_liarliar = pd.DataFrame(similar_to_liarliar,columns=['Correlation'])
corr_liarliar.dropna(inplace=True)
corr_liarliar = corr_liarliar.join(ratings['num of ratings'])
print(corr_liarliar[corr_liarliar['num of ratings']>100].sort_values('Correlation',ascending=False).head())
