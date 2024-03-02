# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 15:01:20 2023

@author: 48660
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


#Downloading the data
games = pd.read_csv("C://Users//48660//Desktop//NBA dataset//games.csv")
column_names = games.columns.values
seasons = games['SEASON'].unique()
print("Names of columns: ", column_names, "\n \n")

#Basic information


print("Dataframe shape: ",games.shape, "\n \n")
#GAMES INFO
print("Dataframe info: \n")
games.info()
print("\n \n")


#Describe basic statistical characteristics
games_deleted_columns = games.drop(['GAME_ID', 'GAME_STATUS_TEXT' ,'HOME_TEAM_ID',
 'VISITOR_TEAM_ID', 'SEASON' ,'TEAM_ID_home', 'TEAM_ID_away', 'GAME_DATE_EST'], axis=1)  #deleting unnecessary columns (team, place in league)
column_names = games_deleted_columns.columns.values

describe = games_deleted_columns.describe()
print("stats describe: \n", describe, "\n \n")

games_normalized = games_deleted_columns

#Optional normalization
#games_normalized = (games_deleted_columns - games_deleted_columns.min()) / (games_deleted_columns.max() - games_deleted_columns.min())

matrix = games_normalized.corr()
plt.figure(dpi = 1000)
sns.heatmap(matrix, vmin = -1, vmax = 1, xticklabels=games_normalized.columns,
            annot = True, fmt = '.2f',
            annot_kws = {"fontsize" : 6}
            )
plt.savefig('Heatmap.png', dpi = 100)
plt.show()



#boxplots collectively
plt.subplots(nrows = 3, ncols = 5, dpi = 1000)
for index in range(12):
    data =  games_normalized[column_names[index]]
    plt.subplot(3, 4, index+1)
    sns.boxplot(data,)
    plt.title(column_names[index])

plt.subplots_adjust(wspace=1, 
                    hspace=1)
plt.show()

outliers_num = []
for index in range(len(column_names)):
    #tworzenie boxplotow kazdy osobno
    data =  games_normalized[column_names[index]]
    plt.figure()
    sns.boxplot(data =data)
    plt.title(column_names[index])
    plt.show()

    #numbers of outliers
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    outlier_condition = ((data < (Q1 - 1.5*IQR)) | (data > (Q3 + 1.5*IQR)))
    outliers_num.append(sum(outlier_condition))


outliers_df = pd.DataFrame({'Outliers': outliers_num, 'Columns': column_names})
print("Number of outliers: \n", outliers_df)
