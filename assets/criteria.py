from assets.libraries import *

def criterio_1():
    salida_criterio=html.Div(children=[
                dbc.Table(
                    children=[
                        html.Thead(children=[

                            html.Tr([
                                html.Th("Nota máxima",colSpan=1),
                                html.Th("Nota por criterio",colSpan=1),
                                html.Th("Criterios",colSpan=1),
                            ],
                            ),
                        ]),

                        html.Tbody([
                            html.Tr([
                                html.Td(0,rowSpan=3),
                                html.Td(0),
                                html.Td('N/A'),
                            ]),
                            html.Tr([
                                html.Td(0),
                                html.Td('N/A'),
                            ]),
                            html.Tr([
                                html.Td(0),
                                html.Td(f'''N/A'''),
                            ]),
                        ])
                    ],
                    bordered=True,
                    hover=True,
                    responsive=True,
                    striped=True,
                ),
            ],style={'width': '100%'})
    return salida_criterio

def criterio_2():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=1),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(4,rowSpan=5),
                        html.Td(4*0.3),
                        html.Td('Asignado a todos automáticamente'),
                    ]),
                    html.Tr([
                        html.Td(4*0.3),
                        html.Td('Comparación con 2021'),
                    ]),
                    html.Tr([
                        html.Td(4*0.4,rowSpan=3),
                        html.Td(f'''Criterio 1: Relevancia estratégica'''),
                    ]),
                    html.Tr([
                        html.Td(f'''Criterio 2: Impacto potencial'''),
                    ]),
                    html.Tr([
                        html.Td(f'''Criterio 3: Nivel de novedad'''),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_3():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=1),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(1,rowSpan=1),
                        html.Td(1),
                        html.Td('Asignado automáticamente por responder un valor'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio
        
def criterio_4():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(3,rowSpan=5),
                        html.Td(1),
                        html.Td('Asignado a todos automáticamente',colSpan=2),
                    ]),
                    html.Tr([
                        html.Td(2,rowSpan=3),
                        html.Td(2),
                        html.Td(f'Si es mayor a promedio distrital'),
                    ]),
                    html.Tr([
                        html.Td(1),
                        html.Td(f'Si es menor a promedio distrital'),
                    ]),
                    html.Tr([
                        html.Td(0),
                        html.Td(f'Si no tiene valor'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_5():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=1),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(1,rowSpan=1),
                        html.Td(1),
                        html.Td('Asignado automáticamente por responder un valor'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_6():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(2.7,rowSpan=5),
                        html.Td(1),
                        html.Td('Asignado a todos automáticamente',colSpan=2),
                    ]),
                    html.Tr([
                        html.Td(1.7,rowSpan=3),
                        html.Td(1.7),
                        html.Td(f'Si es mayor a promedio distrital'),
                    ]),
                    html.Tr([
                        html.Td(1),
                        html.Td(f'Si es menor a promedio distrital'),
                    ]),
                    html.Tr([
                        html.Td(0),
                        html.Td(f'Si no tiene valor'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_7():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=1),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(2,rowSpan=1),
                        html.Td(2),
                        html.Td('Asignado automáticamente por responder un valor'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_8():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(1,rowSpan=4),
                        html.Td('Comparación 2021: 50%',rowSpan=4),
                    ]),
                    html.Tr([
                        html.Td(1),
                        html.Td('Si es mayor'),
                    ]),
                    html.Tr([
                        html.Td(0.5),
                        html.Td('Si es menor'),
                    ]),
                    html.Tr([
                        html.Td(0),
                        html.Td('Si no tiene valor'),
                    ]),



                    html.Tr([
                        html.Td(1,rowSpan=4),
                        html.Td('Comparación media distrital: 50%',rowSpan=4),
                    ]),
                    html.Tr([
                        html.Td(1),
                        html.Td('Si es mayor'),
                    ]),
                    html.Tr([
                        html.Td(0.5),
                        html.Td('Si es menor'),
                    ]),
                    html.Tr([
                        html.Td(0),
                        html.Td('Si no tiene valor'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_9():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=1),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(0,rowSpan=1),
                        html.Td(0),
                        html.Td('Pregunta no es suficientemente sensible'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_10():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=1),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(2,rowSpan=1),
                        html.Td(2),
                        html.Td('Asignado automáticamente por responder un valor'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_11():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(1,rowSpan=4),
                        html.Td('Comparación 2021: 50%',rowSpan=4),
                    ]),
                    html.Tr([
                        html.Td(1),
                        html.Td('Si es mayor'),
                    ]),
                    html.Tr([
                        html.Td(0.5),
                        html.Td('Si es menor'),
                    ]),
                    html.Tr([
                        html.Td(0),
                        html.Td('Si no tiene valor'),
                    ]),



                    html.Tr([
                        html.Td(1,rowSpan=4),
                        html.Td('Comparación media distrital: 50%',rowSpan=4),
                    ]),
                    html.Tr([
                        html.Td(1),
                        html.Td('Si es mayor'),
                    ]),
                    html.Tr([
                        html.Td(0.5),
                        html.Td('Si es menor'),
                    ]),
                    html.Tr([
                        html.Td(0),
                        html.Td('Si no tiene valor'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_12():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=1),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(0,rowSpan=1),
                        html.Td(0),
                        html.Td('Pregunta no es suficientemente sensible'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_13():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(1.38,rowSpan=4),
                        html.Td('Comparación facilitar innovación 2021: 30%',rowSpan=4),
                    ]),
                    html.Tr([
                        html.Td(1.38),
                        html.Td('Si es mayor'),
                    ]),
                    html.Tr([
                        html.Td(0.7),
                        html.Td('Si es menor'),
                    ]),
                    html.Tr([
                        html.Td(0),
                        html.Td('Si no tiene valor'),
                    ]),



                    html.Tr([
                        html.Td(3.22,rowSpan=4),
                        html.Td('Valoración de criterios: 70%',rowSpan=4),
                    ]),
                    html.Tr([
                        html.Td(1),
                        html.Td('Criterio 1: Grado de novedad'),
                    ]),
                    html.Tr([
                        html.Td(1.22),
                        html.Td('Criterio 2: Aporte a la innovación'),
                    ]),
                    html.Tr([
                        html.Td(1),
                        html.Td('Criterio 3: Categoría a la que pertenece'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),

        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Categoría",colSpan=1),
                        html.Th("Nota",colSpan=1),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(1,rowSpan=7),
                        html.Td(0.5),
                        html.Td('Gestión documental'),
                    ]),
                    html.Tr([
                        html.Td(0.5),
                        html.Td('Asistencia virtual y chatbot'),
                    ]),
                    html.Tr([
                        html.Td(0.5),
                        html.Td('Seguridad y protección'),
                    ]),
                    html.Tr([
                        html.Td(1),
                        html.Td('Geolocalización y cartografía'),
                    ]),
                    html.Tr([
                        html.Td(1),
                        html.Td('Sistemas de información misional'),
                    ]),
                    html.Tr([
                        html.Td(1),
                        html.Td('Comunicación y colaboración'),
                    ]),
                    html.Tr([
                        html.Td(1),
                        html.Td('Analisis y visualización de datos'),
                    ]),

                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_14():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(2.8,rowSpan=4),
                        html.Td(0.9),
                        html.Td('Elaboró documento'),
                    ]),
                    html.Tr([
                        html.Td(0.9),
                        html.Td('Planificó acciones'),
                    ]),
                    html.Tr([
                        html.Td(1),
                        html.Td('Socializó info'),
                    ]),
                    html.Tr([
                        html.Td('Depende de faltante'),
                        html.Td('Otro (comodin)'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_15():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(1,rowSpan=4),
                        html.Td(0.3),
                        html.Td('Elaboró documento'),
                    ]),
                    html.Tr([
                        html.Td(0.3),
                        html.Td('Planificó acciones'),
                    ]),
                    html.Tr([
                        html.Td(0.4),
                        html.Td('Socializó info'),
                    ]),
                    html.Tr([
                        html.Td('Depende de faltante'),
                        html.Td('Otro (comodin)'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_16():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(2.8,rowSpan=4),
                        html.Td(0.9),
                        html.Td('Elaboró documento'),
                    ]),
                    html.Tr([
                        html.Td(0.9),
                        html.Td('Planificó acciones'),
                    ]),
                    html.Tr([
                        html.Td(1),
                        html.Td('Socializó info'),
                    ]),
                    html.Tr([
                        html.Td('Depende de faltante'),
                        html.Td('Otro (comodin)'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_17():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(1.2,rowSpan=4),
                        html.Td(0),
                        html.Td('0 CANALES'),
                    ]),
                    html.Tr([
                        html.Td(0.6),
                        html.Td('1 CANAL'),
                    ]),
                    html.Tr([
                        html.Td(0.9),
                        html.Td('2-3 CANALES'),
                    ]),
                    html.Tr([
                        html.Td(1.2),
                        html.Td('4 O MAS CANALES'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_18():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(1.2,rowSpan=4),
                        html.Td(0),
                        html.Td('0 CANALES'),
                    ]),
                    html.Tr([
                        html.Td(0.6),
                        html.Td('1 CANAL'),
                    ]),
                    html.Tr([
                        html.Td(0.9),
                        html.Td('2-3 CANALES'),
                    ]),
                    html.Tr([
                        html.Td(1.2),
                        html.Td('4 O MAS CANALES'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_19():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(3,rowSpan=4),
                        html.Td(1),
                        html.Td('Elaboró documento'),
                    ]),
                    html.Tr([
                        html.Td(1),
                        html.Td('Planificó acciones'),
                    ]),
                    html.Tr([
                        html.Td(1),
                        html.Td('Socializó info'),
                    ]),
                    html.Tr([
                        html.Td('Depende de faltante'),
                        html.Td('Otro (comodin)'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_20():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(3,rowSpan=4),
                        html.Td(1),
                        html.Td('Elaboró documento'),
                    ]),
                    html.Tr([
                        html.Td(1),
                        html.Td('Planificó acciones'),
                    ]),
                    html.Tr([
                        html.Td(1),
                        html.Td('Socializó info'),
                    ]),
                    html.Tr([
                        html.Td('Depende de faltante'),
                        html.Td('Otro (comodin)'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_21():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(1,rowSpan=4),
                        html.Td(0),
                        html.Td('0 CANALES'),
                    ]),
                    html.Tr([
                        html.Td(0.5),
                        html.Td('1 CANAL'),
                    ]),
                    html.Tr([
                        html.Td(0.75),
                        html.Td('2-3 CANALES'),
                    ]),
                    html.Tr([
                        html.Td(1),
                        html.Td('4 O MAS CANALES'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_22():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(1,rowSpan=4),
                        html.Td(0),
                        html.Td('0 CANALES'),
                    ]),
                    html.Tr([
                        html.Td(0.5),
                        html.Td('1 CANAL'),
                    ]),
                    html.Tr([
                        html.Td(0.75),
                        html.Td('2-3 CANALES'),
                    ]),
                    html.Tr([
                        html.Td(1),
                        html.Td('4 O MAS CANALES'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_23():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(7,rowSpan=4),
                        html.Td(5),
                        html.Td('Criterio del analista'),
                    ]),
                    html.Tr([
                        html.Td(2),
                        html.Td('Validez del prototipo'),
                    ]),

                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_24():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(6,rowSpan=5),
                        html.Td(1.2),
                        html.Td('Eventos propios'),
                    ]),
                    html.Tr([
                        html.Td(1.2),
                        html.Td('Eventos de otras entidades'),
                    ]),
                    html.Tr([
                        html.Td(1.2),
                        html.Td('Formación propia'),
                    ]),
                    html.Tr([
                        html.Td(1.2),
                        html.Td('Formación de otras entidades'),
                    ]),
                    html.Tr([
                        html.Td(1.2),
                        html.Td('Otras actividades'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_25():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(2.8,rowSpan=5),
                        html.Td(2.8),
                        html.Td('Esfuerzo'),
                    ]),
                    html.Tr([
                        html.Td(2.8),
                        html.Td('Alcance'),
                    ]),
                    html.Tr([
                        html.Td(2.8),
                        html.Td('Normativización'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_26():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(1.1,rowSpan=3),
                        html.Td(1.1),
                        html.Td('Esfuerzo'),
                    ]),
                    html.Tr([
                        html.Td(1.1),
                        html.Td('Alcance'),
                    ]),
                    html.Tr([
                        html.Td(1.1),
                        html.Td('Normativización'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_27():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(1.1,rowSpan=5),
                        html.Td(1.1),
                        html.Td('Lab, semillero y observatorio'),
                    ]),
                    html.Tr([
                        html.Td(0.5),
                        html.Td('Mesas técnicas, comités, equipos u otros que maso con innovación'),
                    ]),
                    html.Tr([
                        html.Td(0),
                        html.Td('Otros no relacionados con innovación'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_28():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(20.5,rowSpan=5),
                        html.Td(9),
                        html.Td('Implementada o en implementación'),
                    ]),
                    html.Tr([
                        html.Td(5),
                        html.Td('Validada con usuarios'),
                    ]),
                    html.Tr([
                        html.Td(3),
                        html.Td('Metodología utilizada'),
                    ]),
                    html.Tr([
                        html.Td(2),
                        html.Td('Befenicia a ciudadanos'),
                    ]),
                    html.Tr([
                        html.Td(1.5),
                        html.Td('Ahorra recursos'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_29():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(2.2,rowSpan=5),
                        html.Td(1),
                        html.Td('Asignado a todos automáticamente',colSpan=2),
                    ]),
                    html.Tr([
                        html.Td(1.2,rowSpan=3),
                        html.Td(1.2),
                        html.Td(f'Si es mayor a promedio distrital'),
                    ]),
                    html.Tr([
                        html.Td(.6),
                        html.Td(f'Si es menor a promedio distrital'),
                        
                    ]),
                    html.Tr([
                        html.Td(0),
                        html.Td(f'Si no tiene valor'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_30():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(2.2,rowSpan=5),
                        html.Td(1),
                        html.Td('Asignado a todos automáticamente',colSpan=2),
                    ]),
                    html.Tr([
                        html.Td(1.2,rowSpan=3),
                        html.Td(1.2),
                        html.Td(f'Si es mayor a promedio distrital'),
                    ]),
                    html.Tr([
                        html.Td(.6),
                        html.Td(f'Si es menor a promedio distrital'),
                        
                    ]),
                    html.Tr([
                        html.Td(0),
                        html.Td(f'Si no tiene valor'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_31():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(1.5,rowSpan=5),
                        html.Td(1.5),
                        html.Td('Existen acuerdos/actos en innovación',colSpan=2),
                    ]),

                    html.Tr([
                        html.Td(0),
                        html.Td(f'NO existen acuerdos/actos en innovación'),
                        
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_32():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(1.5,rowSpan=5),
                        html.Td(1.5),
                        html.Td('Existen enfoques / líneas / componentes / proyectos / programas o planes',colSpan=2),
                    ]),

                    html.Tr([
                        html.Td(0),
                        html.Td(f'No existen enfoques / líneas / componentes / proyectos / programas o planes'),
                        
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_33():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(1,rowSpan=5),
                        html.Td(1),
                        html.Td('Publicó retos en innovación desde ciudadanos',colSpan=2),
                    ]),

                    html.Tr([
                        html.Td(0),
                        html.Td(f'NO Publicó retos en innovación desde ciudadanos'),
                        
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_34():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(1,rowSpan=5),
                        html.Td(1),
                        html.Td('Publicó retos en innovación desde funcionarios/contratistas',colSpan=2),
                    ]),

                    html.Tr([
                        html.Td(0),
                        html.Td(f'NO Publicó retos en innovación desde funcionarios/contratistas'),
                        
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_35():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(1,rowSpan=5),
                        html.Td(1),
                        html.Td('Publicó ideas desde ciudadanos',colSpan=2),
                    ]),

                    html.Tr([
                        html.Td(0),
                        html.Td(f'NO Publicó ideas desde ciudadanos'),
                        
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_36():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(1,rowSpan=5),
                        html.Td(1),
                        html.Td('Publicó ideas desde funcionarios/contratistas',colSpan=2),
                    ]),

                    html.Tr([
                        html.Td(0),
                        html.Td(f'NO Publicó ideas desde funcionarios/contratistas'),
                        
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_37():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(1,rowSpan=5),
                        html.Td(1),
                        html.Td('Publicó buenas prácticas y lecciones en innovación',colSpan=2),
                    ]),

                    html.Tr([
                        html.Td(0),
                        html.Td(f'NO publicó buenas prácticas y lecciones en innovación'),
                        
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_38():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(1,rowSpan=5),
                        html.Td(1),
                        html.Td('Publicó buenas prácticas y lecciones de la entidad',colSpan=2),
                    ]),

                    html.Tr([
                        html.Td(0),
                        html.Td(f'NO publicó buenas prácticas y lecciones de la entidad'),
                        
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_39():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(6,rowSpan=5),
                        html.Td(6),
                        html.Td('Documento o matriz para hacer monitoreo y seguimiento a las innovaciones implementadas',colSpan=2),
                    ]),

                    html.Tr([
                        html.Td(0),
                        html.Td(f'NO documento o matriz para hacer monitoreo y seguimiento a las innovaciones implementadas'),
                        
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio