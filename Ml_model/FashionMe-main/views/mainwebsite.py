import time
from dash import dcc,html
import dash_bootstrap_components as dbc
from dash import Input, Output,  html,State
from maindash import app

from assets.additional_css import secondaryColor
from assets.additional_css import BodyStyle

import pandas as pd
import os
import json


from views.haider import Mainnavbar
from views.allTaps import make_taps
from mycontrollers.preprocessing import get_df_products


MainWebsite =  html.Div([
                      html.Div(
                        style= BodyStyle,
                        children=[                               
                                dbc.Spinner(
                                    fullscreen = False,
                                    color = secondaryColor,
                                    size = "md",
                                    type = "grow",
                                    show_initially  = False,
                                    spinner_style = {"width": "120px","height": "120px","margin":"300px 0px 5px 0px" },
                                    children=[
                                        html.Div(id="loading-output-spinner")
                                    ]
                                 ),
                                ],
                             ),

                    ]
                    )



description_website = html.Div(
            style={"margin":"50px 5px 5px 50px" },
            children=[ 
               
                html.Br(),
                html.H4("FashionMe is a new tool for analysing products trends based on products sales.") ,  
                html.Br(),
                html.Br(),

                html.H5("Services :"),
                html.Br(),

                html.H5("1) With simple clicks you can use our website to find the cheapest product for particular brand and sexe.  "),
                html.H5("2) FashionMe gives you the specific price, average prices, best products based on linear formula and more informations on a specific product. "),
                html.H5("3) You can detect easily the trend brands and choose the best brand for your new product. "),
                html.H5("4) You can have a good see on the price distribution of the products in the same brand.  "),
             
             
                ]
                        
                         )
@app.callback(
    Output('loading-output-spinner', 'children'),
    Input('submit-val', 'n_clicks'),
    State('product_searched', 'value')
)
def update_output(n_clicks, product_searched):
    if n_clicks:
        return make_taps()
    else :
        return description_website
