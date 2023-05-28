# -*- coding: utf-8 -*-
"""Netflix_Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SJn9dgjrBfvtfiD7emhjiCPFuP4El-GG
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""## 1. Defining Problem Statement and Analysing basic metrics

We need to explore data to understand and answer how Netflix can grow their business. What is working for them and how they can plan ahead. The challenges that we will face during the analysis will be dealing with missing values,multiple values in columns and datatype of the columns
"""

! gdown 1XNHfxmS7qeUSGDHrCrbU-GVS6TPtkEpz

# Read the csv file
df=pd.read_csv("Netflix.csv")

# List of columns in the data
df.columns

# Top 5 rows from the data
df.head()

# Check duplicate entries
df[df.duplicated]
# There are no duplicate entries in the data

"""## 2. Observations on the shape of data, data types of all the attributes, conversion of categorical attributes to 'category' (If required), missing value detection, statistical summary"""

# Shape of the data
df.shape

# Dimension of the data
df.ndim

# Data type of data
type(df)

# Basic information of the data
df.info()
# Director, cast, country, and date_added has NaN values. We also have minor missing values in rating and duration columns

# Changing datatype of the columns

df["date_added"]=pd.to_datetime(df["date_added"])
df["director"]=df["director"].astype(dtype="string")
df["cast"]=df["cast"].astype(dtype="string")
df["listed_in"]=df["listed_in"].astype(dtype="string")
df["country"]=df["country"].astype(dtype="string")
df["duration"]=df["duration"].astype(dtype="string")

df.info()

# Statistical details of the data
df.describe(include="all")

# Checking the null values in columns and getting boolean values
df.isnull()

# Heatmap for null values
sns.heatmap(df.isnull())

"""## 3. Dealing with missing values"""

# Using interpolate to filling the missing values

df=df.interpolate(method="pad",limit_direction="forward")
df.fillna("Anonymous",inplace=True)
df

"""## 4. Non-Graphical and visual analysis of data"""

# Movies vs TV Show Count
df.groupby("type")[["type"]].value_counts()

plt.figure(figsize=(3,5))
sns.countplot(df,x="type")

"""We can see that Netflix has 6131 Movies and 2676 TV Shows. """

# Unnesting country's column for further analysis
df_c=df.assign(country=df['country'].str.split(',')).explode('country')
df_c

# Count of movies and tv shows contributed by each country
df_country=df_c.groupby("country")[["title"]].count().sort_values(by="title",ascending=False).rename(columns={"title":"count"}).reset_index()
df_c1=df_country.head(6)
df_c1

sns.barplot(df_c1,x="country",y="count")
plt.xticks(rotation=45)

# Top 5 genres United States has contributed into
df_c.query('country=="United States"')[["listed_in"]].value_counts().head(5).reset_index().rename(columns={0:"count"})

"""Top 5 contributors on Netflix are United States, India, United Kingdom, Canada and Japan with United States on the top with count of 4224 which includes Documentaries as the top listed category."""

# Top viewed genre on Netflix 
df_g=df.assign(listed_in=df['listed_in'].str.split(',')).explode('listed_in')
df_g["listed_in"].value_counts().head()

"""Netflix has most content in International movies category. Here we assume that the Netflix has more content that people watch. Hence, the highest count of the genre will be the most viewed genre"""

# Number of movies and tv shows released every year
df.groupby("release_year")[["type"]].count().rename(columns={"type":"count"}).sort_values(by="count",ascending=False).head(10)

# Number of movies and shows release in the past 30 years
plt.figure(figsize=(15,5))
sns.histplot(df,x=df.query('release_year>=1990')["release_year"])

# Number of movies vs shows release in the past 30 years
plt.figure(figsize=(15,5))
sns.histplot(df,x=df.query('release_year>=1990')["release_year"],hue="type")

# Graphial repesentation via boxplot
sns.boxplot(df,x="release_year",y="type")

"""Most content was released in 2018 on Netflix. However, most of the TV show was released in 2020. From the chart we can see that Netflix has always focused more on Movies rather than Tv shows unlike in 2021 where Tv show was more than movies"""

# Best time to launch a tv vs movies
df["added_month"]=df["date_added"].dt.month_name()
df.query('type=="Movie"')[["added_month"]].value_counts()

df.query('type=="TV Show"')[["added_month"]].value_counts()

# Best time to launch a movie is July and tv show is December as the previous data shows that has monst movies and shows have been launched during that month.

#  Graphical representation of best time to launch a movie and tv show
plt.figure(figsize=(15,5))
df["added_month"]=df["date_added"].dt.month_name()
sns.countplot(df,x=df["added_month"],hue="type")

"""From the charts we can conclude that mostly movies are launched in July and Tv shows in December. As per the data, July and December will be a good time to launch movies and tv shows respectively."""

# Top 10 directors who has produced max number of movies or tv shows
df_d=df.assign(director=df['director'].str.split(',')).explode('director')
df_d

df_d.query('type=="Movie"')[["director"]].value_counts().head(10)

df_d.query('type=="TV Show"')[["director"]].value_counts().head(10)

# Top 10 casts on Netflix
df_cast=df.assign(cast=df['cast'].str.split(',')).explode('cast')
df_cast

df_cast.query('type=="Movie"')[["cast"]].value_counts().head(10)

df_cast.query('type=="TV Show"')[["cast"]].value_counts().head(10)

"""As per the above analysis, Rajiv Chilaka has directed most movies and Marcus Raboy has directed most Tv shows. Anupam Kher and Takahiro Sakurai acted most movies and tv series present on Netflix."""

# Analysis of rating
df["rating"].value_counts().head(10)

df_cast.query('rating=="TV-MA"')["director"].value_counts()

df_cast.query('rating=="TV-MA"')["cast"].value_counts()

# Graphical representation of rating
plt.figure(figsize=(15,5))
rating=df["rating"].value_counts().head(10)
sns.barplot(df,x=rating.index,y=rating.values)

"""Netflix has most of the content for mature audiences and audience above the age of 14 i.e., TV-MA and TV-14. Youssef Chahine and  Takahiro Sakurai has directed and acted most content for TV-MA category respectively."""

# Duration analysis
# Spliting the duration column
df["duration"]=df["duration"].str.split(expand=True)[0]
df

# Duration that has highest frequency on the movies data
df_dur=df.query('type=="Movie"')[["duration"]].value_counts().reset_index().rename(columns={"duration":"minutes", 0:"count"}).head(50)
df_dur.head()

plt.figure(figsize=(20,5))
plt.xticks(rotation=45)
sns.barplot(data=df_dur,x="minutes",y="count")

# Duration that has highest frequency on the TV Show data
df_dur1=df.query('type=="TV Show"')[["duration"]].value_counts().reset_index().rename(columns={"duration":"seasons", 0:"count"})
df_dur1.head()

plt.figure(figsize=(10,5))
plt.xticks(rotation=45)
sns.barplot(data=df_dur1,x="seasons",y="count")

"""Most favourable duration for movies is 90 minutes. Assuming there are equal number of episodes in each season, tv show with highest number of seasons will be most favourable considering more and more seasons are produced as per the previous seasons’ rating and TRP."""



"""Netflix has more movies than tv shows. The United states has contributed most in the content. Netflix should focus on more content from the top 5 contributors (US, India, UK, Canada, Japan) of the content from international movies, dramas and comedies genre. It should also get more and more content directed from Rajiv Chilaka and Marcus Raboy.

Netflix has more content for mature population and anything else. We can infer that most of the people prefer to watch 90 mins of movies as when we compared it with other durations of the movies, it has the highest count. Assuming there are equal number of episodes in each season, tv show with highest number of seasons will me most favourable considering more and more seasons are produced as per the previous seasons’ rating and TRP.

"""