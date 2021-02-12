import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app.app import dash_app
import app.graph as graph

dash_app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

app = dash_app.server

@dash_app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return graph.layout
    else:
        print(pathname)
        return '404'



if __name__ == '__main__':
    # dash_app.run_server(host='0.0.0.0', debug=True, port=8080)
    dash_app.run_server(debug=True)
