import dash
import dash_bootstrap_components as dbc

dash_app = dash.Dash(
        'The Promised Neverland',
        external_stylesheets=[
            "https://fonts.googleapis.com/css?family=Product+Sans:400,400i,700,700i",
            "https://cdn.rawgit.com/plotly/dash-app-stylesheets/2cc54b8c03f4126569a3440aae611bbef1d7a5dd/stylesheet.css",
            "https://codepen.io/bcd/pen/KQrXdb.css"
            ]
        )

dash_app.config.suppress_callback_exceptions = True
