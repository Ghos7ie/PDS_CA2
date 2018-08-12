import pandas as pd
import pymongo
from pymongo import MongoClient
import matplotlib.pyplot as plt

client = MongoClient()
db = client['pds_CA2']

dataCrimeT = pd.DataFrame(list(db.crimeRatesTypes.find()))

types = dataCrimeT['crime_classes'].unique()

# Used to plot lines
def plotLines (type_list):
    for typeC in type_list:
        # Set what rows of data are used
        dataUsed = dataCrimeT.loc[dataCrimeT['crime_classes']==typeC]
        axis4.plot(dataUsed['year'], dataUsed['crime_cases'], label=typeC, marker = 'o',markersize=4)
        
# Plotting
linePlot = plt.figure(figsize=(10,8))
axis4 = linePlot.add_subplot(111)
## Set title
plt.title('Crime Cases by Type')
## Set x and y labels
plt.xlabel('Year', fontsize=20, labelpad=15)
plt.ylabel('Cases', fontsize=20, labelpad=15)
## Rotate x ticks
plt.xticks(rotation=45)
plotLines(types)
axis4.legend(loc="upper left",bbox_to_anchor=(1,1), fontsize=8)
plt.show()
