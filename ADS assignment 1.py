# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 14:30:25 2022

@author: kjide
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
cols = [0, 2, 3, 4, 9, 10]   # Columns of interest

# Read file into DataFrame, extract columns and print
GasPrices = pd.read_csv("gas_prices.csv", usecols=(cols))
print(GasPrices)

# Use iloc to extract rows 10 to 18
df_recent = GasPrices.iloc[-9:]
print(df_recent)

# Line Plot
# Define Line Plot Functions
def line_plot(x_axis, y_data, xticks, label, title):
    plt.figure(figsize=(10,5))
    for i in range(len(y_data)):
        plt.plot(x_axis,y_data[i],label=label[i])
    plt.legend()
    plt.xticks(x_axis,xticks)
    plt.title(title,fontsize=8)
    return

x_axis = df_recent["Year"].index
y_data = [df_recent["Canada"],df_recent["France"],df_recent["Germany"],
          df_recent["UK"],df_recent["USA"]]
xticks = ["2000","2001","2002","2003","2004","2005","2006","2007","2008"]
label = ["Canada","France","Germany","UK","USA"]
title = 'Line Plot Showing The GasPrices in 5 Selected Countries (2000-2008)'

line_plot(x_axis, y_data, xticks, label, title)

plt.xlabel("Year")
plt.ylabel("GasPrices($)")
plt.show()


# BAR PLOT
bar_data = df_recent.drop(["Canada", "USA"], axis=1)  # Drop Columns Canada and USA
print(bar_data)

# Define Bar Plot Functions
def bar_chart(country1, country2, country3):
    plt.subplots(figsize=(10, 6))
    width = wt
    ct1 = np.arange(len(country1))
    ct2 = [x + width for x in ct1]
    ct3 = [x + width for x in ct2]
    plt.bar(ct1, country1, color='blue', width=wt, label=lab1)
    plt.bar(ct2, country2, color='red', width=wt, label=lab2)
    plt.bar(ct3, country3, color='green', width=wt, label=lab3)
    plt.xticks([s + width for s in range(len(country1))], ["2000", "2001", "2002", "2003", "2004", 
                                                       "2005", "2006", "2007", "2008"])
    plt.legend()
   
    return

wt = 0.2
country1 = bar_data["France"]
country2 = bar_data["Germany"]
country3 = bar_data["UK"]
lab1 = "France"
lab2 = "Germany"
lab3 = "UK"
bar_chart(country1, country2, country3)
plt.xlabel("Year")
plt.ylabel("GasPrices($)")
plt.title("Bar Plot Showing The GasPrices in 3 European Countries")

plt.show()


# PIE CHART
# Define Pie Chart Functions
def subplot_pie_chart(x_axis,label,title):
     plt.figure(figsize=(8,7))
     for i in range(len(x_axis)):
         plt.subplot(2,2, i+1).set_title(title[i])
         plt.pie(x_axis[i],labels=label) 
     plt.show()
     
x_axis = [df_recent["Canada"],df_recent["France"],df_recent["Germany"],
          df_recent["UK"]]
label = df_recent["Year"]
title = ["Canada","France","Germany","UK"]
subplot_pie_chart(x_axis,label,title)


