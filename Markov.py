# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 11:40:56 2021

@author: Thomas
"""
# %%
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import calendar

#os.chdir('G:/spiced')
# %%
df = pd.DataFrame()
print(os.listdir('./data/'))

## import data into dataframe
for file in os.listdir('./data/'):
    print(file)
    dummy = pd.read_csv('./data/' + file, sep=';', parse_dates=['timestamp'], index_col=['timestamp'])
    df = df.append(dummy)

df = df.sort_index()
df['weekday'] = df.index.dayofweek
df['weekday'] = df['weekday'].apply(lambda x: calendar.day_name[x])
# %%
df['location'].value_counts()
print(df['location'].value_counts())
df['customer_no'].value_counts().sum()
print(df['customer_no'].value_counts().sum())

# Calculate the total number of customers in each section over time
df.groupby('location').resample('H')['customer_no'].count()

# %%
#Calculate the time each customer spent in the market
df['timestamp'] = df.index
time_spent =df.groupby(['weekday','customer_no'], as_index=False).agg({'timestamp':['min', 'max']})
time_spent['spent'] = time_spent['timestamp', 'max'] - time_spent['timestamp', 'min']
# extract integer (minutes)?
# %%
# Calculate the total number of customers in the supermarket over time.
df2 = df.groupby(['weekday','customer_no'], as_index=False).resample('1Min').ffill()

# %%
df2_friday = df2[df2['weekday']=='Friday']
df2_friday['datetime'] = df2_friday.index.get_level_values(1)
df2_friday.groupby(['datetime']).count().plot(y='customer_no')
# %%
df3 =df.groupby(['weekday','customer_no'], as_index=False).agg({'timestamp':['min']})
# %%
vector_base = df.groupby(['weekday','customer_no']).first().value_counts('location', normalize=True)
vector_base['checkout'] = 0.0
# %%
last_stations = df.groupby(['weekday','customer_no'], as_index=False).last()
no_checkout = last_stations[last_stations['location']!='checkout']



# %%
row_filter = df['customer_no'].isin(no_checkout['customer_no']) & df['weekday'].isin(no_checkout['weekday'])
# %%
first_stations = df.groupby(['weekday','customer_no']).nth(0)['location']
second_stations = df.groupby(['weekday','customer_no']).nth(1)['location']

new_df = pd.merge(first_stations, second_stations,  
    how='left', 
    left_on=['weekday','customer_no'], 
    right_on = ['weekday','customer_no'])

new_df.fillna('checkout', inplace=True)


P = pd.crosstab(new_df['location_y'], new_df['location_x'], normalize=True)
# %%
