# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 11:40:56 2021

@author: Thomas
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

os.chdir('G:/spiced')

monday = pd.read_csv('./nlpepper-encounter-notes/08_markov_simulation/data/monday.csv',
                     sep=';')

monday.head()
monday.shape

monday['timestamp'] = pd.to_datetime(monday['timestamp'], format='%Y-%m-%d %H:%M:%S')
monday.set_index('timestamp', inplace=True)

monday['location'].value_counts()
monday['customer_no'].value_counts().sum()

monday['hour'] = monday.index.hour
df2=monday.groupby(['location', 'hour'], as_index=False).count()

row_filter = df2['location'] == 'checkout'
checkout_time = df2[row_filter]
checkout_time.plot(x='hour')
checkout_time['customer_no'].sum() # ~10 don't check out

customer = monday['customer_no'] == 526
cust526 = monday[customer]

monday['timestamp'] = monday.index
time_spent =monday.groupby(['customer_no'], as_index=False).agg({'timestamp':['min', 'max']})

customer_longest = time_spent['customer_no'] == 526
time_spent[customer_longest]

time_spent['spent'] = time_spent['timestamp', 'max'] - time_spent['timestamp', 'min']
# extract integer (minutes)?

# Calculate the total number of customers in the supermarket over time.
customers_over_time =monday.groupby(['hour'], as_index=False).count()

opening_range = pd.date_range("07:00", "21:50", freq="1min").strftime('%H:%M:%S')