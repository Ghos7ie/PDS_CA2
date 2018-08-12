## Data Extraction

import pandas as pd
import numpy as np
import pymongo
from pymongo import MongoClient
import os
import glob

# Population size
file1 = 'data/API_SP.POP.TOTL_DS2_en_csv_v2_10058048.csv'
# Mobile Data usage
file2 = 'data/mobile-data-usage.csv'
# Mobile Usage (Activities)
file3 = 'data/usage-of-mobile-devices-for-media-activities.csv'
# Overall crime rates
file4 = 'data/overall-crime-cases-crime-rate.csv'
# Overall crime rates by crime type
file5 = 'data/overall-crime-cases-reported-by-crime-classes.csv'
# Distribution of mobile vs desktop vs tablet

df1 = pd.read_csv(file1, encoding='utf-8', skiprows=4)
df2 = pd.read_csv(file2, encoding='utf-8')
df3 = pd.read_csv(file3, encoding='utf-8')
df4 = pd.read_csv(file4, encoding='utf-8')
df5 = pd.read_csv(file5, encoding='utf-8')
# Distribution of mobile vs desktop vs tablet
def readCompare ():
    # define dir path
    path =r'C:\Jupyter\PDS_CA2\data\comparison'
    # gets all files that end with csv
    allFiles = glob.glob(os.path.join(path, "*.csv"))
    # loop within to read all csv and concat into df
    df = pd.concat((pd.read_csv(f) for f in allFiles))
    df = df.reset_index(drop=True)
    return df.fillna(0)
# end function   
df6 = readCompare()

# Getting info on each dataset

# df1
print('<-- Dataset 1 - Population size -->');print()
print(df1.info())
print('-----end-----');print()

# df2
print('<-- Dataset 2 - Mobile Data Usage -->');print()
print(df2.info())
print('-----end-----');print()

# df3
print('<-- Dataset 3 - Mobile Usage (Activities) -->');print()
print(df3.info())
print('-----end-----');print()

# df4
print('<-- Dataset 4 - Overall crime rates -->');print()
print(df4.info())
print('-----end-----');print()

# df5
print('<-- Dataset 5 - Overall crime rates by crime types -->');print()
print(df5.info())
print('-----end-----');print()

############################################################
### Extracting data from each dataset within 2008 - 2015 ###
############################################################

# create array containing years 2008 - 2015
years_used = np.arange(2008,2016)

# File 1 - Population size
# File 1 - Population size
df1e = df1.loc[df1['Country Name']=='Singapore']
# Drop unneccessary rows
df1e = df1e.drop(['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code', 'Unnamed: 62'], axis=1)
# transpose the dataframe
df1e = df1e.T
# reset index so that year column will come out and then rename it
df1e = df1e.reset_index()
df1e = df1e.rename(index=str, columns={'index':'year',
                                      206:'population'})
# get years i need
df1e = df1e.iloc[45:55,:]
df1e = df1e.reset_index(drop=True)

# File 2 - Mobile Data usage
df2e = df2.iloc[df2['quarter'].iloc[14:46].index].reset_index(drop=True)

# Remaining datasets do not need extraction

# function meant to insert Data to mongoDb
def insertData (collectName, df):
    collection = db[collectName]
    collection.insert_many(df.to_dict('records'))    
    
client = MongoClient()
db = client['pds_CA2']
insertData('populationSize', df1e)
insertData('mobileDataUsage', df2e)
insertData('mobileActivities', df3)
# converting year to string because IT WON'T SUCCEED OTHERWISE
df4['year'] = df4['year'].astype(str)
insertData('crimeRates', df4)
insertData('crimeRatesTypes', df5)   
insertData('deviceCompare', df6)
