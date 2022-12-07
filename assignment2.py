#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 18:20:49 2022

@author: asus
"""
import pandas as pd
import matplotlib.pyplot as plt

def get_data_frames(filename):
    '''
    

    Parameters
    ----------
    filename : TYPE
        DESCRIPTION.

    Returns
    -------
    df : TYPE
        DESCRIPTION.
    df2 : TYPE
        DESCRIPTION.

    '''
    df = pd.read_csv(filename, skiprows=(4), index_col=False)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df = df.loc[df['Country Name'].isin(countries)]
    df2 = df.melt(id_vars=['Country Name','Country Code','Indicator Name','Indicator Code'], var_name='Years')
    
    del df2['Country Code']
    df2 = df2.pivot_table('value',['Years','Indicator Name','Indicator Code'],'Country Name').reset_index()

    return df, df2


countries = ['Japan','Germany','Canada','United Kingdom']

#----------------------------------------------------------
#Line plot 1
df, df2 = get_data_frames('API_19_DS2_en_csv_v2_4700503.csv')
df2 = df2.loc[df2['Indicator Code'].eq('EG.FEC.RNEW.ZS')]

plt.figure(figsize=(7,7))
df2['Years'] = pd.to_numeric(df2['Years'])
df2.plot("Years", countries, title='Renewable energy consumption (% of total final energy consumption)')
plt.xlabel("Years")
plt.ylabel("Renewable energy consumption ")
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()

#-----------------------------------------
# Line Plot 2
data1, data2 = get_data_frames('API_19_DS2_en_csv_v2_4700503.csv')
data2 = data2.loc[data2['Indicator Code'].eq('SP.POP.TOTL')]

plt.figure(figsize=(7,7))
data2['Years'] = pd.to_numeric(data2['Years'])
data2.plot("Years", countries, title='Total population')
plt.xlabel("Years")
plt.ylabel("Total population")
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()


