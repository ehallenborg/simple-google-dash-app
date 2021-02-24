import dash_html_components as html


def template(template_name: str, dropdown_menu, table):
    return html.Div([
        html.H2('The Promised Neverland',
                    style={'font-size': '3.65em',
                        'font-weight': 'bolder',
                        'font-family': 'Product Sans',
                        'color': "rgba(117, 117, 117, 0.95)",
                        'margin-top': '20px',
                        'margin-bottom': '0',
                        'text-align': 'center'
                            }),
        html.H2(
                html.Img(src="https://upload.wikimedia.org/wikipedia/commons/5/5a/The-promised-neverland-logo.svg",
                style={
                    'height': '100px',
                    'display': 'block',
                    'margin-bottom': '10px',
                    'margin-left': 'auto',
                    'margin-right': 'auto'
                })
        ),
        dropdown_menu,
        html.Div(id='graphs-' + template_name),
                html.H4('MyAnimeList Scores',
                    style={"display": "inline",
                        'font-size': '1.65em',
                        'margin-left': '7px',
                        'font-weight': 'bolder',
                        'font-family': 'Product Sans',
                        'color': "rgba(117, 117, 117, 0.95)",
                        'margin-top': '20px',
                        'margin-bottom': '20px',
                            }),
        table
    ], className='container')
