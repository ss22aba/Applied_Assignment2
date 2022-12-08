#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 18:20:49 2022

@author: asus
"""

"""
Imported reqired libraries
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def get_data_frames(filename):
    
    """
    The function get_data_frames takes filename as the 
    argument read the data file
    into dataframes and returns df(countries), df2(years).
    
    """ 
    df = pd.read_csv(filename, skiprows=(4), index_col=False)
    print(df.info())

#Removing the column containg "unnamed" as part of the data cleaning.
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
   
#Selecting the countries.
    df = df.loc[df['Country Name'].isin(countries)]

#Transposing the data
    df2 = df.melt(id_vars=['Country Name','Country Code',
                           'Indicator Name','Indicator Code'], 
                  var_name='Years')

#Deleted country code.    
    del df2['Country Code']
    
# Transposing the data
    df2 = df2.pivot_table('value',
                          ['Years','Indicator Name','Indicator Code'],
                          'Country Name').reset_index()
    
    print(df2.info())

#Return countries and years.
    return df, df2

#Removes all the rows cotaining the null values.
    df.dropna()
    df2.dropna()

#The required countries for ploting the graphs are selected.
countries = ['Japan','Germany','Canada','United Kingdom']

#----------------------------------------------------------

#Generates the line plot for the renewable energy consumption ofr the selected
#countries.

#Read the file into dataframes.
df, df2 = get_data_frames('API_19_DS2_en_csv_v2_4700503.csv')

#The function the indicators
df2 = df2.loc[df2['Indicator Code'].eq('EG.FEC.RNEW.ZS')]

#Ploting the figure
plt.figure(figsize=(7,7))


df2['Years'] = pd.to_numeric(df2['Years'])

#Plots the line gragh also  the title is set.
df2.plot("Years", countries, 
         title='Renewable energy consumption(% of total final energy consumption)')

# Setting the x label as Years.
plt.xlabel("Years")

#Setting the y label as "Renewable energy consumption. 
plt.ylabel("Renewable energy consumption")

#Setting the legend
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

#saving the figure.
plt.savefig("Renewable  line plot")

#Show the figure.
plt.show()

# #----------------------------------------------------------------------------
#Generates the line plot for the Total population of the selected
#countries.

#Read the file into dataframes.
data1, data2 = get_data_frames('API_19_DS2_en_csv_v2_4700503.csv')
data2 = data2.loc[data2['Indicator Code'].eq('SP.POP.TOTL')]

# Plotting the figure.
# X label and Y label is set.
# Stting the title
plt.figure(figsize=(7,7))
data2['Years'] = pd.to_numeric(data2['Years'])
data2.plot("Years", countries, title='Total population in %')
plt.xlabel("Years")
plt.ylabel("Total population in %")

#setting the legend
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

#save the figure
plt.savefig("Population lie plot")

#Shows the figure.
plt.show()

#------------------------------------------------------------------------------
#Bar chart1

'''This function plot bar chart from the dataset using dataframe.
Bar chart shows duration of sunlight in UK between 2000-2005 for all seasons.
'''
df_bar, df2_bar = get_data_frames('API_19_DS2_en_csv_v2_4700503.csv')
print(df2_bar)
df2_bar = df2_bar.loc[df2_bar['Indicator Code'].eq('AG.LND.AGRI.ZS')]
# loc function used to get data of specific years 2000-2005 from dataframe.
print(df2_bar)
df2_bar = df2_bar.loc[df2_bar['Years'].isin(['2000','2001','2002','2003','2004','2005'])]

print(df2_bar)

x = np.arange(6)
width = 0.2
years = df2_bar['Years'].tolist()

plt.figure(dpi=144)
#To show main title of plot.
plt.title('Agricultural land (% of land area)')
# x is used for grouped bar chart. x is the position of 1 bar.
# x+0.2, x-0.2, x-0.4 these postion are used to show bar charts in groups.
plt.bar(x, df2_bar['Japan'], width, label='Japan')
plt.bar(x+0.2, df2_bar['Germany'], width, label='Germany')
plt.bar(x-0.2, df2_bar['Canada'], width, label='Canada')
plt.bar(x+0.4, df2_bar['United Kingdom'], width, label='United Kingdom')
# xticks are used to show years on x-axis of the plot.
plt.xticks(x, years)
# plt.yticks(np.arange(100,1000,200))
# x-axis label
plt.xlabel('Years')
# y-axis label
plt.ylabel('Agricultural land (% of land area)')
# legend function is called to make labels visibles on the chart like Seanson names.
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()

#-----------------------------------------------------------------------
#Bar chart 2
data_bar, data2_bar = get_data_frames('API_19_DS2_en_csv_v2_4700503.csv')
print(df2_bar)
data2_bar = data2_bar.loc[data2_bar['Indicator Code'].eq('AG.LND.FRST.ZS')]
# loc function used to get data of specific years 2000-2005 from dataframe.
print(data2_bar)
data2_bar = data2_bar.loc[data2_bar['Years'].
                          isin(['2000','2001','2002','2003','2004','2005'])]

print(data2_bar)

x = np.arange(6)
width = 0.2
years = data2_bar['Years'].tolist()

#P
plt.figure(dpi=144)

#To show main title of plot.
plt.title('Forest area (% of land area)')

# x is used for grouped bar chart. x is the position of 1 bar.
# x+0.2, x-0.2, x-0.4 these postion are used to show bar charts in groups.
plt.bar(x, data2_bar['Japan'], width, label='Japan')
plt.bar(x+0.2, data2_bar['Germany'], width, label='Germany')
plt.bar(x-0.2, data2_bar['Canada'], width, label='Canada')
plt.bar(x+0.4, data2_bar['United Kingdom'], width, label='United Kingdom')

# xticks are used to show years on x-axis of the plot.
plt.xticks(x, years)

# x-axis label
plt.xlabel('Years')

# y-axis label
plt.ylabel('Forest area (% of land area)')

#Legend function is called to make labels visibles on the chart.
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

#The function to show the figure.
plt.show()

#------------------------------------------------------------------------------
# Plotting the  pie chart of population growth for the countries : Japan, UK
#Canada and Germany

#Read the file into dataframes.
df, df2 = get_data_frames('API_19_DS2_en_csv_v2_4700503.csv')
df2 = df2.loc[df2['Indicator Code'].eq('SP.POP.GROW')]

#removing all the nan values.
df2.dropna()
print(df2.info())

Japan= np.sum(df2['Japan'])
Canada= np.sum(df2['Canada'])

Germany=np.sum(df2['Germany'])
uk= np.sum(df2["United Kingdom"])

total= Japan +Canada+uk+Germany

Japan= Japan/ total*100
Canada= Canada/ total*100
Germany=Germany/ total*100
uk= uk/ total*100

population_growth = np.array([Japan,Canada,uk,Germany])

#Plot the figure
plt.figure(dpi=144)
plt.pie(population_growth, labels= countries,autopct=('%1.1f%%'))

#Set the title
plt.title("Population growth (annual %)")

#Save the figure
plt.savefig("populationgrowth_pie")

#Show the figure
plt.show()
