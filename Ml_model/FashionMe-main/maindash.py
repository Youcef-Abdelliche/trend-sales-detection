import dash
import dash_bootstrap_components as dbc

# Instance de l'application dash pour la gestion des événements
dbc_css = ("https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.2/dbc.min.css")
external_stylesheets = dbc.themes.BOOTSTRAP

app = dash.Dash(__name__,
 external_stylesheets=[external_stylesheets, dbc_css],
 assets_folder= "assets",
 title= "FashionMe",
 suppress_callback_exceptions=True
 )

