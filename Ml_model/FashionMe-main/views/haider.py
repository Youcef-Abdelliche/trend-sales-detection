import dash_bootstrap_components as dbc
from dash import Input, Output, State, html
from maindash import app
from dash import dcc,html

maincolor = "#22242a"
secondaryColor= "#4ECDC4"
familyfont  = "Verdana"

containerStyle = {
    'height': '80px',
    'width': '100%',
    'maxHeight': '100%',
    'maxHeight': '100%',
    'align': 'start',
    'backgroundColor': 'orange',
    "float": "left"
}



MyInput_style = {
    'color': 'orange',
    'padding': '15px',
    'fontWeight': 'bold',
    "borderLeft": "1px solid lightgrey"  ,
    "borderRight": "1px solid lightgrey"  ,
    "borderTop": "4px solid "+secondaryColor ,
    "width":"800px",
    "fontFamily": familyfont,

}



SearchBAr = html.Div(
        children=[
            dbc.Row(
                            [ 
                            dbc.Col(
                                    [ 
                                        dcc.Input(
                                                        id="product_searched",
                                                      
                                                       
                                                        style=MyInput_style

                                                    ),

                                    ],
                                        align='center'      
                                    ),

                            dbc.Col(
                                    [     
                                           dbc.Button(
                                            "Lancer",
                                             className="btn btn-theme",
                                             id='submit-val',
                                              n_clicks=0
                                             ),
                                    ],
                                        align='center'
                                        
                                    ),
                            ],
                             justify="center"
                           ),   
        ]
)               

            
navbar = dbc.Navbar(
    dbc.Container(
       style=containerStyle,
       children= [
                    html.A(
                        dbc.Row(
                            [
                                dbc.Col(
                                    dbc.NavbarBrand(
                                        "FashionMe",
                                        style={
                                            "fontFamily": familyfont,
                                            "color": 'white',
                                            'fontWeight': 'bold',
                                             'fontSize':"30px"
                                              }
                                                
                                                    )
                                    ),
                            ],
                            align="center",
                            className="g-0",
                        ),
                        href="",
                        target="_blank",
                        style={"textDecoration": "none"},
                    ),
               
                    dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                    SearchBAr
             
        ]
    ),
    color="orange",
    dark=False,
)
Mainnavbar = html.Div([navbar])

# add callback for toggling the collapse on small screens
@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open