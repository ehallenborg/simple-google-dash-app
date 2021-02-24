import dash_core_components as dcc
import plotly.graph_objs as go
import dash_table
from dash.dependencies import Input, Output
import pandas as pd

import app.template as template
from app.app import dash_app
from utils.google import Google

APPS_NAME = 'Promised Neverland Season 2'
g = Google()
df = g.get_data()
df['Date'] = pd.to_datetime(df['Date'])
df_table = df.copy()
df_table['Date'] = df_table['Date'].dt.strftime('%m/%d/%Y')
df_table = df_table.drop(columns=['Source'])


dropdown_menu = dcc.Dropdown(id='data-input-' + APPS_NAME,
                            options=[ {'label': 'MAL', 'value': 'Score'}],
                            value=['Score'],
                            multi=True)

table = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df_table.columns],
    style_cell={'textAlign': 'center'},
    style_header={
        'backgroundColor': 'rgb(230, 230, 230)',
        'fontWeight': 'bold'
    },
    style_as_list_view=True,
    data=df_table.to_dict('records'),
)

layout = template.template(APPS_NAME, dropdown_menu=dropdown_menu, table=table)

def score(value_name: str):
    data_1 = go.Scatter(x=df['Date'], y=df['Score'], name="Score", mode="markers")
    data = [data_1]
    layout = dict(title='Change of Score Over Time',
                xaxis=dict(title='Date'),
                yaxis=dict(title='MAL Score'),
    )
    fig = dict(data=data, layout=layout)
    return dcc.Graph(
        id=value_name,
        figure=fig,
    )

def bar(value_name: str):
    dcc.Graph(
        id='bar-graph',
        figure={
            'data': [
                {'x': df['Date'], 'y': df['Score'], 'type': 'bar', 'name': 'Score'},
            ],
            'layout': {
                'title': 'Change of Score Over Time'
            }
        }
    )


@dash_app.callback(
    Output('graphs-' + APPS_NAME, 'children'),
    [Input('data-input-' + APPS_NAME, 'value')],
)

def update_graph(data):
    graphs = []
    for x in data:
        if x == 'Score':
            graphs.append(score(x))

    return graphs
