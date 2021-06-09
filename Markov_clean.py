# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 15:34:32 2021

@author: Thomas
"""

# %%
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import calendar
import glob

df = pd.DataFrame()

## import data into dataframe
for file in glob.glob('./data/'+'*.csv'):
    dummy = pd.read_csv(file, sep=';', parse_dates=['timestamp'], index_col=['timestamp'])
    df = df.append(dummy)
    
df = df.sort_index()

# add weekday column, and replace it with day_name
df['weekday'] = df.index.dayofweek
df['weekday'] = df['weekday'].apply(lambda x: calendar.day_name[x])

#os.chdir('G:/spiced')
# %%
def Get_Markov():
    # Calculate the total number of customers in the supermarket over time
    # forward fill to fill out the timestamps
    df2 = df.groupby(['weekday','customer_no'], as_index=False).resample('1Min').ffill()
    
    # get the next location of the custoners
    df2['next_location']=df2.groupby(['weekday','customer_no'])['location'].shift(-1)
    df2.fillna('checkout', inplace=True)
    
    P = pd.crosstab(df2['location'], df2['next_location'], normalize='index')
    return P

    # %%
def Get_Entry():
    df['timestamp'] = df.index.time
    time_spent = df.groupby(['weekday','customer_no'], as_index=False).agg({'timestamp':'min'})
    time_spent.head()
    
    entry = time_spent.groupby('timestamp').count() //5
    
    entry['timestamp'] = entry.index

    entry = entry.assign(time=pd.to_datetime(entry.index, format='%H:%M:%S'))
    entry.set_index('time', inplace=True)
    entry = entry.resample('1Min').ffill()
    
    entry_per_min = entry['customer_no']
    return entry_per_min


