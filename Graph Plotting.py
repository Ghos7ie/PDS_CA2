
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
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Population Size'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=False)

