from assets.libraries import *

def card_p1(**kwargs):
    return dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H5(children='Índice', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['ind_car'], className="card-title"),

                    html.H5(children='Nombre', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['nom_car'], className="card-title"),

                    html.H5(children='Descripción', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['des_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),
                    
                    html.H5(children='Soporte', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['sop_car'], className="card-text"),
                    
                ]
            ),
        ],
        style={"width": "46%",'padding':'1rem 1rem 1rem 1rem','margin':'2% 2% 2% 2%','background-color':'#f8f9fa'},
    )

def card_p2(**kwargs):
    return dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H5(children='Índice', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['ind_car'], className="card-title"),
                    
                    html.H5(children='Nombre', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['nom_car'], className="card-title"),

                    html.H5(children='Descripción', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['des_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),
                    
                    html.H5(children='Soporte', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['sop_car'], className="card-text"),
                    
                ]
            ),
        ],
        style={"width": "46%",'padding':'1rem 1rem 1rem 1rem','margin':'2% 2% 2% 2%','background-color':'#f8f9fa'},
    )

def card_p3_p4_p5_p6(**kwargs):

    gastos=['Presupuesto 2021','Gasto 2021','Presupuesto 2022','Gasto 2022']
    return dbc.Card(
        [
            dbc.CardBody(
                [   
                    html.Div([
                        html.H3(children='Año 2021', className="card-title me-2",style={'font-weight':'bold'}),
                        html.Br(),
                        html.H5(children=gastos[0], className="card-title me-2",style={'font-weight':'bold'}),
                        html.P(children=f"$ {kwargs['pre_2021']:,}", className="card-text"),

                        html.H5(children=gastos[1], className="card-title me-2",style={'font-weight':'bold'}),
                        html.P(children=f"$ {kwargs['cos_2021']:,}", className="card-text"),
                    ],
                    style={'width': '50%','float': 'left'}
                    ),

                    html.Div([
                        html.H3(children='Año 2022', className="card-title me-2",style={'font-weight':'bold'}),
                        html.Br(),
                        html.H5(children=gastos[2], className="card-title me-2",style={'font-weight':'bold'}),
                        html.P(children=f"$ {kwargs['pre_2022']:,}", className="card-text"),

                        html.H5(children=gastos[3], className="card-title me-2",style={'font-weight':'bold'}),
                        html.P(children=f"$ {kwargs['cos_2022']:,}", className="card-text"),
                    ],
                    style={'width': '50%','float': 'left'}
                    ),

                    html.Div([
                        html.Br(),
                        html.H5(children='Soporte', className="card-title me-2",style={'font-weight':'bold'}),
                        html.P(children=kwargs['sop_car_2023'], className="card-text"),
                    ],
                    style={'width': '100%','float': 'left'}
                    ),                    
                ]
            ),
        ],
        style={"width": "96%",'padding':'1rem 1rem 1rem 1rem','margin':'2% 2% 2% 2%','background-color':'#f8f9fa'},
    )

def card_p7_p8_p9(**kwargs):

    gastos=['Funcionarios totales 2021',
            'Funcionarios manual 2021',
            'Funcionarios ocasionales 2021',
            'Funcionarios totales 2022',
            'Funcionarios manual 2022',
            'Funcionarios ocasionales 2022']
    return dbc.Card(
        [
            dbc.CardBody(
                [   
                    html.Div([
                        html.H3(children='Año 2021', className="card-title me-2",style={'font-weight':'bold'}),
                        html.Br(),
                        html.H5(children=gastos[0], className="card-title me-2",style={'font-weight':'bold'}),
                        html.P(children=f"{kwargs['can_2021']:,}", className="card-text"),

                        html.H5(children=gastos[1], className="card-title me-2",style={'font-weight':'bold'}),
                        html.P(children=f"{kwargs['fun_2021']:,}", className="card-text"),

                        html.H5(children=gastos[2], className="card-title me-2",style={'font-weight':'bold'}),
                        html.P(children=f"{kwargs['oca_2021']:,}", className="card-text"),
                    ],
                    style={'width': '50%','float': 'left'}
                    ),

                    html.Div([
                        html.H3(children='Año 2022', className="card-title me-2",style={'font-weight':'bold'}),
                        html.Br(),
                        html.H5(children=gastos[3], className="card-title me-2",style={'font-weight':'bold'}),
                        html.P(children=f"{kwargs['can_2022']:,}", className="card-text"),

                        html.H5(children=gastos[4], className="card-title me-2",style={'font-weight':'bold'}),
                        html.P(children=f"{kwargs['fun_2022']:,}", className="card-text"),

                        html.H5(children=gastos[5], className="card-title me-2",style={'font-weight':'bold'}),
                        html.P(children=f"{kwargs['oca_2022']:,}", className="card-text"),
                    ],
                    style={'width': '50%','float': 'left'}
                    ),

                    html.Div([
                        html.Br(),
                        html.H5(children='Soporte', className="card-title me-2",style={'font-weight':'bold'}),
                        html.P(children=kwargs['sop_car'], className="card-text"),
                    ],
                    style={'width': '100%','float': 'left'}
                    ),                    
                ]
            ),
        ],
        style={"width": "96%",'padding':'1rem 1rem 1rem 1rem','margin':'2% 2% 2% 2%','background-color':'#f8f9fa'},
    )

def card_p10_p11_p12(**kwargs):

    gastos=['Contratistas totales 2021',
            'Contratistas manual 2021',
            'Contratistas ocasionales 2021',
            'Contratistas totales 2022',
            'Contratistas manual 2022',
            'Contratistas ocasionales 2022']
    return dbc.Card(
        [
            dbc.CardBody(
                [   
                    html.Div([
                        html.H3(children='Año 2021', className="card-title me-2",style={'font-weight':'bold'}),
                        html.Br(),
                        html.H5(children=gastos[0], className="card-title me-2",style={'font-weight':'bold'}),
                        html.P(children=f"{kwargs['can_2021']:,}", className="card-text"),

                        html.H5(children=gastos[1], className="card-title me-2",style={'font-weight':'bold'}),
                        html.P(children=f"{kwargs['fun_2021']:,}", className="card-text"),

                        html.H5(children=gastos[2], className="card-title me-2",style={'font-weight':'bold'}),
                        html.P(children=f"{kwargs['oca_2021']:,}", className="card-text"),
                    ],
                    style={'width': '50%','float': 'left'}
                    ),

                    html.Div([
                        html.H3(children='Año 2022', className="card-title me-2",style={'font-weight':'bold'}),
                        html.Br(),
                        html.H5(children=gastos[3], className="card-title me-2",style={'font-weight':'bold'}),
                        html.P(children=f"{kwargs['can_2022']:,}", className="card-text"),

                        html.H5(children=gastos[4], className="card-title me-2",style={'font-weight':'bold'}),
                        html.P(children=f"{kwargs['fun_2022']:,}", className="card-text"),

                        html.H5(children=gastos[5], className="card-title me-2",style={'font-weight':'bold'}),
                        html.P(children=f"{kwargs['oca_2022']:,}", className="card-text"),
                    ],
                    style={'width': '50%','float': 'left'}
                    ),

                    html.Div([
                        html.Br(),
                        html.H5(children='Soporte', className="card-title me-2",style={'font-weight':'bold'}),
                        html.P(children=kwargs['sop_car'], className="card-text"),
                    ],
                    style={'width': '100%','float': 'left'}
                    ),                    
                ]
            ),
        ],
        style={"width": "96%",'padding':'1rem 1rem 1rem 1rem','margin':'2% 2% 2% 2%','background-color':'#f8f9fa'},
    )

def card_p13(**kwargs):
    return dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H5(children='Índice', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['ind_car'], className="card-title"),
                    
                    html.H5(children='Nombre', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['nom_car'], className="card-title"),

                    html.H5(children='Descripción', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['des_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),
                    
                    html.H5(children='Costo adquisición', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['cos_car'], className="card-text"),
                    
                    html.H5(children='Soporte', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['sop_car'], className="card-text"),
                    
                ]
            ),
        ],
        style={"width": "46%",'padding':'1rem 1rem 1rem 1rem','margin':'2% 2% 2% 2%','background-color':'#f8f9fa'},
    )

def card_p14_15_16_19_20(**kwargs):
    return dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H5(children='Índice', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['ind_car'], className="card-title"),
                    
                    html.H5(children='Nombre', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['nom_car'], className="card-title"),

                    html.H5(children='Actividades', className="card-title me-2",style={'font-weight':'bold'}),
                    dbc.Table(
                    children=[
                        html.Thead(html.Tr([html.Th("Act 1"), html.Th("Act 2"), html.Th("Act 3"), html.Th("Act 4"), html.Th("Act 5")])),
                        html.Tbody([html.Tr([html.Td(kwargs['act_1']), html.Td(kwargs['act_2']), html.Td(kwargs['act_3']), html.Td(kwargs['act_4']), html.Td(kwargs['act_5'])])])
                        ],
                    bordered=True,
                    #dark=True,
                    hover=True,
                    responsive=True,
                    striped=True,
                    ),

                    html.H5(children='Otra actividad', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['act_otr'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),

                    html.H5(children='Realizó alguna acción para responder al reto', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['acc_car'], className="card-text"),
                    
                    html.H5(children='Soporte', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['sop_car'], className="card-text"),
                    
                ]
            ),
        ],
        style={"width": "46%",'padding':'1rem 1rem 1rem 1rem','margin':'2% 2% 2% 2%','background-color':'#f8f9fa'},
    )

def card_p17_18_21_22(**kwargs):
    return dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H5(children='Índice', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['ind_car'], className="card-title"),
                    
                    html.H5(children='Nombre', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['nom_car'], className="card-title"),

                    html.H5(children='Usuarios', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['usr_car'], className="card-title"),

                ]
            ),
        ],
        style={"width": "46%",'padding':'1rem 1rem 1rem 1rem','margin':'2% 2% 2% 2%','background-color':'#f8f9fa'},
    )

def card_p23(**kwargs):
    return dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H5(children='Índice', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['ind_car'], className="card-title"),
                    
                    html.H5(children='Nombre', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['nom_car'], className="card-title"),

                    html.H5(children='Descripción', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['des_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),

                    dbc.Table(
                    children=[
                        html.Thead([
                            html.Tr([
                                html.Th("Crea 1"),
                                html.Th("Crea 2"),
                                html.Th("Crea 3"),
                            ])
                        ]                            
                        ),
                        html.Tbody([
                            html.Tr([
                                html.Td(kwargs['us1_car']),
                                html.Td(kwargs['us2_car']),
                                html.Td(kwargs['us3_car']),
                            ])
                        ]
                        )
                        ],
                    bordered=True,
                    hover=True,
                    responsive=True,
                    striped=True,
                    ),

                    html.H5(children='Prototipado', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['pro_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),

                    dbc.Table(
                    children=[
                        html.Thead([
                            html.Tr([
                                html.Th("Valida 1"),
                                html.Th("Valida 2"),
                                html.Th("Valida 3"),
                            ])
                        ]                            
                        ),
                        html.Tbody([
                            html.Tr([
                                html.Td(kwargs['va1_car']),
                                html.Td(kwargs['va2_car']),
                                html.Td(kwargs['va3_car']),
                            ])
                        ]
                        )
                        ],
                    bordered=True,
                    hover=True,
                    responsive=True,
                    striped=True,
                    ),
                    
                    html.H5(children='Soporte', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['sop_car'], className="card-text"),
                    
                ]
            ),
        ],
        style={"width": "46%",'padding':'1rem 1rem 1rem 1rem','margin':'2% 2% 2% 2%','background-color':'#f8f9fa'},
    )

def card_p24(**kwargs):
    return dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H5(children='Índice', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['ind_car'], className="card-title"),
                    
                    html.H5(children='Nombre', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['nom_car'], className="card-title"),

                    html.H5(children='Descripción', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['des_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),

                    html.H5(children='Impartió', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['imp_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),

                    html.H5(children='Asistentes', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['asi_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),
                    
                    html.H5(children='Soporte', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['sop_car'], className="card-text"),
                    
                ]
            ),
        ],
        style={"width": "46%",'padding':'1rem 1rem 1rem 1rem','margin':'2% 2% 2% 2%','background-color':'#f8f9fa'},
    )

def card_p25_p26(**kwargs):
    return dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H5(children='Índice', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['ind_car'], className="card-title"),
                    
                    html.H5(children='Nombre', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['nom_car'], className="card-title"),

                    html.H5(children='Descripción', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['des_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),

                    html.H5(children='Recomendaría', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['rec_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),
                    
                ]
            ),
        ],
        style={"width": "46%",'padding':'1rem 1rem 1rem 1rem','margin':'2% 2% 2% 2%','background-color':'#f8f9fa'},
    )

def card_p27(**kwargs):
    return dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H5(children='Índice', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['ind_car'], className="card-title"),
                    
                    html.H5(children='Nombre', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['nom_car'], className="card-title"),

                    html.H5(children='Descripción', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['des_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),

                    html.H5(children='Temática', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['tem_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),

                    html.H5(children='Tamaño del equipo', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['tam_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),
                    
                ]
            ),
        ],
        style={"width": "46%",'padding':'1rem 1rem 1rem 1rem','margin':'2% 2% 2% 2%','background-color':'#f8f9fa'},
    )

def card_p28(**kwargs):
    return dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H5(children='Índice', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['ind_car'], className="card-title"),
                    
                    html.H5(children='Nombre', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['nom_car'], className="card-title"),

                    html.H5(children='Implementó', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['imp_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),

                    html.H5(children='Validó', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['val_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),
                    
                    html.H5(children='Metodología', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['met_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),

                    html.H5(children='Beneficia ciudadanos', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['ben_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),

                    html.H5(children='Ciudadanos beneficiados', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['b1_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),

                    html.H5(children='Ahorra recursos', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['aho_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),

                    html.H5(children='Recursos ahorrados', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['a1_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),
                ]
            ),
        ],
        style={"width": "46%",'padding':'1rem 1rem 1rem 1rem','margin':'2% 2% 2% 2%','background-color':'#f8f9fa'},
    )

def card_p29_p30(**kwargs):
    return dbc.Card(
        [
            dbc.CardBody(
                [   
                    html.Div([
                        html.H3(children='Formados 2021', className="card-title me-2",style={'font-weight':'bold'}),
                        html.Br(),
                        html.P(children=f"{int(kwargs['for_2021'])}", className="card-text"),
                    ],
                    style={'width': '50%','float': 'left'}
                    ),

                    html.Div([
                        html.H3(children='Formados 2022', className="card-title me-2",style={'font-weight':'bold'}),
                        html.Br(),
                        html.P(children=f"{int(kwargs['for_2022'])}", className="card-text"),
                    ],
                    style={'width': '50%','float': 'left'}
                    ),
               
                ]
            ),
        ],
        style={"width": "96%",'padding':'1rem 1rem 1rem 1rem','margin':'2% 2% 2% 2%','background-color':'#f8f9fa'},
    )

def card_p31_p32(**kwargs):
    return dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H5(children='Índice', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['ind_car'], className="card-title"),
                    
                    html.H5(children='Codigo', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['cod_car'], className="card-title"),

                    html.H5(children='Nombre', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['nom_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),

                    html.H5(children='Descripción', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['des_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),
                    
                    html.H5(children='Soporte', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['sop_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),
                ]
            ),
        ],
        style={"width": "46%",'padding':'1rem 1rem 1rem 1rem','margin':'2% 2% 2% 2%','background-color':'#f8f9fa'},
    )

def card_p33_p34_p35_p36_p37_p38(**kwargs):
    return dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H5(children='Índice', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['ind_car'], className="card-title"),
                    
                    html.H5(children='Codigo', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['cod_car'], className="card-title"),
                    
                    html.H5(children='Soporte', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['sop_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),
                ]
            ),
        ],
        style={"width": "46%",'padding':'1rem 1rem 1rem 1rem','margin':'2% 2% 2% 2%','background-color':'#f8f9fa'},
    )

def card_p39(**kwargs):
    return dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H5(children='Índice', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['ind_car'], className="card-title"),
                    
                    html.H5(children='Medio', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['cod_car'], className="card-title"),
                    
                    html.H5(children='Soporte', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['sop_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),
                ]
            ),
        ],
        style={"width": "46%",'padding':'1rem 1rem 1rem 1rem','margin':'2% 2% 2% 2%','background-color':'#f8f9fa'},
    )