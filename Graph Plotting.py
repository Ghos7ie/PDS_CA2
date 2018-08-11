
# coding: utf-8

# # Plotting of Data

# **Steps**
# 1. Retrieve data from MongoDb
# 2. Set up Dash
# 3. DISPLAY THE GODDAMN SHIT JESUS

# # 1. Population Size

# In[ ]:


import pandas as pd
import pymongo
from pymongo import MongoClient
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go


client = MongoClient()
db = client['pds_CA2']

dataPopulation = pd.DataFrame(list(db.populationSize.find()))
print(dataPopulation)

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='How are crime rates affected by the size of the population?'),

    html.Div(children='''
        First, we try to see how the population has been doing from 2005 to 2015
    '''),

    dcc.Graph(
        id='population-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [dataPopulation.year], 'y':[dataPopulation.population], 'type':'bar', 'name':'Singapore Population'},
            ],
            'layout': {
                'title': 'Population Size'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=False)

