from assets.libraries import *
from assets.commons import *
from assets.cards import *
from assets.criteria import *

dash.register_page(__name__, path='/stats')

par_spacer='1rem'
progress_thickness='.8rem'

tarjeta_resumen_2021 = dbc.Card(
    [
        
        dbc.CardBody(
            [
                
                html.H3(children='Posición 2021: ', className="card-title me-2",style={'display':'inline-block'}),
                html.H3(id='posicion_2021',children='', className="card-title",style={'display':'inline-block','font-weight':'bold'}),

                
                
                html.Div(
                    [
                        html.P(children='Total: ', className="card-title me-2",style={'display':'inline-block','font-weight':'bold'}),
                        dbc.Progress(id='st',value=0,label='',style={"height": f"{progress_thickness}"},color="success"),
                        html.Br()
                    ],
                    className="card-text",
                    style={'line-height':f'{par_spacer}'}
                ),

                html.Div(
                    [
                        html.P(children='C1: ', className="card-title me-2",style={'display':'inline-block','font-weight':'bold'}),
                        dbc.Progress(id='sc1',value=0,label='',style={"height": f"{progress_thickness}"}),
                        html.Br()
                    ],
                    className="card-text",
                    style={'line-height':f'{par_spacer}'}
                ),

                html.Div(
                    [
                        html.P(children='C2: ', className="card-title me-2",style={'display':'inline-block','font-weight':'bold'}),
                        dbc.Progress(id='sc2',value=0,label='',style={"height": f"{progress_thickness}"}),
                        html.Br()
                    ],
                    className="card-text",
                    style={'line-height':f'{par_spacer}'}
                ),

                html.Div(
                    [
                        html.P(children='C3: ', className="card-title me-2",style={'display':'inline-block','font-weight':'bold'}),
                        dbc.Progress(id='sc3',value=0,label='',style={"height": f"{progress_thickness}"}),
                        html.Br()
                    ],
                    className="card-text",
                    style={'line-height':f'{par_spacer}'}
                ),

                html.Div(
                    [
                        html.P(children='C4: ', className="card-title me-2",style={'display':'inline-block','font-weight':'bold'}),
                        dbc.Progress(id='sc4',value=0,label='',style={"height": f"{progress_thickness}"}),
                        html.Br()
                    ],
                    className="card-text",
                    style={'line-height':f'{par_spacer}'}
                ),
            ]
        ),
    ],
)

tarjeta_resumen_2023 = dbc.Card(
    [
        
        dbc.CardBody(
            [
                
                html.H3(children='Posición 2023: ', className="card-title me-2",style={'display':'inline-block'}),
                html.H3(id='posicion_2023',children='', className="card-title",style={'display':'inline-block','font-weight':'bold'}),

                
                
                html.Div(
                    [
                        html.P(children='Total: ', className="card-title me-2",style={'display':'inline-block','font-weight':'bold'}),
                        dbc.Progress(id='st_2023',value=0,label='',style={"height": f"{progress_thickness}"},color="success"),
                        html.Br()
                    ],
                    className="card-text",
                    style={'line-height':f'{par_spacer}'}
                ),

                html.Div(
                    [
                        html.P(children='C1: ', className="card-title me-2",style={'display':'inline-block','font-weight':'bold'}),
                        dbc.Progress(id='sc1_2023',value=0,label='',style={"height": f"{progress_thickness}"}),
                        html.Br()
                    ],
                    className="card-text",
                    style={'line-height':f'{par_spacer}'}
                ),

                html.Div(
                    [
                        html.P(children='C2: ', className="card-title me-2",style={'display':'inline-block','font-weight':'bold'}),
                        dbc.Progress(id='sc2_2023',value=0,label='',style={"height": f"{progress_thickness}"}),
                        html.Br()
                    ],
                    className="card-text",
                    style={'line-height':f'{par_spacer}'}
                ),

                html.Div(
                    [
                        html.P(children='C3: ', className="card-title me-2",style={'display':'inline-block','font-weight':'bold'}),
                        dbc.Progress(id='sc3_2023',value=0,label='',style={"height": f"{progress_thickness}"}),
                        html.Br()
                    ],
                    className="card-text",
                    style={'line-height':f'{par_spacer}'}
                ),

                html.Div(
                    [
                        html.P(children='C4: ', className="card-title me-2",style={'display':'inline-block','font-weight':'bold'}),
                        dbc.Progress(id='sc4_2023',value=0,label='',style={"height": f"{progress_thickness}"}),
                        html.Br()
                    ],
                    className="card-text",
                    style={'line-height':f'{par_spacer}'}
                ),
            ]
        ),
    ],
)

tarjeta_total_2023 = dbc.Card(
    [
        
        dbc.CardBody(
            [
                
                html.H3(children='Total IIP 2023: ', className="card-title me-2",style={'display':'inline-block'}),
                html.H3(id='posicion_total',children='', className="card-title",style={'display':'inline-block','font-weight':'bold'}),

                
                
                html.Div(
                    [
                        html.P(children='Total: ', className="card-title me-2",style={'display':'inline-block','font-weight':'bold'}),
                        dbc.Progress(id='stotal',value=0,label='',style={"height": f"{progress_thickness}"},color="success"),
                        html.Br()
                    ],
                    className="card-text",
                    style={'line-height':f'{par_spacer}'}
                ),

                html.Div(
                    [
                        html.P(children='C1: ', className="card-title me-2",style={'display':'inline-block','font-weight':'bold'}),
                        dbc.Progress(id='sc1total',value=0,label='',style={"height": f"{progress_thickness}"}),
                        html.Br()
                    ],
                    className="card-text",
                    style={'line-height':f'{par_spacer}'}
                ),

                html.Div(
                    [
                        html.P(children='C2: ', className="card-title me-2",style={'display':'inline-block','font-weight':'bold'}),
                        dbc.Progress(id='sc2total',value=0,label='',style={"height": f"{progress_thickness}"}),
                        html.Br()
                    ],
                    className="card-text",
                    style={'line-height':f'{par_spacer}'}
                ),

                html.Div(
                    [
                        html.P(children='C3: ', className="card-title me-2",style={'display':'inline-block','font-weight':'bold'}),
                        dbc.Progress(id='sc3total',value=0,label='',style={"height": f"{progress_thickness}"}),
                        html.Br()
                    ],
                    className="card-text",
                    style={'line-height':f'{par_spacer}'}
                ),

                html.Div(
                    [
                        html.P(children='C4: ', className="card-title me-2",style={'display':'inline-block','font-weight':'bold'}),
                        dbc.Progress(id='sc4total',value=0,label='',style={"height": f"{progress_thickness}"}),
                        html.Br()
                    ],
                    className="card-text",
                    style={'line-height':f'{par_spacer}'}
                ),
            ]
        ),
    ],
)

selector_pregunta = dcc.Dropdown(
    id="selector_pregunta",
    options=[{'label': x, 'value': x} for x in PREGUNTAS_TODAS],
    placeholder='Seleccione la pregunta a analizar',
    value=PREGUNTA_INICIAL
)

selector_iniciativa = dcc.Dropdown(
    id="selector_iniciativa",
    options=[],
    placeholder='',
    value=''
)

selector_criterio_entidad = dcc.Dropdown(
    id="selector_criterio_entidad",
    options=[],
    placeholder='',
    value=''
)

selector_criterio_bucle = dcc.Dropdown(
    id="selector_criterio_bucle",
    options=[],
    placeholder='',
    value=''
)

zona_velas = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H3(children='Diagrama de velas: ', className="card-title me-2"),
                html.Br(),
                dcc.Graph(id='candlesticks')
            ]
        ),
    ],
)

zona_de_peligro = dbc.Card(
    [
        dbc.CardBody(children=
            [
                html.H3(children='Zona del peligro: ', className="card-title me-2"),
                html.Br(),
                html.H5(children='Selector de iniciativa: ', className="card-title me-2"),
                selector_iniciativa,
                html.Br(),
                html.H5(children='Selector de criterio entidad: ', className="card-title me-2"),
                selector_criterio_entidad,
                html.Br(),
                html.H5(children='Selector de criterio bucle: ', className="card-title me-2"),
                selector_criterio_bucle,
                html.Br(),
                html.H5(children='Entrada de nota: ', className="card-title me-2"),
                html.Br(),
                dbc.Input(id='entrada_nota', value=1.6, placeholder="Ingrese la nota: ", type="number"),
                html.Br(),
                html.Div(id='empty'),
                dbc.Button(id='enviar_nota',children='Enviar nota a excel', style={'width':'100%'}),
            ]
            ),
    ],
)

zona_de_notas = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H3(children='Zona del notas: ', className="card-title me-2"),
                html.Br(),
                html.Div(id='tabla_criterios'),
            ]
        ),
    ],
)

zona_descarga = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Button("Exportar respuestas 2023", id="btn_download_respuestas_2023", style={'width':'100%'}),
                dcc.Download(id="download_respuestas_2023"),
                html.Br(),
                html.Br(),
                dbc.Button("Exportar resultados 2023", id="btn_download_resultados_2023", style={'width':'100%'}),
                dcc.Download(id="download_resultados_2023"),
                html.Br(),
                html.Br(),
                dbc.Button("Exportar repeats", id="btn_download_repeats", style={'width':'100%'}),
                dcc.Download(id="download_repeats"),
            ]
        ),
    ],
)

###############################################################################################################################################################################################################
# LAYOUT    
###############################################################################################################################################################################################################

layout = dbc.Container([

    #FILA 1
    dbc.Row([
        
        dcc.Store(id='pregunta_seleccionada',storage_type='memory'),
        dcc.Store(id='iniciativa_seleccionada',storage_type='memory'),
        dcc.Store(id='criterio_seleccionado_entidad',storage_type='memory'),
        dcc.Store(id='criterio_seleccionado_bucle',storage_type='memory'),
        dcc.Store(id='criterios_disponibles_bucle',storage_type='memory'),
        dcc.Store(id='nota',storage_type='memory'),

        #Nombre entidad seleccionada
        dbc.Col([
            html.H1(children=[],id='nom_ent',style={'font-weight':'bold'}),
            html.Br(),
            ],
            width=9,
        ),

        #Selector pregunta
        dbc.Col([
            selector_pregunta
            ],
            width=3,
        )
        ],
        justify="between",
        
    ),

    #FILA 2
    dbc.Row([

        #Mision, visión, pregunta, respuesta, criterio, respuesta 2021 y respuesta 2023
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.H3('Mision'),
                        html.P(id='mision',children=[])
                    ],                        
                    style={'padding':f'0rem 2rem 0rem 0rem','text-justify':'auto','text-align': 'justify'}
                    ),
                ]),
                dbc.Col([
                    html.Div([
                        html.H3('Vision'),
                        html.P(id='vision',children=[])
                    ],
                    style={'text-justify':'auto','text-align': 'justify'}
                    ),
                ]),
            ]),

            html.Br(),
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.H3('Pregunta'),
                        html.P(id='pregunta',children=[]),
                    ],                        
                    style={'padding':f'0rem 2rem 0rem 0rem','text-justify':'auto','text-align': 'justify'}
                    ),
                ]),

                dbc.Col([
                    html.Div([
                        html.H3('Respuesta 2021'),
                        html.P(id='respuesta_2021',children=[]),

                        html.H5('Nota obtenida en 2021: ', className="card-title me-2",style={'display':'inline-block'}),
                        html.H5(id='nota_obtenida_2021',children=20, className="card-title me-2",style={'display':'inline-block','font-weight':'bold'}),
                        html.Br(),
                        html.H5('Nota máxima en 2021: ', className="card-title me-2",style={'display':'inline-block'}),
                        html.H5(id='nota_max_2021',children=20, className="card-title me-2",style={'display':'inline-block','font-weight':'bold'}),
                    ],
                    style={'text-justify':'auto','text-align': 'justify'}
                    ),
                ]),
            ]),

            html.Br(),
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.H3('Criterio de evaluación'),
                        html.Div(id='criterio',children=[]),
                    ],
                    style={'text-justify':'auto','text-align': 'justify'}
                    ),
                ]),
            ]),

            html.Br(),
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.H3(f'Respuesta 2023'),
                        html.Div(id='respuesta_2023',children='',),
                    ]),
                ]),
            ]),
        ],
        width=9,
        style={'padding':f'0rem 1.5rem 0rem 0rem'}
        ),
            
        #Tarjeta resumen 2021, zona de peligro, zona de descarga
        dbc.Col([
            tarjeta_resumen_2021,
            html.Br(),
            tarjeta_resumen_2023,
            html.Br(),
            tarjeta_total_2023,
            html.Br(),
            zona_de_peligro,
            html.Br(),
            zona_de_notas,
            html.Br(),
            zona_velas,
            html.Br(),
            zona_descarga

        ],
        width=3
        )

    ],
    justify="end",
    ),
])

###############################################################################################################################################################################################################
# CALLBACKS
###############################################################################################################################################################################################################

#Callback nombre, misión y visión
@dash.callback(
    Output('nom_ent', 'children'),
    Output('mision', 'children'),
    Output('vision', 'children'),
    Input('entidad_seleccionada', 'data')
)
def mision_vision_entidad_f(value):

    nom_ent= respuestas_2023_df[respuestas_2023_df['_uuid'] == value]['entidad']
    
    mis = respuestas_2023_df[respuestas_2023_df['_uuid'] == value]['mision']
    vis = respuestas_2023_df[respuestas_2023_df['_uuid'] == value]['vision']

    if mis.empty ==False:
        mis_ent=mis
    else:
        mis_ent = 'N/A'

    if vis.empty ==False:
        vis_ent=vis
    else:
        vis_ent = 'N/A'

    return nom_ent,mis_ent,vis_ent

#Callback resumen 2021 lateral
@dash.callback(
    Output('posicion_2021', 'children'),
    Output('st', 'label'),
    Output('sc1', 'label'),
    Output('sc2', 'label'),
    Output('sc3', 'label'),
    Output('sc4', 'label'),
    Output('st', 'value'),
    Output('sc1', 'value'),
    Output('sc2', 'value'),
    Output('sc3', 'value'),
    Output('sc4', 'value'),
    Input('entidad_seleccionada', 'data')
)
def tabla_resumen_2021(entidad):
    
    pos = resultados_2021_df[resultados_2021_df['_uuid'] == entidad]['pos']
    if pos.empty == False:
        pos_2021 = pos
    else:
        pos_2021 = 'N/A'

    total = resultados_2021_df[resultados_2021_df['_uuid'] == entidad]['total'].round(2)
    if total.empty == False:
        res_total  = total
        st = total
    else:
        res_total = 'N/A'
        st = 0

    c1 = resultados_2021_df[resultados_2021_df['_uuid'] == entidad]['res_c1'].round(2)
    if c1.empty == False:
        res_c1 = c1
        sc1 = c1
    else:
        res_c1 = 'N/A'
        sc1 = 0

    c2 = resultados_2021_df[resultados_2021_df['_uuid'] == entidad]['res_c2'].round(2)
    if c2.empty == False:
        res_c2 = c2
        sc2 = c2
    else:
        res_c2 = 'N/A'
        sc2 = 0

    c3 = resultados_2021_df[resultados_2021_df['_uuid'] == entidad]['res_c3'].round(2)
    if c3.empty == False:
        res_c3 = c3
        sc3 = c3
    else:
        res_c3 = 'N/A'
        sc3 = 0

    c4 = resultados_2021_df[resultados_2021_df['_uuid'] == entidad]['res_c4'].round(2)
    if c4.empty == False:
        res_c4 = c4
        sc4 = c4
    else:
        res_c4 = 'N/A'
        sc4 = 0

    return pos_2021,res_total,res_c1,res_c2,res_c3,res_c4,st,sc1,sc2,sc3,sc4

#Callback resumen 2023 lateral
@dash.callback(
    Output('posicion_2023', 'children'),
    Output('st_2023', 'label'),
    Output('sc1_2023', 'label'),
    Output('sc2_2023', 'label'),
    Output('sc3_2023', 'label'),
    Output('sc4_2023', 'label'),
    Output('st_2023', 'value'),
    Output('sc1_2023', 'value'),
    Output('sc2_2023', 'value'),
    Output('sc3_2023', 'value'),
    Output('sc4_2023', 'value'),
    Input('entidad_seleccionada', 'data'),
    Input('pregunta_seleccionada', 'data'),
    Input('iniciativa_seleccionada', 'data'),
    Input('criterio_seleccionado_entidad', 'data'),
    Input('criterio_seleccionado_bucle', 'data'),
)
def tabla_resumen_2023(entidad,pregunta,iniciativa,criterio_entidad,criterio_bucle):
    
    pos = resultados_2023_df[resultados_2023_df['_uuid'] == entidad]['pos']
    if pos.empty == False:
        pos_2021 = pos
    else:
        pos_2021 = 'N/A'

    total = resultados_2023_df[resultados_2023_df['_uuid'] == entidad]['total'].round(2)
    if total.empty == False:
        res_total  = total
        st = total
    else:
        res_total = 'N/A'
        st = 0

    c1 = resultados_2023_df[resultados_2023_df['_uuid'] == entidad]['res_c1'].round(2)
    if c1.empty == False:
        res_c1 = c1
        sc1 = c1
    else:
        res_c1 = 'N/A'
        sc1 = 0

    c2 = resultados_2023_df[resultados_2023_df['_uuid'] == entidad]['res_c2'].round(2)
    if c2.empty == False:
        res_c2 = c2
        sc2 = c2
    else:
        res_c2 = 'N/A'
        sc2 = 0

    c3 = resultados_2023_df[resultados_2023_df['_uuid'] == entidad]['res_c3'].round(2)
    if c3.empty == False:
        res_c3 = c3
        sc3 = c3
    else:
        res_c3 = 'N/A'
        sc3 = 0

    c4 = resultados_2023_df[resultados_2023_df['_uuid'] == entidad]['res_c4'].round(2)
    if c4.empty == False:
        res_c4 = c4
        sc4 = c4
    else:
        res_c4 = 'N/A'
        sc4 = 0

    return pos_2021,res_total,res_c1,res_c2,res_c3,res_c4,st,sc1,sc2,sc3,sc4

#Callback resumen iip lateral
@dash.callback(
    Output('posicion_total', 'children'),
    Output('stotal', 'label'),
    Output('sc1total', 'label'),
    Output('sc2total', 'label'),
    Output('sc3total', 'label'),
    Output('sc4total', 'label'),
    Output('stotal', 'value'),
    Output('sc1total', 'value'),
    Output('sc2total', 'value'),
    Output('sc3total', 'value'),
    Output('sc4total', 'value'),
    Input('entidad_seleccionada', 'data'),
    Input('pregunta_seleccionada', 'data'),
    Input('iniciativa_seleccionada', 'data'),
    Input('criterio_seleccionado_entidad', 'data'),
    Input('criterio_seleccionado_bucle', 'data'),
)
def tabla_resumen_total(entidad,pregunta,iniciativa,criterio_entidad,criterio_bucle):
    

        total = round(resultados_2023_df.loc[:,'total'].mean(),2)

        c1 = round(resultados_2023_df.loc[:,'res_c1'].mean(),2)

        c2 = round(resultados_2023_df.loc[:,'res_c2'].mean(),2)

        c3 = round(resultados_2023_df.loc[:,'res_c3'].mean(),2)

        c4 = round(resultados_2023_df.loc[:,'res_c4'].mean(),2)

        pos_2021 = total

        res_total = total
        st = total

        res_c1 = c1
        sc1 = c1

        res_c2 = c2
        sc2 = c2

        res_c3 = c3
        sc3 = c3

        res_c4 = c4
        sc4 = c4

        return pos_2021,res_total,res_c1,res_c2,res_c3,res_c4,st,sc1,sc2,sc3,sc4

#Callback velas
@dash.callback(
    Output('candlesticks', 'figure'),
    Input('pregunta_seleccionada', 'data'),
)
def diagrama_velas(pregunta_seleccionada):
    
    x_axis = ['2021','2023']
    outliers_top = []
    mean_top = []
    mean_bottom = []
    outliers_bottom = []

    try:
        outliers_top_2021 = resultados_2021_df[pregunta_seleccionada].max()
        mean_top_2021 = resultados_2021_df[pregunta_seleccionada].median() + resultados_2021_df[pregunta_seleccionada].std()
        mean_bottom_2021 = resultados_2021_df[pregunta_seleccionada].median() - resultados_2021_df[pregunta_seleccionada].std()
        outliers_bottom_2021 = resultados_2021_df[pregunta_seleccionada].min()
    except:
        outliers_top_2021 = 0
        mean_top_2021 = 0
        mean_bottom_2021 = 0
        outliers_bottom_2021 = 0
    
    #"""
    
    if pregunta_seleccionada=='p1':

        outliers_top_2023 = p1_df['nota_iniciativa'].max()
        mean_top_2023 = p1_df['nota_iniciativa'].median() + p1_df['nota_iniciativa'].std()
        mean_bottom_2023 = p1_df['nota_iniciativa'].median() - p1_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p1_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p2':

        outliers_top_2023 = p2_df['nota_iniciativa'].max()
        mean_top_2023 = p2_df['nota_iniciativa'].median() + p2_df['nota_iniciativa'].std()
        mean_bottom_2023 = p2_df['nota_iniciativa'].median() - p2_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p2_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p3':

        outliers_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].max()
        mean_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() + respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        mean_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() - respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        outliers_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].min()

    if pregunta_seleccionada=='p4':

        outliers_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].max()
        mean_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() + respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        mean_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() - respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        outliers_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].min()

    if pregunta_seleccionada=='p5':

        outliers_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].max()
        mean_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() + respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        mean_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() - respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        outliers_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].min()

    if pregunta_seleccionada=='p6':

        outliers_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].max()
        mean_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() + respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        mean_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() - respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        outliers_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].min()

    if pregunta_seleccionada=='p7':

        outliers_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].max()
        mean_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() + respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        mean_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() - respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        outliers_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].min()

    if pregunta_seleccionada=='p8':

        outliers_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].max()
        mean_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() + respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        mean_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() - respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        outliers_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].min()

    if pregunta_seleccionada=='p9':

        outliers_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].max()
        mean_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() + respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        mean_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() - respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        outliers_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].min()

    if pregunta_seleccionada=='p10':

        outliers_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].max()
        mean_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() + respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        mean_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() - respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        outliers_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].min()

    if pregunta_seleccionada=='p11':

        outliers_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].max()
        mean_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() + respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        mean_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() - respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        outliers_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].min()

    if pregunta_seleccionada=='p12':

        outliers_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].max()
        mean_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() + respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        mean_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() - respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        outliers_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].min()

    if pregunta_seleccionada=='p13':

        outliers_top_2023 = p13_df['nota_iniciativa'].max()
        mean_top_2023 = p13_df['nota_iniciativa'].median() + p13_df['nota_iniciativa'].std()
        mean_bottom_2023 = p13_df['nota_iniciativa'].median() - p13_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p13_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p14':

        outliers_top_2023 = p14_df['nota_iniciativa'].max()
        mean_top_2023 = p14_df['nota_iniciativa'].median() + p14_df['nota_iniciativa'].std()
        mean_bottom_2023 = p14_df['nota_iniciativa'].median() - p14_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p14_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p15':

        outliers_top_2023 = p15_df['nota_iniciativa'].max()
        mean_top_2023 = p15_df['nota_iniciativa'].median() + p15_df['nota_iniciativa'].std()
        mean_bottom_2023 = p15_df['nota_iniciativa'].median() - p15_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p15_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p16':

        outliers_top_2023 = p16_df['nota_iniciativa'].max()
        mean_top_2023 = p16_df['nota_iniciativa'].median() + p16_df['nota_iniciativa'].std()
        mean_bottom_2023 = p16_df['nota_iniciativa'].median() - p16_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p16_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p17':

        outliers_top_2023 = p17_df['nota_iniciativa'].max()
        mean_top_2023 = p17_df['nota_iniciativa'].median() + p17_df['nota_iniciativa'].std()
        mean_bottom_2023 = p17_df['nota_iniciativa'].median() - p17_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p17_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p18':

        outliers_top_2023 = p18_df['nota_iniciativa'].max()
        mean_top_2023 = p18_df['nota_iniciativa'].median() + p18_df['nota_iniciativa'].std()
        mean_bottom_2023 = p18_df['nota_iniciativa'].median() - p18_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p18_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p19':

        outliers_top_2023 = p19_df['nota_iniciativa'].max()
        mean_top_2023 = p19_df['nota_iniciativa'].median() + p19_df['nota_iniciativa'].std()
        mean_bottom_2023 = p19_df['nota_iniciativa'].median() - p19_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p19_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p20':

        outliers_top_2023 = p20_df['nota_iniciativa'].max()
        mean_top_2023 = p20_df['nota_iniciativa'].median() + p20_df['nota_iniciativa'].std()
        mean_bottom_2023 = p20_df['nota_iniciativa'].median() - p20_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p20_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p21':

        outliers_top_2023 = p21_df['nota_iniciativa'].max()
        mean_top_2023 = p21_df['nota_iniciativa'].median() + p21_df['nota_iniciativa'].std()
        mean_bottom_2023 = p21_df['nota_iniciativa'].median() - p21_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p21_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p22':

        outliers_top_2023 = p22_df['nota_iniciativa'].max()
        mean_top_2023 = p22_df['nota_iniciativa'].median() + p22_df['nota_iniciativa'].std()
        mean_bottom_2023 = p22_df['nota_iniciativa'].median() - p22_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p22_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p23':

        outliers_top_2023 = p23_df['nota_iniciativa'].max()
        mean_top_2023 = p23_df['nota_iniciativa'].median() + p23_df['nota_iniciativa'].std()
        mean_bottom_2023 = p23_df['nota_iniciativa'].median() - p23_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p23_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p24':

        outliers_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].max()
        mean_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() + respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        mean_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() - respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        outliers_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].min()

    if pregunta_seleccionada=='p25':

        outliers_top_2023 = p25_df['nota_iniciativa'].max()
        mean_top_2023 = p25_df['nota_iniciativa'].median() + p25_df['nota_iniciativa'].std()
        mean_bottom_2023 = p25_df['nota_iniciativa'].median() - p25_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p25_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p26':

        outliers_top_2023 = p26_df['nota_iniciativa'].max()
        mean_top_2023 = p26_df['nota_iniciativa'].median() + p26_df['nota_iniciativa'].std()
        mean_bottom_2023 = p26_df['nota_iniciativa'].median() - p26_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p26_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p27':

        outliers_top_2023 = p27_df['nota_iniciativa'].max()
        mean_top_2023 = p27_df['nota_iniciativa'].median() + p27_df['nota_iniciativa'].std()
        mean_bottom_2023 = p27_df['nota_iniciativa'].median() - p27_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p27_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p28':

        outliers_top_2023 = p28_df['nota_iniciativa'].max()
        mean_top_2023 = p28_df['nota_iniciativa'].median() + p28_df['nota_iniciativa'].std()
        mean_bottom_2023 = p28_df['nota_iniciativa'].median() - p28_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p28_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p29':

        outliers_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].max()
        mean_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() + respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        mean_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() - respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        outliers_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].min()

    if pregunta_seleccionada=='p30':

        outliers_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].max()
        mean_top_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() + respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        mean_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].median() - respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].std()
        outliers_bottom_2023 = respuestas_2023_df[f'{pregunta_seleccionada}_nota_pregunta'].min()

    if pregunta_seleccionada=='p31':

        outliers_top_2023 = p31_df['nota_iniciativa'].max()
        mean_top_2023 = p31_df['nota_iniciativa'].median() + p31_df['nota_iniciativa'].std()
        mean_bottom_2023 = p31_df['nota_iniciativa'].median() - p31_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p31_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p32':

        outliers_top_2023 = p32_df['nota_iniciativa'].max()
        mean_top_2023 = p32_df['nota_iniciativa'].median() + p32_df['nota_iniciativa'].std()
        mean_bottom_2023 = p32_df['nota_iniciativa'].median() - p32_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p32_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p33':

        outliers_top_2023 = p33_df['nota_iniciativa'].max()
        mean_top_2023 = p33_df['nota_iniciativa'].median() + p33_df['nota_iniciativa'].std()
        mean_bottom_2023 = p33_df['nota_iniciativa'].median() - p33_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p33_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p34':

        outliers_top_2023 = p34_df['nota_iniciativa'].max()
        mean_top_2023 = p34_df['nota_iniciativa'].median() + p34_df['nota_iniciativa'].std()
        mean_bottom_2023 = p34_df['nota_iniciativa'].median() - p34_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p34_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p35':

        outliers_top_2023 = p35_df['nota_iniciativa'].max()
        mean_top_2023 = p35_df['nota_iniciativa'].median() + p35_df['nota_iniciativa'].std()
        mean_bottom_2023 = p35_df['nota_iniciativa'].median() - p35_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p35_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p36':

        outliers_top_2023 = p36_df['nota_iniciativa'].max()
        mean_top_2023 = p36_df['nota_iniciativa'].median() + p36_df['nota_iniciativa'].std()
        mean_bottom_2023 = p36_df['nota_iniciativa'].median() - p36_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p36_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p37':

        outliers_top_2023 = p37_df['nota_iniciativa'].max()
        mean_top_2023 = p37_df['nota_iniciativa'].median() + p37_df['nota_iniciativa'].std()
        mean_bottom_2023 = p37_df['nota_iniciativa'].median() - p37_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p37_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p38':

        outliers_top_2023 = p38_df['nota_iniciativa'].max()
        mean_top_2023 = p38_df['nota_iniciativa'].median() + p38_df['nota_iniciativa'].std()
        mean_bottom_2023 = p38_df['nota_iniciativa'].median() - p38_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p38_df['nota_iniciativa'].min()

    if pregunta_seleccionada=='p39':

        outliers_top_2023 = p39_df['nota_iniciativa'].max()
        mean_top_2023 = p39_df['nota_iniciativa'].median() + p39_df['nota_iniciativa'].std()
        mean_bottom_2023 = p39_df['nota_iniciativa'].median() - p39_df['nota_iniciativa'].std()
        outliers_bottom_2023 = p39_df['nota_iniciativa'].min()

    #""" 
    #El problema son las "notas de las iniciativas"
    #Arreglar cuando cambiemos columnas


    """
    outliers_top_2023=outliers_top_2021
    mean_top_2023=mean_top_2021
    mean_bottom_2023=mean_bottom_2021
    outliers_bottom_2023=outliers_bottom_2021
    #"""

    outliers_top.append(outliers_top_2021)
    outliers_top.append(outliers_top_2023)

    mean_top.append(mean_top_2021)
    mean_top.append(mean_top_2023)

    mean_bottom.append(mean_bottom_2021)
    mean_bottom.append(mean_bottom_2023)

    outliers_bottom.append(outliers_bottom_2021)
    outliers_bottom.append(outliers_bottom_2023)


    fig = go.Figure(data=[
        go.Candlestick(
            x=x_axis,
            high=outliers_top,
            open=mean_top,
            close=mean_bottom,
            low=outliers_bottom,
            )
        ],
        ).update_layout(margin={"t":0,"b":0,"l":0,"r":0},xaxis_rangeslider_visible=False)

    return fig

#Callback guardar pregunta seleccionada
@dash.callback(
    Output('pregunta_seleccionada', 'data'),
    Input('selector_pregunta', 'value')
)
def seleccion_pregunta(value):
    if value != None:
        salida=value
    else:
        salida = preguntas_df[preguntas_df["codigo 2023"] == "p1"]["codigo 2023"].tolist()[0]
    return salida

#Callback guardar iniciativa seleccionada
@dash.callback(
    Output('iniciativa_seleccionada', 'data'),
    Input('selector_iniciativa', 'value')
)
def seleccion_iniciativa(value):
    return value

#Callback guardar criterio entidad seleccionado
@dash.callback(
    Output('criterio_seleccionado_entidad', 'data'),
    Input('selector_criterio_entidad', 'value'),
)
def seleccion_criterio_entidad(entidad):
    return entidad

#Callback guardar criterio bucle seleccionado
@dash.callback(
    Output('criterio_seleccionado_bucle', 'data'),
    Output('criterios_disponibles_bucle', 'data'),
    Input('selector_criterio_bucle', 'value'),
    Input('selector_criterio_bucle', 'options'),
)
def seleccion_criterio_bucle(bucle,opciones_bucle):
    return bucle,opciones_bucle

#Callback para llamar valor de nota
@dash.callback(
    Output('nota', 'data'),
    Input('entrada_nota', 'value'),
)
def llamar_numero(valor):
    return valor

#Callback llamar notas
@dash.callback(
    Output('tabla_criterios', 'children'),

    Input('entidad_seleccionada', 'data'),
    Input('pregunta_seleccionada', 'data'),
    Input('iniciativa_seleccionada', 'data'),
    Input('criterio_seleccionado_entidad', 'data'),
    Input('criterio_seleccionado_bucle', 'data'),
)
def tabla_criterios(entidad_seleccionada,pregunta_seleccionada,iniciativa_seleccionada,criterio_seleccionado_entidad,criterio_seleccionado_bucle):
    tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'N/A'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td('N/A'),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )
    
    if pregunta_seleccionada=='p1':
        pass

    elif pregunta_seleccionada=='p2':
        crits=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada]['c3'])
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                        html.Th(f'c3',colSpan=3),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'],2),rowSpan=2),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'],2),rowSpan=2),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c3'],2),colSpan=3),
                    ],
                    ),
                    html.Tr([
                        html.Td(p2_df.loc[p2_df['_index']==iniciativa_seleccionada,crits[0]]),
                        html.Td(p2_df.loc[p2_df['_index']==iniciativa_seleccionada,crits[1]]),
                        html.Td(p2_df.loc[p2_df['_index']==iniciativa_seleccionada,crits[2]]),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )

    elif pregunta_seleccionada=='p3':
        pass

    elif pregunta_seleccionada=='p4':
        crits=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'],2)),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'],2)),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )

    elif pregunta_seleccionada=='p5':
        pass
        
    elif pregunta_seleccionada=='p6':
        crits=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'],2)),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'],2)),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )

    elif pregunta_seleccionada=='p7':
        pass

    elif pregunta_seleccionada=='p8':
        crits=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'],2)),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'],2)),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )

    elif pregunta_seleccionada=='p9':
        pass

    elif pregunta_seleccionada=='p10':
        pass

    elif pregunta_seleccionada=='p11':
        crits=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'],2)),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'],2)),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )

    elif pregunta_seleccionada=='p12':
        pass

    elif pregunta_seleccionada=='p13':
        crits=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada]['c2'])
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2',colSpan=3),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'],2),rowSpan=2),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'],2),colSpan=3),
                    ],
                    ),
                    html.Tr([
                        html.Td(p13_df.loc[p13_df['_index']==iniciativa_seleccionada,crits[0]]),
                        html.Td(p13_df.loc[p13_df['_index']==iniciativa_seleccionada,crits[1]]),
                        html.Td(p13_df.loc[p13_df['_index']==iniciativa_seleccionada,crits[2]]),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )

    elif pregunta_seleccionada=='p14':
        crits=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada]['c1'])
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1',colSpan=3),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'],2),colSpan=3),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'],2),rowSpan=2),
                    ],
                    ),
                    html.Tr([
                        html.Td(p14_df.loc[p14_df['_index']==iniciativa_seleccionada,crits[0]]),
                        html.Td(p14_df.loc[p14_df['_index']==iniciativa_seleccionada,crits[1]]),
                        html.Td(p14_df.loc[p14_df['_index']==iniciativa_seleccionada,crits[2]]),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )

    elif pregunta_seleccionada=='p15':
        crits=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada]['c1'])
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1',colSpan=3),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'],2),colSpan=3),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'],2),rowSpan=2),
                    ],
                    ),
                    html.Tr([
                        html.Td(p15_df.loc[p15_df['_index']==iniciativa_seleccionada,crits[0]]),
                        html.Td(p15_df.loc[p15_df['_index']==iniciativa_seleccionada,crits[1]]),
                        html.Td(p15_df.loc[p15_df['_index']==iniciativa_seleccionada,crits[2]]),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )

    elif pregunta_seleccionada=='p16':
        crits=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada]['c1'])
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1',colSpan=3),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'],2),colSpan=3),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'],2),rowSpan=2),
                    ],
                    ),
                    html.Tr([
                        html.Td(p16_df.loc[p16_df['_index']==iniciativa_seleccionada,crits[0]]),
                        html.Td(p16_df.loc[p16_df['_index']==iniciativa_seleccionada,crits[1]]),
                        html.Td(p16_df.loc[p16_df['_index']==iniciativa_seleccionada,crits[2]]),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )

    elif pregunta_seleccionada=='p17':
        crits=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada]['c1'])
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'],2)),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'],2),rowSpan=2),
                    ],
                    ),
                    html.Tr([
                        html.Td(p17_df.loc[p17_df['_index']==iniciativa_seleccionada,crits[0]]),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )

    elif pregunta_seleccionada=='p18':
        crits=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada]['c1'])
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'],2)),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'],2),rowSpan=2),
                    ],
                    ),
                    html.Tr([
                        html.Td(p18_df.loc[p18_df['_index']==iniciativa_seleccionada,crits[0]]),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )

    elif pregunta_seleccionada=='p19':
        crits=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada]['c1'])
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1',colSpan=3),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'],2),colSpan=3),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'],2),rowSpan=2),
                    ],
                    ),
                    html.Tr([
                        html.Td(p19_df.loc[p19_df['_index']==iniciativa_seleccionada,crits[0]]),
                        html.Td(p19_df.loc[p19_df['_index']==iniciativa_seleccionada,crits[1]]),
                        html.Td(p19_df.loc[p19_df['_index']==iniciativa_seleccionada,crits[2]]),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )

    elif pregunta_seleccionada=='p20':
        crits=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada]['c1'])
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1',colSpan=3),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'],2),colSpan=3),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'],2),rowSpan=2),
                    ],
                    ),
                    html.Tr([
                        html.Td(p20_df.loc[p20_df['_index']==iniciativa_seleccionada,crits[0]]),
                        html.Td(p20_df.loc[p20_df['_index']==iniciativa_seleccionada,crits[1]]),
                        html.Td(p20_df.loc[p20_df['_index']==iniciativa_seleccionada,crits[2]]),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )

    elif pregunta_seleccionada=='p21':
        crits=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada]['c1'])
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'],2)),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'],2),rowSpan=2),
                    ],
                    ),
                    html.Tr([
                        html.Td(p21_df.loc[p21_df['_index']==iniciativa_seleccionada,crits[0]]),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )

    elif pregunta_seleccionada=='p22':
        crits=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada]['c1'])
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'],2)),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'],2),rowSpan=2),
                    ],
                    ),
                    html.Tr([
                        html.Td(p22_df.loc[p22_df['_index']==iniciativa_seleccionada,crits[0]]),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )

    elif pregunta_seleccionada=='p23':
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                        html.Th(f'c3'),
                        html.Th(f'c4'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'],2)),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'],2)),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c3'],2)),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c4'],2)),
                        
                    ],
                    ),
                    html.Tr([
                        html.Td(p23_df.loc[p23_df['_index']==iniciativa_seleccionada,'c1']),
                        html.Td(p23_df.loc[p23_df['_index']==iniciativa_seleccionada,'c2']),
                        html.Td(p23_df.loc[p23_df['_index']==iniciativa_seleccionada,'c3']),
                        html.Td(p23_df.loc[p23_df['_index']==iniciativa_seleccionada,'c4']),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )

    elif pregunta_seleccionada=='p24':
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                        html.Th(f'c3'),
                        html.Th(f'c4'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'],2)),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'],2)),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c3'],2)),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c4'],2)),
                        
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )

    elif pregunta_seleccionada=='p25':
        crits=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada]['c1'])
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1',colSpan=3),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'],2),colSpan=3),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'],2),rowSpan=2),
                        
                    ],
                    ),
                    html.Tr([
                        html.Td(p25_df.loc[p25_df['_index']==iniciativa_seleccionada,crits[0]]),
                        html.Td(p25_df.loc[p25_df['_index']==iniciativa_seleccionada,crits[1]]),
                        html.Td(p25_df.loc[p25_df['_index']==iniciativa_seleccionada,crits[2]]),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )

    elif pregunta_seleccionada=='p26':
        crits=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada]['c1'])
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1',colSpan=3),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'],2),colSpan=3),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'],2),rowSpan=2),
                        
                    ],
                    ),
                    html.Tr([
                        html.Td(p26_df.loc[p26_df['_index']==iniciativa_seleccionada,crits[0]]),
                        html.Td(p26_df.loc[p26_df['_index']==iniciativa_seleccionada,crits[1]]),
                        html.Td(p26_df.loc[p26_df['_index']==iniciativa_seleccionada,crits[2]]),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )

    elif pregunta_seleccionada=='p27':
        crits=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada]['c1'])
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'],2)),
                        
                    ],
                    ),
                    html.Tr([
                        html.Td(p27_df.loc[p27_df['_index']==iniciativa_seleccionada,crits[0]]),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )

    elif pregunta_seleccionada=='p28':
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                        html.Th(f'c3'),
                        html.Th(f'c4'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(p23_df.loc[p23_df['_index']==iniciativa_seleccionada,'c1']),
                        html.Td(p23_df.loc[p23_df['_index']==iniciativa_seleccionada,'c2']),
                        html.Td(p23_df.loc[p23_df['_index']==iniciativa_seleccionada,'c3']),
                        html.Td(p23_df.loc[p23_df['_index']==iniciativa_seleccionada,'c4']),
                    ],
                    ),
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
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                        html.Th(f'c3'),
                        html.Th(f'c4',colSpan=4),
                        html.Th(f'c5'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'],2),rowSpan=2),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'],2),rowSpan=2),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c3'],2),rowSpan=2),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c4'],2),colSpan=4),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c5'],2)),
                    ],
                    ),
                    html.Tr([
                        html.Td(p28_df.loc[p28_df['_index']==iniciativa_seleccionada,'c1']),
                        html.Td(p28_df.loc[p28_df['_index']==iniciativa_seleccionada,'c2']),
                        html.Td(p28_df.loc[p28_df['_index']==iniciativa_seleccionada,'c3']),
                        html.Td(p28_df.loc[p28_df['_index']==iniciativa_seleccionada,'c4']),
                        html.Td(p28_df.loc[p28_df['_index']==iniciativa_seleccionada,'c5']),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),


        ],
        style={'width':'100%'}
        )

    elif pregunta_seleccionada=='p29':
        crits=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada])
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'],2)),
                        
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )

    elif pregunta_seleccionada=='p30':
        crits=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada])
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'],2)),
                        
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )

    elif pregunta_seleccionada=='p31':
        pass

    elif pregunta_seleccionada=='p32':
        crits=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada]['c2'])
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'],2),rowSpan=2),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'],2)),
                        
                    ],
                    ),
                    html.Tr([
                        html.Td(p32_df.loc[p32_df['_index']==iniciativa_seleccionada,crits[0]]),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )

    elif pregunta_seleccionada=='p33':
        crits=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada]['c2'])
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'],2),rowSpan=2),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'],2)),
                        
                    ],
                    ),
                    html.Tr([
                        html.Td(p33_df.loc[p33_df['_index']==iniciativa_seleccionada,crits[0]]),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )

    elif pregunta_seleccionada=='p34':
        crits=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada]['c2'])
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'],2),rowSpan=2),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'],2)),
                        
                    ],
                    ),
                    html.Tr([
                        html.Td(p34_df.loc[p34_df['_index']==iniciativa_seleccionada,crits[0]]),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )

    elif pregunta_seleccionada=='p35':
        crits=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada]['c2'])
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'],2),rowSpan=2),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'],2)),
                        
                    ],
                    ),
                    html.Tr([
                        html.Td(p35_df.loc[p35_df['_index']==iniciativa_seleccionada,crits[0]]),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )

    elif pregunta_seleccionada=='p36':
        crits=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada]['c2'])
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'],2),rowSpan=2),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'],2)),
                        
                    ],
                    ),
                    html.Tr([
                        html.Td(p36_df.loc[p36_df['_index']==iniciativa_seleccionada,crits[0]]),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )

    elif pregunta_seleccionada=='p37':
        crits=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada]['c2'])
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'],2),rowSpan=2),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'],2)),
                        
                    ],
                    ),
                    html.Tr([
                        html.Td(p37_df.loc[p37_df['_index']==iniciativa_seleccionada,crits[0]]),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )

    elif pregunta_seleccionada=='p38':
        crits=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada]['c2'])
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'],2),rowSpan=2),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'],2)),
                        
                    ],
                    ),
                    html.Tr([
                        html.Td(p38_df.loc[p38_df['_index']==iniciativa_seleccionada,crits[0]]),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )

    elif pregunta_seleccionada=='p39':
        crits=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada]['c2'])
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'],2),rowSpan=2),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'],2)),
                        
                    ],
                    ),
                    html.Tr([
                        html.Td(p39_df.loc[p39_df['_index']==iniciativa_seleccionada,crits[0]]),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )

    else:
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'N/A'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td('N/A'),
                    ],
                    ),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,                               
            ),
        ],
        style={'width':'100%'}
        )
    
    return tabla_criterios

#Callback enviar criterios bucle
@dash.callback(
    Output('selector_criterio_bucle', 'options'),
    Output('selector_criterio_bucle', 'value'),

    Input('criterio_seleccionado_entidad', 'data'),
    State('pregunta_seleccionada', 'data'),
)
def enviar_criterios_bucle(criterio_seleccionado,pregunta_seleccionada):
    salida_criterios_bucle=[]
    salida_criterios_bucle_seleccionado='N/A'
    unwanted=['l1','l2','l3','l4']
    
    #Acuerdos y/o actos administrativos
    if pregunta_seleccionada=='p1':
        pass
        
    #Enfoques, lineas o proyectos
    elif pregunta_seleccionada=='p2':
        if criterio_seleccionado=='c3':
            salida_criterios_bucle_full=CRITS_PREGUNTAS_BASE[pregunta_seleccionada][criterio_seleccionado]
            salida_criterios_bucle = [item for item in salida_criterios_bucle_full if item not in unwanted]
            
            try:
                salida_criterios_bucle_seleccionado=salida_criterios_bucle[0]
            except:
                salida_criterios_bucle_seleccionado='N/A'

        else:
            salida_criterios_bucle=[]
            salida_criterios_bucle_seleccionado='N/A'

    #Presupuesto general
    elif pregunta_seleccionada=='p3':
        pass
        
    #Presupuesto general innovación
    elif pregunta_seleccionada=='p4':
        pass
        
    #Presupuesto inversión general
    elif pregunta_seleccionada=='p5':
        pass
        
    #Presupuesto inversión innovación
    elif pregunta_seleccionada=='p6':
        pass
        
    #Funcionarios total
    elif pregunta_seleccionada=='p7':
        pass
        
    #Funcionarios manual en innovación 
    elif pregunta_seleccionada=='p8':
        pass
        
    #Funcionarios ocasionales
    elif pregunta_seleccionada=='p9':
        pass
        
    #Contratistas total
    elif pregunta_seleccionada=='p10':
        pass
        
    #Contratistas en innovación 
    elif pregunta_seleccionada=='p11':
        pass
        
    #Contratistas ocasionales
    elif pregunta_seleccionada=='p12':
        pass
        
    # Recursos digitales
    elif pregunta_seleccionada=='p13':
        if criterio_seleccionado=='c2':
            salida_criterios_bucle_full=CRITS_PREGUNTAS_BASE[pregunta_seleccionada][criterio_seleccionado]
            salida_criterios_bucle = [item for item in salida_criterios_bucle_full if item not in unwanted]

            try:
                salida_criterios_bucle_seleccionado=salida_criterios_bucle[0]
            except:
                salida_criterios_bucle_seleccionado='N/A'

        else:
            salida_criterios_bucle=[]
            salida_criterios_bucle_seleccionado='N/A'
        
    #retos SDQS
    elif pregunta_seleccionada=='p14':
        if criterio_seleccionado=='c1':
            salida_criterios_bucle_full=CRITS_PREGUNTAS_BASE[pregunta_seleccionada][criterio_seleccionado]
            salida_criterios_bucle = [item for item in salida_criterios_bucle_full if item not in unwanted]

            try:
                salida_criterios_bucle_seleccionado=salida_criterios_bucle[0]
            except:
                salida_criterios_bucle_seleccionado='N/A'

        else:
            salida_criterios_bucle=[]
            salida_criterios_bucle_seleccionado='N/A'
        
    #retos otros para ciudadanos
    elif pregunta_seleccionada=='p15':
        if criterio_seleccionado=='c1':
            salida_criterios_bucle_full=CRITS_PREGUNTAS_BASE[pregunta_seleccionada][criterio_seleccionado]
            salida_criterios_bucle = [item for item in salida_criterios_bucle_full if item not in unwanted]

            try:
                salida_criterios_bucle_seleccionado=salida_criterios_bucle[0]
            except:
                salida_criterios_bucle_seleccionado='N/A'

        else:
            salida_criterios_bucle=[]
            salida_criterios_bucle_seleccionado='N/A'
        
    #retos por funcionarios/contratistas
    elif pregunta_seleccionada=='p16':
        if criterio_seleccionado=='c1':
            salida_criterios_bucle_full=CRITS_PREGUNTAS_BASE[pregunta_seleccionada][criterio_seleccionado]
            salida_criterios_bucle = [item for item in salida_criterios_bucle_full if item not in unwanted]

            try:
                salida_criterios_bucle_seleccionado=salida_criterios_bucle[0]
            except:
                salida_criterios_bucle_seleccionado='N/A'

        else:
            salida_criterios_bucle=[]
            salida_criterios_bucle_seleccionado='N/A'

    #canales retos
    elif pregunta_seleccionada=='p17':
        if criterio_seleccionado=='c1':
            salida_criterios_bucle_full=CRITS_PREGUNTAS_BASE[pregunta_seleccionada][criterio_seleccionado]
            salida_criterios_bucle = [item for item in salida_criterios_bucle_full if item not in unwanted]

            try:
                salida_criterios_bucle_seleccionado=salida_criterios_bucle[0]
            except:
                salida_criterios_bucle_seleccionado='N/A'

        else:
            salida_criterios_bucle=[]
            salida_criterios_bucle_seleccionado='N/A'
        
    #actividades retos
    elif pregunta_seleccionada=='p18':
        if criterio_seleccionado=='c1':
            salida_criterios_bucle_full=CRITS_PREGUNTAS_BASE[pregunta_seleccionada][criterio_seleccionado]
            salida_criterios_bucle = [item for item in salida_criterios_bucle_full if item not in unwanted]

            try:
                salida_criterios_bucle_seleccionado=salida_criterios_bucle[0]
            except:
                salida_criterios_bucle_seleccionado='N/A'


        else:
            salida_criterios_bucle=[]
            salida_criterios_bucle_seleccionado='N/A'
        
    #ideas ciudadanos
    elif pregunta_seleccionada=='p19':
        if criterio_seleccionado=='c1':
            salida_criterios_bucle_full=CRITS_PREGUNTAS_BASE[pregunta_seleccionada][criterio_seleccionado]
            salida_criterios_bucle = [item for item in salida_criterios_bucle_full if item not in unwanted]

            try:
                salida_criterios_bucle_seleccionado=salida_criterios_bucle[0]
            except:
                salida_criterios_bucle_seleccionado='N/A'

        else:
            salida_criterios_bucle=[]
            salida_criterios_bucle_seleccionado='N/A'
        
    #ideas funcionarios
    elif pregunta_seleccionada=='p20':
        if criterio_seleccionado=='c1':
            salida_criterios_bucle_full=CRITS_PREGUNTAS_BASE[pregunta_seleccionada][criterio_seleccionado]
            salida_criterios_bucle = [item for item in salida_criterios_bucle_full if item not in unwanted]

            try:
                salida_criterios_bucle_seleccionado=salida_criterios_bucle[0]
            except:
                salida_criterios_bucle_seleccionado='N/A'

        else:
            salida_criterios_bucle=[]
            salida_criterios_bucle_seleccionado='N/A'
        
    #canales ideas
    elif pregunta_seleccionada=='p21':
        if criterio_seleccionado=='c1':
            salida_criterios_bucle_full=CRITS_PREGUNTAS_BASE[pregunta_seleccionada][criterio_seleccionado]
            salida_criterios_bucle = [item for item in salida_criterios_bucle_full if item not in unwanted]

            try:
                salida_criterios_bucle_seleccionado=salida_criterios_bucle[0]
            except:
                salida_criterios_bucle_seleccionado='N/A'

        else:
            salida_criterios_bucle=[]
            salida_criterios_bucle_seleccionado='N/A'
        
    #actividades ideas
    elif pregunta_seleccionada=='p22':
        if criterio_seleccionado=='c1':
            salida_criterios_bucle_full=CRITS_PREGUNTAS_BASE[pregunta_seleccionada][criterio_seleccionado]
            salida_criterios_bucle = [item for item in salida_criterios_bucle_full if item not in unwanted]

            try:
                salida_criterios_bucle_seleccionado=salida_criterios_bucle[0]
            except:
                salida_criterios_bucle_seleccionado='N/A'

        else:
            salida_criterios_bucle=[]
            salida_criterios_bucle_seleccionado='N/A'
        
    #innovaciones diseñadas
    elif pregunta_seleccionada=='p23':
        if criterio_seleccionado=='c1':
            salida_criterios_bucle_full=CRITS_PREGUNTAS_BASE[pregunta_seleccionada][criterio_seleccionado]
            salida_criterios_bucle = [item for item in salida_criterios_bucle_full if item not in unwanted]

            try:
                salida_criterios_bucle_seleccionado=salida_criterios_bucle[0]
            except:
                salida_criterios_bucle_seleccionado='N/A'

        elif criterio_seleccionado=='c2':
            salida_criterios_bucle_full=CRITS_PREGUNTAS_BASE[pregunta_seleccionada][criterio_seleccionado]
            salida_criterios_bucle = [item for item in salida_criterios_bucle_full if item not in unwanted]

            try:
                salida_criterios_bucle_seleccionado=salida_criterios_bucle[0]
            except:
                salida_criterios_bucle_seleccionado='N/A'

        elif criterio_seleccionado=='c3':
            salida_criterios_bucle_full=CRITS_PREGUNTAS_BASE[pregunta_seleccionada][criterio_seleccionado]
            salida_criterios_bucle = [item for item in salida_criterios_bucle_full if item not in unwanted]

            try:
                salida_criterios_bucle_seleccionado=salida_criterios_bucle[0]
            except:
                salida_criterios_bucle_seleccionado='N/A'

        elif criterio_seleccionado=='c4':
            salida_criterios_bucle_full=CRITS_PREGUNTAS_BASE[pregunta_seleccionada][criterio_seleccionado]
            salida_criterios_bucle = [item for item in salida_criterios_bucle_full if item not in unwanted]

            try:
                salida_criterios_bucle_seleccionado=salida_criterios_bucle[0]
            except:
                salida_criterios_bucle_seleccionado='N/A'

        else:
            salida_criterios_bucle=[]
            salida_criterios_bucle_seleccionado='N/A'

    #innovaciones diseñadas
    elif pregunta_seleccionada=='p24':
        if criterio_seleccionado=='p24_1':
            salida_criterios_bucle_full=CRITS_PREGUNTAS_BASE[pregunta_seleccionada][criterio_seleccionado]
            salida_criterios_bucle = [item for item in salida_criterios_bucle_full if item not in unwanted]

            try:
                salida_criterios_bucle_seleccionado=salida_criterios_bucle[0]
            except:
                salida_criterios_bucle_seleccionado='N/A'

        elif criterio_seleccionado=='p24_2':
            salida_criterios_bucle_full=CRITS_PREGUNTAS_BASE[pregunta_seleccionada][criterio_seleccionado]
            salida_criterios_bucle = [item for item in salida_criterios_bucle_full if item not in unwanted]

            try:
                salida_criterios_bucle_seleccionado=salida_criterios_bucle[0]
            except:
                salida_criterios_bucle_seleccionado='N/A'

        elif criterio_seleccionado=='p24_3':
            salida_criterios_bucle_full=CRITS_PREGUNTAS_BASE[pregunta_seleccionada][criterio_seleccionado]
            salida_criterios_bucle = [item for item in salida_criterios_bucle_full if item not in unwanted]
            try:
                salida_criterios_bucle_seleccionado=salida_criterios_bucle[0]
            except:
                salida_criterios_bucle_seleccionado='N/A'

        elif criterio_seleccionado=='p24_4':
            salida_criterios_bucle_full=CRITS_PREGUNTAS_BASE[pregunta_seleccionada][criterio_seleccionado]
            salida_criterios_bucle = [item for item in salida_criterios_bucle_full if item not in unwanted]

            try:
                salida_criterios_bucle_seleccionado=salida_criterios_bucle[0]
            except:
                salida_criterios_bucle_seleccionado='N/A'

        else:
            salida_criterios_bucle=[]
            salida_criterios_bucle_seleccionado='N/A'

    #promoción de una cultura de innovación
    elif pregunta_seleccionada=='p25':
        if criterio_seleccionado=='c1':
            salida_criterios_bucle_full=CRITS_PREGUNTAS_BASE[pregunta_seleccionada][criterio_seleccionado]
            salida_criterios_bucle = [item for item in salida_criterios_bucle_full if item not in unwanted]

            try:
                salida_criterios_bucle_seleccionado=salida_criterios_bucle[0]
            except:
                salida_criterios_bucle_seleccionado='N/A'

        else:
            salida_criterios_bucle=[]
            salida_criterios_bucle_seleccionado='N/A'
        
    #espacios de experimentación
    elif pregunta_seleccionada=='p26':
        if criterio_seleccionado=='c1':
            salida_criterios_bucle_full=CRITS_PREGUNTAS_BASE[pregunta_seleccionada][criterio_seleccionado]
            salida_criterios_bucle = [item for item in salida_criterios_bucle_full if item not in unwanted]

            try:
                salida_criterios_bucle_seleccionado=salida_criterios_bucle[0]
            except:
                salida_criterios_bucle_seleccionado='N/A'

        else:
            salida_criterios_bucle=[]
            salida_criterios_bucle_seleccionado='N/A'
        
    #unidades de innovación
    elif pregunta_seleccionada=='p27':
        if criterio_seleccionado=='c1':
            salida_criterios_bucle_full=CRITS_PREGUNTAS_BASE[pregunta_seleccionada][criterio_seleccionado]
            salida_criterios_bucle = [item for item in salida_criterios_bucle_full if item not in unwanted]

            try:
                salida_criterios_bucle_seleccionado=salida_criterios_bucle[0]
            except:
                salida_criterios_bucle_seleccionado='N/A'

        else:
            salida_criterios_bucle=[]
            salida_criterios_bucle_seleccionado='N/A'
        
    #implementación de innovaciones
    elif pregunta_seleccionada=='p28':

        if criterio_seleccionado=='c4':
            salida_criterios_bucle_full=CRITS_PREGUNTAS_BASE[pregunta_seleccionada][criterio_seleccionado]
            salida_criterios_bucle = [item for item in salida_criterios_bucle_full if item not in unwanted]

            try:
                salida_criterios_bucle_seleccionado=salida_criterios_bucle[0]
            except:
                salida_criterios_bucle_seleccionado='N/A'

        elif criterio_seleccionado=='c5':
            salida_criterios_bucle_full=CRITS_PREGUNTAS_BASE[pregunta_seleccionada][criterio_seleccionado]
            salida_criterios_bucle = [item for item in salida_criterios_bucle_full if item not in unwanted]

            try:
                salida_criterios_bucle_seleccionado=salida_criterios_bucle[0]
            except:
                salida_criterios_bucle_seleccionado='N/A'

        else:
            salida_criterios_bucle=[]
            salida_criterios_bucle_seleccionado='N/A'

    #funcionarios formados
    elif pregunta_seleccionada=='p29':
        pass
        
    #contratistas formados
    elif pregunta_seleccionada=='p30':
        pass
        
    #acuerdos o actos en gestión del conocimiento
    elif pregunta_seleccionada=='p31':
        pass
        
    #proyectos o lineas en gestión del conocimiento
    elif pregunta_seleccionada=='p32':
        if criterio_seleccionado=='c2':
            salida_criterios_bucle_full=CRITS_PREGUNTAS_BASE[pregunta_seleccionada][criterio_seleccionado]
            salida_criterios_bucle = [item for item in salida_criterios_bucle_full if item not in unwanted]

            try:
                salida_criterios_bucle_seleccionado=salida_criterios_bucle[0]
            except:
                salida_criterios_bucle_seleccionado='N/A'

        else:
            salida_criterios_bucle=[]
            salida_criterios_bucle_seleccionado='N/A'
        
    #sistematización de retos ciudadanos
    elif pregunta_seleccionada=='p33':
        if criterio_seleccionado=='c2':
            salida_criterios_bucle_full=CRITS_PREGUNTAS_BASE[pregunta_seleccionada][criterio_seleccionado]
            salida_criterios_bucle = [item for item in salida_criterios_bucle_full if item not in unwanted]

            try:
                salida_criterios_bucle_seleccionado=salida_criterios_bucle[0]
            except:
                salida_criterios_bucle_seleccionado='N/A'

        else:
            salida_criterios_bucle=[]
            salida_criterios_bucle_seleccionado='N/A'
        
    #sistematización de retos de funcionarios contratistas
    elif pregunta_seleccionada=='p34':
        if criterio_seleccionado=='c2':
            salida_criterios_bucle_full=CRITS_PREGUNTAS_BASE[pregunta_seleccionada][criterio_seleccionado]
            salida_criterios_bucle = [item for item in salida_criterios_bucle_full if item not in unwanted]

            try:
                salida_criterios_bucle_seleccionado=salida_criterios_bucle[0]
            except:
                salida_criterios_bucle_seleccionado='N/A'

        else:
            salida_criterios_bucle=[]
            salida_criterios_bucle_seleccionado='N/A'
        
    #sistematización ideas de ciudadanos
    elif pregunta_seleccionada=='p35':
        if criterio_seleccionado=='c2':
            salida_criterios_bucle_full=CRITS_PREGUNTAS_BASE[pregunta_seleccionada][criterio_seleccionado]
            salida_criterios_bucle = [item for item in salida_criterios_bucle_full if item not in unwanted]

            try:
                salida_criterios_bucle_seleccionado=salida_criterios_bucle[0]
            except:
                salida_criterios_bucle_seleccionado='N/A'

        else:
            salida_criterios_bucle=[]
            salida_criterios_bucle_seleccionado='N/A'
        
    #sistematización ideas de funcionarios contratistas
    elif pregunta_seleccionada=='p36':
        if criterio_seleccionado=='c2':
            salida_criterios_bucle_full=CRITS_PREGUNTAS_BASE[pregunta_seleccionada][criterio_seleccionado]
            salida_criterios_bucle = [item for item in salida_criterios_bucle_full if item not in unwanted]

            try:
                salida_criterios_bucle_seleccionado=salida_criterios_bucle[0]
            except:
                salida_criterios_bucle_seleccionado='N/A'

        else:
            salida_criterios_bucle=[]
            salida_criterios_bucle_seleccionado='N/A'
        
    #buenas prácticas y lecciones aprendidas en innovación
    elif pregunta_seleccionada=='p37':
        if criterio_seleccionado=='c2':
            salida_criterios_bucle_full=CRITS_PREGUNTAS_BASE[pregunta_seleccionada][criterio_seleccionado]
            salida_criterios_bucle = [item for item in salida_criterios_bucle_full if item not in unwanted]

            try:
                salida_criterios_bucle_seleccionado=salida_criterios_bucle[0]
            except:
                salida_criterios_bucle_seleccionado='N/A'

        else:
            salida_criterios_bucle=[]
            salida_criterios_bucle_seleccionado='N/A'
        
    #buenas prácticas y lecciones aprendidas generales
    elif pregunta_seleccionada=='p38':
        if criterio_seleccionado=='c2':
            salida_criterios_bucle_full=CRITS_PREGUNTAS_BASE[pregunta_seleccionada][criterio_seleccionado]
            salida_criterios_bucle = [item for item in salida_criterios_bucle_full if item not in unwanted]

            try:
                salida_criterios_bucle_seleccionado=salida_criterios_bucle[0]
            except:
                salida_criterios_bucle_seleccionado='N/A'

        else:
            salida_criterios_bucle=[]
            salida_criterios_bucle_seleccionado='N/A'
        
    #Monitoreo y seguimiento a innovaciones
    elif pregunta_seleccionada=='p39':
        if criterio_seleccionado=='c2':
            salida_criterios_bucle_full=CRITS_PREGUNTAS_BASE[pregunta_seleccionada][criterio_seleccionado]
            salida_criterios_bucle = [item for item in salida_criterios_bucle_full if item not in unwanted]

            try:
                salida_criterios_bucle_seleccionado=salida_criterios_bucle[0]
            except:
                salida_criterios_bucle_seleccionado='N/A'

        else:
            salida_criterios_bucle=[]
            salida_criterios_bucle_seleccionado='N/A'
        
    #Cualquier caso no definido
    else:
        salida_criterios_bucle=[]
        salida_criterios_bucle_seleccionado='N/A'
    
    return salida_criterios_bucle,salida_criterios_bucle_seleccionado

#Callback calificar iniciativa seleccionada
@dash.callback(
    Output('empty', 'children'),

    Input('enviar_nota', 'n_clicks'),

    State('entidad_seleccionada', 'data'),
    State('pregunta_seleccionada', 'data'),
    State('iniciativa_seleccionada', 'data'),
    State('criterio_seleccionado_entidad', 'data'),
    State('criterio_seleccionado_bucle', 'data'),
    State('criterios_disponibles_bucle', 'data'),
    State('nota', 'data'),
)
def calificacion_iniciativa(clicks,entidad_seleccionada,pregunta_seleccionada,iniciativa_seleccionada,criterio_seleccionado,criterio_seleccionado_bucle,criterios_disponibles_bucle,nota):
    
    if clicks is not None:

        #Acuerdos y/o actos administrativos
        if pregunta_seleccionada=='p1':
            pass

        #Enfoques, lineas o proyectos
        elif pregunta_seleccionada=='p2':
            
            if criterio_seleccionado=='c1':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota
                respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            
            
            elif criterio_seleccionado=='c2':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota
                respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            
            
            elif criterio_seleccionado=='c3':
                
                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p2_df.loc[p2_df['_index']==iniciativa_seleccionada, criterio_seleccionado_bucle]=nota

                #CALCULO PROMEDIO INICIATIVA
                p2_df['l1']= p2_df[criterios_disponibles_bucle].mean(axis=1)
                p2_df.to_excel(f'./files/separadas/repeat_p2.xlsx',index=False)

                nota_entidad = round(p2_df.loc[p2_df['_submission__uuid']==entidad_seleccionada]['l1'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota_entidad

            else:
                pass

            p2_df['nota_iniciativa']=p2_df['l1']
            p2_df.to_excel(f'./files/separadas/repeat_p2.xlsx',index=False)
        
            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c3'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta
            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        #Presupuesto general
        elif pregunta_seleccionada=='p3':

            pass

        #Presupuesto general innovación
        elif pregunta_seleccionada=='p4':
            
            if criterio_seleccionado=='c1':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota

            elif criterio_seleccionado=='c2':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota
                
            else:
                pass

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        #Presupuesto inversión general
        elif pregunta_seleccionada=='p5':
            
            pass

        #Presupuesto inversión innovación
        elif pregunta_seleccionada=='p6':
            
            if criterio_seleccionado=='c1':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota

            elif criterio_seleccionado=='c2':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota
                
            else:
                pass

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        #Funcionarios total
        elif pregunta_seleccionada=='p7':

            pass

        #Funcionarios manual en innovación 
        elif pregunta_seleccionada=='p8':

            if criterio_seleccionado=='c1':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota

            elif criterio_seleccionado=='c2':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota
                
            else:
                pass

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)
            
        #Funcionarios ocasionales
        elif pregunta_seleccionada=='p9':

            pass

        #Contratistas total
        elif pregunta_seleccionada=='p10':

            pass

        #Contratistas en innovación 
        elif pregunta_seleccionada=='p11':

            if criterio_seleccionado=='c1':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota

            elif criterio_seleccionado=='c2':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota
                
            else:
                pass

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        #Contratistas ocasionales
        elif pregunta_seleccionada=='p12':

            pass

        # Recursos digitales
        elif pregunta_seleccionada=='p13':
            
            if criterio_seleccionado=='c1':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota
                respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
           
            elif criterio_seleccionado=='c2':
                
                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p13_df.loc[p13_df['_index']==iniciativa_seleccionada, criterio_seleccionado_bucle]=nota

                #CALCULO PROMEDIO INICIATIVA
                p13_df['l1'] = p13_df[criterios_disponibles_bucle].sum(axis=1)
                p13_df.to_excel(f'./files/separadas/repeat_p13.xlsx',index=False)

                nota_entidad = p13_df.loc[p13_df['_submission__uuid']==entidad_seleccionada]['l1'].mean()
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota_entidad

            else:
                pass

            p13_df['nota_iniciativa']=p13_df['l1']
            p13_df.to_excel(f'./files/separadas/repeat_p13.xlsx',index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta
            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        #retos SDQS
        elif pregunta_seleccionada=='p14':

            if criterio_seleccionado=='c1':

                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p14_df.loc[p14_df['_index']==iniciativa_seleccionada, criterio_seleccionado_bucle]=nota

                #CALCULO PROMEDIO INICIATIVA
                p14_df['l1']= p14_df[criterios_disponibles_bucle].sum(axis=1)
                p14_df.to_excel(f'./files/separadas/repeat_p14.xlsx',index=False)

                nota_entidad = round(p14_df.loc[p14_df['_submission__uuid']==entidad_seleccionada]['l1'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota_entidad

            elif criterio_seleccionado=='c2':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota

            else:
                pass

            p14_df['nota_iniciativa']=p14_df['l1']
            p14_df.to_excel(f'./files/separadas/repeat_p14.xlsx',index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta
            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        #retos otros para ciudadanos
        elif pregunta_seleccionada=='p15':

            if criterio_seleccionado=='c1':

                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p15_df.loc[p15_df['_index']==iniciativa_seleccionada, criterio_seleccionado_bucle]=nota

                #CALCULO PROMEDIO INICIATIVA
                p15_df['l1']= p15_df[criterios_disponibles_bucle].sum(axis=1)
                p15_df.to_excel(f'./files/separadas/repeat_p15.xlsx',index=False)
        
                nota_entidad = round(p15_df.loc[p15_df['_submission__uuid']==entidad_seleccionada]['l1'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota_entidad

            elif criterio_seleccionado=='c2':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota
                
            else:
                pass

            p15_df['nota_iniciativa']=p15_df['l1']
            p15_df.to_excel(f'./files/separadas/repeat_p15.xlsx',index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        #retos por funcionarios/contratistas
        elif pregunta_seleccionada=='p16':

            if criterio_seleccionado=='c1':

                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p16_df.loc[p16_df['_index']==iniciativa_seleccionada, criterio_seleccionado_bucle]=nota

                #CALCULO PROMEDIO INICIATIVA
                p16_df['l1']= p16_df[criterios_disponibles_bucle].sum(axis=1)
                p16_df.to_excel(f'./files/separadas/repeat_p16.xlsx',index=False)
        
                nota_entidad = round(p16_df.loc[p16_df['_submission__uuid']==entidad_seleccionada]['l1'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota_entidad

            elif criterio_seleccionado=='c2':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota
                
            else:
                pass

            p16_df['nota_iniciativa']=p16_df['l1']
            p16_df.to_excel(f'./files/separadas/repeat_p16.xlsx',index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        #canales retos
        elif pregunta_seleccionada=='p17':

            if criterio_seleccionado=='c1':

                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p17_df.loc[p17_df['_index']==iniciativa_seleccionada, criterio_seleccionado_bucle]=nota

                #CALCULO PROMEDIO INICIATIVA
                p17_df['l1']= p17_df[criterios_disponibles_bucle].sum(axis=1)
                p17_df.to_excel(f'./files/separadas/repeat_p17.xlsx',index=False)
        
                nota_entidad = round(p17_df.loc[p17_df['_submission__uuid']==entidad_seleccionada]['l1'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota_entidad

            elif criterio_seleccionado=='c2':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota
                
            else:
                pass

            p17_df['nota_iniciativa']=p17_df['l1']
            p17_df.to_excel(f'./files/separadas/repeat_p17.xlsx',index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        #actividades retos
        elif pregunta_seleccionada=='p18':

            if criterio_seleccionado=='c1':

                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p18_df.loc[p18_df['_index']==iniciativa_seleccionada, criterio_seleccionado_bucle]=nota

                #CALCULO PROMEDIO INICIATIVA
                p18_df['l1']= p18_df[criterios_disponibles_bucle].sum(axis=1)
                p18_df.to_excel(f'./files/separadas/repeat_p18.xlsx',index=False)
        
                nota_entidad = round(p18_df.loc[p18_df['_submission__uuid']==entidad_seleccionada]['l1'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota_entidad

            elif criterio_seleccionado=='c2':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota
                
            else:
                pass

            p18_df['nota_iniciativa']=p18_df['l1']
            p18_df.to_excel(f'./files/separadas/repeat_p18.xlsx',index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        #ideas ciudadanos
        elif pregunta_seleccionada=='p19':

            if criterio_seleccionado=='c1':

                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p19_df.loc[p19_df['_index']==iniciativa_seleccionada, criterio_seleccionado_bucle]=nota

                #CALCULO PROMEDIO INICIATIVA
                p19_df['l1']= p19_df[criterios_disponibles_bucle].sum(axis=1)
                p19_df.to_excel(f'./files/separadas/repeat_p19.xlsx',index=False)
        
                nota_entidad = round(p19_df.loc[p19_df['_submission__uuid']==entidad_seleccionada]['l1'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota_entidad

            elif criterio_seleccionado=='c2':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota
                
            else:
                pass

            p19_df['nota_iniciativa']=p19_df['l1']
            p19_df.to_excel(f'./files/separadas/repeat_p19.xlsx',index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        #ideas funcionarios
        elif pregunta_seleccionada=='p20':

            if criterio_seleccionado=='c1':

                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p20_df.loc[p20_df['_index']==iniciativa_seleccionada, criterio_seleccionado_bucle]=nota

                #CALCULO PROMEDIO INICIATIVA
                p20_df['l1']= p20_df[criterios_disponibles_bucle].sum(axis=1)
                p20_df.to_excel(f'./files/separadas/repeat_p20.xlsx',index=False)
        
                nota_entidad = round(p20_df.loc[p20_df['_submission__uuid']==entidad_seleccionada]['l1'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota_entidad

            elif criterio_seleccionado=='c2':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota
                
            else:
                pass

            p20_df['nota_iniciativa']=p20_df['l1']
            p20_df.to_excel(f'./files/separadas/repeat_p20.xlsx',index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        #canales ideas
        elif pregunta_seleccionada=='p21':

            if criterio_seleccionado=='c1':

                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p21_df.loc[p21_df['_index']==iniciativa_seleccionada, criterio_seleccionado_bucle]=nota

                #CALCULO PROMEDIO INICIATIVA
                p21_df['l1']= p21_df[criterios_disponibles_bucle].sum(axis=1)
                p21_df.to_excel(f'./files/separadas/repeat_p21.xlsx',index=False)
        
                nota_entidad = round(p21_df.loc[p21_df['_submission__uuid']==entidad_seleccionada]['l1'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota_entidad

            elif criterio_seleccionado=='c2':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota
                
            else:
                pass

            p21_df['nota_iniciativa']=p21_df['l1']
            p21_df.to_excel(f'./files/separadas/repeat_p21.xlsx',index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        #actividades ideas
        elif pregunta_seleccionada=='p22':

            if criterio_seleccionado=='c1':

                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p22_df.loc[p22_df['_index']==iniciativa_seleccionada, criterio_seleccionado_bucle]=nota

                #CALCULO PROMEDIO INICIATIVA
                p22_df['l1']= p22_df[criterios_disponibles_bucle].sum(axis=1)
                p22_df.to_excel(f'./files/separadas/repeat_p22.xlsx',index=False)
        
                nota_entidad = round(p22_df.loc[p22_df['_submission__uuid']==entidad_seleccionada]['l1'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota_entidad

            elif criterio_seleccionado=='c2':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota
                
            else:
                pass

            p22_df['nota_iniciativa']=p22_df['l1']
            p22_df.to_excel(f'./files/separadas/repeat_p22.xlsx',index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        #innovaciones diseñadas
        elif pregunta_seleccionada=='p23':

            if criterio_seleccionado=='c1':

                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p23_df.loc[p23_df['_index']==iniciativa_seleccionada, criterio_seleccionado_bucle]=nota

                #CALCULO PROMEDIO INICIATIVA
                p23_df['l1']= p23_df[criterios_disponibles_bucle].mean(axis=1)
                p23_df.to_excel(f'./files/separadas/repeat_p23.xlsx',index=False)

                nota_entidad = round(p23_df.loc[p23_df['_submission__uuid']==entidad_seleccionada]['l1'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota_entidad
           
            elif criterio_seleccionado=='c2':

                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p23_df.loc[p23_df['_index']==iniciativa_seleccionada, criterio_seleccionado_bucle]=nota

                #CALCULO PROMEDIO INICIATIVA
                p23_df['l2']= p23_df[criterios_disponibles_bucle].sum(axis=1)
                p23_df.to_excel(f'./files/separadas/repeat_p23.xlsx',index=False)

                nota_entidad = round(p23_df.loc[p23_df['_submission__uuid']==entidad_seleccionada]['l2'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota_entidad

            elif criterio_seleccionado=='c3':

                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p23_df.loc[p23_df['_index']==iniciativa_seleccionada, criterio_seleccionado_bucle]=nota

                #CALCULO PROMEDIO INICIATIVA
                p23_df['l3']= p23_df[criterios_disponibles_bucle].mean(axis=1)
                p23_df.to_excel(f'./files/separadas/repeat_p23.xlsx',index=False)

                nota_entidad = round(p23_df.loc[p23_df['_submission__uuid']==entidad_seleccionada]['l3'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c3'] = nota_entidad

            elif criterio_seleccionado=='c4':

                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p23_df.loc[p23_df['_index']==iniciativa_seleccionada, criterio_seleccionado_bucle]=nota

                #CALCULO PROMEDIO INICIATIVA
                p23_df['l4']= p23_df[criterios_disponibles_bucle].mean(axis=1)
                p23_df.to_excel(f'./files/separadas/repeat_p23.xlsx',index=False)

                nota_entidad = round(p23_df.loc[p23_df['_submission__uuid']==entidad_seleccionada]['l4'].mean(),4)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c4'] = nota_entidad
            
            else:
                pass

            p23_df['nota_iniciativa']=p23_df['l1']+p23_df['l2']+p23_df['l3']+p23_df['l4']
            p23_df.to_excel(f'./files/separadas/repeat_p23.xlsx',index=False)
            
            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c4'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta
            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        #innovaciones diseñadas
        elif pregunta_seleccionada=='p24':

            if criterio_seleccionado=='c1':

                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota
           
            elif criterio_seleccionado=='c2':

                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota

            elif criterio_seleccionado=='c3':

                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota

            elif criterio_seleccionado=='c4':

                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota

            else:
                pass
            
            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c4'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta
            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        #promoción de una cultura de innovación
        elif pregunta_seleccionada=='p25':

            if criterio_seleccionado=='c1':

                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p25_df.loc[p25_df['_index']==iniciativa_seleccionada, criterio_seleccionado_bucle]=nota

                #CALCULO PROMEDIO INICIATIVA
                p25_df['l1']= p25_df[criterios_disponibles_bucle].mean(axis=1)
                p25_df.to_excel(f'./files/separadas/repeat_{pregunta_seleccionada}.xlsx',index=False)

                nota_entidad = round(p25_df.loc[p25_df['_submission__uuid']==entidad_seleccionada]['l1'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota_entidad

            elif criterio_seleccionado=='c2':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota

            else:
                pass

            p25_df['nota_iniciativa']=p25_df['l1']
            p25_df.to_excel(f'./files/separadas/repeat_p25.xlsx',index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        #espacios de experimentación
        elif pregunta_seleccionada=='p26':

            if criterio_seleccionado=='c1':

                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p26_df.loc[p26_df['_index']==iniciativa_seleccionada, criterio_seleccionado_bucle]=nota

                #CALCULO PROMEDIO INICIATIVA
                p26_df['l1']= p26_df[criterios_disponibles_bucle].mean(axis=1)
                p26_df.to_excel(f'./files/separadas/repeat_{pregunta_seleccionada}.xlsx',index=False)

                nota_entidad = round(p26_df.loc[p26_df['_submission__uuid']==entidad_seleccionada]['l1'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota_entidad

            elif criterio_seleccionado=='c2':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota
                
            else:
                pass

            p26_df['nota_iniciativa']=p26_df['l1']
            p26_df.to_excel(f'./files/separadas/repeat_p26.xlsx',index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        #unidades de innovación
        elif pregunta_seleccionada=='p27':

            if criterio_seleccionado=='c1':

                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p27_df.loc[p27_df['_index']==iniciativa_seleccionada, criterio_seleccionado_bucle]=nota

                #CALCULO PROMEDIO INICIATIVA
                p27_df['l1']= p27_df[criterios_disponibles_bucle].sum(axis=1)
                p27_df.to_excel(f'./files/separadas/repeat_{pregunta_seleccionada}.xlsx',index=False)

                nota_entidad = round(p27_df.loc[p27_df['_submission__uuid']==entidad_seleccionada]['l1'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota_entidad

            else:
                pass

            p27_df['nota_iniciativa']=p27_df['l1']
            p27_df.to_excel(f'./files/separadas/repeat_p27.xlsx',index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        #implementación de innovaciones
        elif pregunta_seleccionada=='p28':

            if criterio_seleccionado=='c1':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota
                respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)

            elif criterio_seleccionado=='c2':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota
                respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)

            elif criterio_seleccionado=='c3':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota
                respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)

            elif criterio_seleccionado=='c4':

                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p28_df.loc[p28_df['_index']==iniciativa_seleccionada, criterio_seleccionado_bucle]=nota

                #CALCULO PROMEDIO INICIATIVA
                p28_df['l1']= p28_df[criterios_disponibles_bucle].sum(axis=1)
                p28_df.to_excel(f'./files/separadas/repeat_p28.xlsx',index=False)

                nota_entidad = round(p28_df.loc[p28_df['_submission__uuid']==entidad_seleccionada]['l1'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota_entidad

            elif criterio_seleccionado=='c5':

                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p28_df.loc[p28_df['_index']==iniciativa_seleccionada, criterio_seleccionado_bucle]=nota

                #CALCULO PROMEDIO INICIATIVA
                p28_df['l2']= p28_df[criterios_disponibles_bucle].mean(axis=1)
                p28_df.to_excel(f'./files/separadas/repeat_p28.xlsx',index=False)

                nota_entidad = round(p28_df.loc[p28_df['_submission__uuid']==entidad_seleccionada]['l2'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota_entidad
            
            else:
                pass

            p28_df['nota_iniciativa']=p28_df['l1']+p28_df['l2']
            p28_df.to_excel(f'./files/separadas/repeat_p28.xlsx',index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c5'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta
            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        #funcionarios formados
        elif pregunta_seleccionada=='p29':

            if criterio_seleccionado=='c1':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota
                
            else:
                pass

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        #contratistas formados
        elif pregunta_seleccionada=='p30':

            if criterio_seleccionado=='c1':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota
                
            else:
                pass

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta

            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        #acuerdos o actos en gestión del conocimiento
        elif pregunta_seleccionada=='p31':

            pass

        #proyectos o lineas en gestión del conocimiento
        elif pregunta_seleccionada=='p32':

            if criterio_seleccionado=='c1':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota
                respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
           
            elif criterio_seleccionado=='c2':
                
                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p32_df.loc[p32_df['_index']==iniciativa_seleccionada, criterio_seleccionado_bucle]=nota

                #CALCULO PROMEDIO INICIATIVA
                p32_df['l1']= p32_df[criterios_disponibles_bucle].mean(axis=1)
                p32_df.to_excel(f'./files/separadas/repeat_p32.xlsx',index=False)

                nota_entidad = round(p32_df.loc[p32_df['_submission__uuid']==entidad_seleccionada]['l1'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota_entidad
            
            else:
                pass

            p32_df['nota_iniciativa'] = p32_df['l1']
            p32_df.to_excel(f'./files/separadas/repeat_p32.xlsx',index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta
            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        #sistematización de retos ciudadanos
        elif pregunta_seleccionada=='p33':

            if criterio_seleccionado=='c1':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota
                respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
           
            elif criterio_seleccionado=='c2':
                
                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p33_df.loc[p33_df['_index']==iniciativa_seleccionada, criterio_seleccionado_bucle]=nota

                #CALCULO PROMEDIO INICIATIVA
                p33_df['l1']= p33_df[criterios_disponibles_bucle].mean(axis=1)
                p33_df.to_excel(f'./files/separadas/repeat_p33.xlsx',index=False)

                nota_entidad = round(p33_df.loc[p33_df['_submission__uuid']==entidad_seleccionada]['l1'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota_entidad
            
            else:
                pass

            p33_df['nota_iniciativa'] = p33_df['l1']
            p33_df.to_excel(f'./files/separadas/repeat_p33.xlsx',index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta
            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        #sistematización de retos de funcionarios contratistas
        elif pregunta_seleccionada=='p34':

            if criterio_seleccionado=='c1':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota
                respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
           
            elif criterio_seleccionado=='c2':
                
                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p34_df.loc[p34_df['_index']==iniciativa_seleccionada, criterio_seleccionado_bucle]=nota

                #CALCULO PROMEDIO INICIATIVA
                p34_df['l1']= p34_df[criterios_disponibles_bucle].mean(axis=1)
                p34_df.to_excel(f'./files/separadas/repeat_p34.xlsx',index=False)

                nota_entidad = round(p34_df.loc[p34_df['_submission__uuid']==entidad_seleccionada]['l1'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota_entidad
            
            else:
                pass

            p34_df['nota_iniciativa'] = p34_df['l1']
            p34_df.to_excel(f'./files/separadas/repeat_p34.xlsx',index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta
            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        #sistematización ideas de ciudadanos
        elif pregunta_seleccionada=='p35':

            if criterio_seleccionado=='c1':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota
                respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
           
            elif criterio_seleccionado=='c2':
                
                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p35_df.loc[p35_df['_index']==iniciativa_seleccionada, criterio_seleccionado_bucle]=nota

                #CALCULO PROMEDIO INICIATIVA
                p35_df['l1']= p35_df[criterios_disponibles_bucle].mean(axis=1)
                p35_df.to_excel(f'./files/separadas/repeat_p35.xlsx',index=False)

                nota_entidad = round(p35_df.loc[p35_df['_submission__uuid']==entidad_seleccionada]['l1'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota_entidad
            
            else:
                pass

            p35_df['nota_iniciativa'] = p35_df['l1']
            p35_df.to_excel(f'./files/separadas/repeat_p35.xlsx',index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta
            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        #sistematización ideas de funcionarios contratistas
        elif pregunta_seleccionada=='p36':

            if criterio_seleccionado=='c1':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota
                respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
           
            elif criterio_seleccionado=='c2':
                
                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p36_df.loc[p36_df['_index']==iniciativa_seleccionada, criterio_seleccionado_bucle]=nota

                #CALCULO PROMEDIO INICIATIVA
                p36_df['l1']= p36_df[criterios_disponibles_bucle].mean(axis=1)
                p36_df.to_excel(f'./files/separadas/repeat_p36.xlsx',index=False)

                nota_entidad = round(p36_df.loc[p36_df['_submission__uuid']==entidad_seleccionada]['l1'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota_entidad
            
            else:
                pass

            p36_df['nota_iniciativa'] = p36_df['l1']
            p36_df.to_excel(f'./files/separadas/repeat_p36.xlsx',index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta
            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        #buenas prácticas y lecciones aprendidas en innovación
        elif pregunta_seleccionada=='p37':

            if criterio_seleccionado=='c1':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota
                respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
           
            elif criterio_seleccionado=='c2':
                
                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p37_df.loc[p37_df['_index']==iniciativa_seleccionada, criterio_seleccionado_bucle]=nota

                #CALCULO PROMEDIO INICIATIVA
                p37_df['l1']= p37_df[criterios_disponibles_bucle].mean(axis=1)
                p37_df.to_excel(f'./files/separadas/repeat_p37.xlsx',index=False)

                nota_entidad = round(p37_df.loc[p37_df['_submission__uuid']==entidad_seleccionada]['l1'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota_entidad
            
            else:
                pass

            p37_df['nota_iniciativa'] = p37_df['l1']
            p37_df.to_excel(f'./files/separadas/repeat_p37.xlsx',index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta
            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        #buenas prácticas y lecciones aprendidas generales
        elif pregunta_seleccionada=='p38':

            if criterio_seleccionado=='c1':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota
                respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
           
            elif criterio_seleccionado=='c2':
                
                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p38_df.loc[p38_df['_index']==iniciativa_seleccionada, criterio_seleccionado_bucle]=nota

                #CALCULO PROMEDIO INICIATIVA
                p38_df['l1']= p38_df[criterios_disponibles_bucle].mean(axis=1)
                p38_df.to_excel(f'./files/separadas/repeat_p38.xlsx',index=False)

                nota_entidad = round(p38_df.loc[p38_df['_submission__uuid']==entidad_seleccionada]['l1'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota_entidad
            
            else:
                pass

            p38_df['nota_iniciativa'] = p38_df['l1']
            p38_df.to_excel(f'./files/separadas/repeat_p38.xlsx',index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta
            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        #Monitoreo y seguimiento a innovaciones
        elif pregunta_seleccionada=='p39':

            if criterio_seleccionado=='c1':
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota
                respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
           
            elif criterio_seleccionado=='c2':
                
                #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
                p39_df.loc[p39_df['_index']==iniciativa_seleccionada, criterio_seleccionado_bucle]=nota

                #CALCULO PROMEDIO INICIATIVA
                p39_df['l1']= p39_df[criterios_disponibles_bucle].mean(axis=1)
                p39_df.to_excel(f'./files/separadas/repeat_p39.xlsx',index=False)

                nota_entidad = round(p39_df.loc[p39_df['_submission__uuid']==entidad_seleccionada]['l1'].mean(),2)
                respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_{criterio_seleccionado}'] = nota_entidad
            
            else:
                pass

            p39_df['nota_iniciativa'] = p39_df['l1']
            p39_df.to_excel(f'./files/separadas/repeat_p39.xlsx',index=False)

            nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
            resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta
            respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
            resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

        #Cualquier caso no definido
        else:
            pass

        nota_componente_1=round(resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,'p1':'p13'].sum().sum(),2)
        resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,'res_c1'] = nota_componente_1

        nota_componente_2=round(resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,'p14':'p27'].sum().sum(),2)
        resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,'res_c2'] = nota_componente_2

        nota_componente_3=round(resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,'p28':'p30'].sum().sum(),2)
        resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,'res_c3'] = nota_componente_3

        nota_componente_4=round(resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,'p31':'p39'].sum().sum(),2)
        resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,'res_c4'] = nota_componente_4

        total_iip_entidad=round(resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,'res_c1':'res_c4'].sum().sum(),2)
        resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,'total'] = total_iip_entidad

#Callback ver respuestas
@dash.callback(
    Output('pregunta', 'children'),
    Output('criterio', 'children'),
    Output('respuesta_2021', 'children'),
    Output('nota_obtenida_2021', 'children'),
    Output('nota_max_2021', 'children'),
    Output('respuesta_2023', 'children'),
    Output('selector_iniciativa', 'options'),
    Output('selector_iniciativa', 'value'),
    Output('selector_criterio_entidad', 'options'),
    Output('selector_criterio_entidad', 'value'),

    Input('entidad_seleccionada', 'data'),
    Input('pregunta_seleccionada', 'data'),
)
def visualizacion_respuestas(entidad_seleccionada,pregunta_seleccionada):
  
    def test_empty_pregunta(entidad_seleccionada,pregunta_seleccionada):
        #pregunta textual
        try:
            pregunta = preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['pregunta 2023']
            salida_pregunta=pregunta
            out_pre='Success'
        except Exception as e_pre:
            pregunta = 'N/A'
            salida_pregunta=pregunta
            out_pre=f"|||PREGUNTA||| Couldn't load pregunta due to {e_pre}"
            print(out_pre)

        return salida_pregunta,out_pre
    
    def test_empty_respuesta_2021(entidad_seleccionada,pregunta_seleccionada):
        #respuesta 2021
        try:
            respuesta_2021 = respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][pregunta_seleccionada]
            if respuesta_2021.empty ==False:
                salida_respuesta_2021=respuesta_2021
            else:
                salida_respuesta_2021 = 'N/A'
            out_2021='Success'
        except Exception as e_res_2021:
            salida_respuesta_2021 = respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada]['p1']
            out_2021=f"|||RESPUESTA 2021||| Couldn't load respuesta 2021 due to {e_res_2021}"
            print(out_2021)
        
        return salida_respuesta_2021,out_2021
    
    def test_empty_respuesta_2023(entidad_seleccionada,pregunta_seleccionada):
        #Respuesta 2023
        try:
            respuesta_2023 = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][pregunta_seleccionada]
            if respuesta_2023.empty ==False:
                salida_respuesta_2023=respuesta_2023
            else:
                salida_respuesta_2023 = 'N/A'
            out_2023='Success'
        except Exception as e_res_2023:
            salida_respuesta_2023 = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p1']
            out_2023=f"|||RESPUESTA 2023||| Couldn't load respuesta 2023 due to {e_res_2023}"
            print(out_2023)

        return salida_respuesta_2023,out_2023

    pregunta,error_pregunta=test_empty_pregunta(entidad_seleccionada,pregunta_seleccionada)
    respuesta_2021,error_2021=test_empty_respuesta_2021(entidad_seleccionada,pregunta_seleccionada)
    respuesta_2023,error_2023=test_empty_respuesta_2023(entidad_seleccionada,pregunta_seleccionada)

    estilo={'display':'flex','flex-wrap': 'wrap','justify-content':'space-between'}
    indices_carousel=[0]
    salida_criterio=indices_carousel

    #Acuerdos y/o actos administrativos
    if pregunta_seleccionada=='p1':

        indices_carousel = p1_df[p1_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p1_df[p1_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_cod']
        nombres_carousel = p1_df[p1_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_nom']
        descripciones_carousel = p1_df[p1_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_des']
        soportes_carousel = p1_df[p1_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']
        
        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p1_p2(
                        ind_car=list(indices_carousel)[i],
                        cod_car=list(codigos_carousel)[i],
                        nom_car=list(nombres_carousel)[i],
                        des_car=list(descripciones_carousel)[i],
                        sop_car=list(soportes_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_1()
        
    #Enfoques, lineas o proyectos
    elif pregunta_seleccionada=='p2':

        indices_carousel = p2_df[p2_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p2_df[p2_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_cod']
        nombres_carousel = p2_df[p2_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_nom']
        descripciones_carousel = p2_df[p2_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_des']
        soportes_carousel = p2_df[p2_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p1_p2(
                        ind_car=list(indices_carousel)[i],
                        cod_car=list(codigos_carousel)[i],
                        nom_car=list(nombres_carousel)[i],
                        des_car=list(descripciones_carousel)[i],
                        sop_car=list(soportes_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_2()

    #Presupuesto general
    elif pregunta_seleccionada=='p3':

        try:
            costo_2019_2020 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]
        except Exception as e:
            costo_2019_2020 = 'N/A'
        
        presupuesto_2021_dis = respuestas_2023_df[f'p3_val_1'].median()
        presupuesto_2022_dis = respuestas_2023_df[f'p3_val_2'].median()
        costo_2021_dis = respuestas_2023_df[f'p4_val_1'].median()
        costo_2022_dis = respuestas_2023_df[f'p4_val_2'].median()

        presupuesto_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p3_val_1']
        presupuesto_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p3_val_2']
        costo_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p4_val_1']
        costo_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p4_val_2']

        soporte_2023 = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        salida_respuesta_2021=f"Presupuesto: \n {costo_2019_2020}"

        cards=[]
        tipo_pregunta=['Presupuesto funcionamiento', 'Presupuesto inversión']

        rel_dist_pre = statistics.mean([float(presupuesto_2021_dis), float(presupuesto_2022_dis)])
        rel_dist_cos = statistics.mean([float(costo_2021_dis), float(costo_2022_dis)])
        res_dis = rel_dist_cos*100/rel_dist_pre

        rel_enti_pre = statistics.mean([float(presupuesto_2021_ent.iloc[0]), float(presupuesto_2022_ent.iloc[0])])
        rel_enti_cos = statistics.mean([float(costo_2021_ent.iloc[0]), float(costo_2022_ent.iloc[0])])
        res_ent=rel_enti_cos*100/rel_enti_pre
            
        card_2023=card_p3_p4_p5_p6(
            tip_preg=tipo_pregunta[0],

            pre_2021_dis=presupuesto_2021_dis,
            pre_2022_dis=presupuesto_2022_dis,
            pre_med_dis=rel_dist_pre,
            cos_2021_dis=costo_2021_dis,
            cos_2022_dis=costo_2022_dis,
            cos_med_dis=rel_dist_cos,
            res_dist=res_dis,

            pre_2021_ent=list(presupuesto_2021_ent)[0],
            pre_2022_ent=list(presupuesto_2022_ent)[0],
            pre_med_ent=rel_enti_pre,
            cos_2021_ent=list(costo_2021_ent)[0],
            cos_2022_ent=list(costo_2022_ent)[0],
            cos_med_ent=rel_enti_cos,
            res_enti=res_ent,

            sop_car_2023=list(soporte_2023)[0],
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])
        
        salida_criterio=criterio_3()
        salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        
    #Presupuesto general innovación
    elif pregunta_seleccionada=='p4':

        try:
            costo_2019_2020 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]
        except Exception as e:
            costo_2019_2020 = 'N/A'
        
        presupuesto_2021_dis = respuestas_2023_df[f'p3_val_1'].median()
        presupuesto_2022_dis = respuestas_2023_df[f'p3_val_2'].median()
        costo_2021_dis = respuestas_2023_df[f'p4_val_1'].median()
        costo_2022_dis = respuestas_2023_df[f'p4_val_2'].median()

        presupuesto_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p3_val_1']
        presupuesto_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p3_val_2']
        costo_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p4_val_1']
        costo_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p4_val_2']

        soporte_2023 = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        salida_respuesta_2021=f"Presupuesto: \n {costo_2019_2020}"

        cards=[]
        tipo_pregunta=['Presupuesto funcionamiento', 'Presupuesto inversión']

        rel_dist_pre = statistics.mean([float(presupuesto_2021_dis), float(presupuesto_2022_dis)])
        rel_dist_cos = statistics.mean([float(costo_2021_dis), float(costo_2022_dis)])
        res_dis = rel_dist_cos*100/rel_dist_pre

        rel_enti_pre = statistics.mean([float(presupuesto_2021_ent.iloc[0]), float(presupuesto_2022_ent.iloc[0])])
        rel_enti_cos = statistics.mean([float(costo_2021_ent.iloc[0]), float(costo_2022_ent.iloc[0])])
        res_ent=rel_enti_cos*100/rel_enti_pre
            
        card_2023=card_p3_p4_p5_p6(
            tip_preg=tipo_pregunta[0],

            pre_2021_dis=presupuesto_2021_dis,
            pre_2022_dis=presupuesto_2022_dis,
            pre_med_dis=rel_dist_pre,
            cos_2021_dis=costo_2021_dis,
            cos_2022_dis=costo_2022_dis,
            cos_med_dis=rel_dist_cos,
            res_dist=res_dis,

            pre_2021_ent=list(presupuesto_2021_ent)[0],
            pre_2022_ent=list(presupuesto_2022_ent)[0],
            pre_med_ent=rel_enti_pre,
            cos_2021_ent=list(costo_2021_ent)[0],
            cos_2022_ent=list(costo_2022_ent)[0],
            cos_med_ent=rel_enti_cos,
            res_enti=res_ent,

            sop_car_2023=list(soporte_2023)[0],
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])
        
        salida_criterio=criterio_4()
        salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        
    #Presupuesto inversión general
    elif pregunta_seleccionada=='p5':

        try:
            costo_2019_2020 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]
        except Exception as e:
            costo_2019_2020 = 'N/A'
        
        presupuesto_2021_dis = respuestas_2023_df[f'p5_val_1'].median()
        presupuesto_2022_dis = respuestas_2023_df[f'p5_val_2'].median()
        costo_2021_dis = respuestas_2023_df[f'p6_val_1'].median()
        costo_2022_dis = respuestas_2023_df[f'p6_val_2'].median()

        presupuesto_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p5_val_1']
        presupuesto_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p5_val_2']
        costo_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p6_val_1']
        costo_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p6_val_2']

        soporte_2023 = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        salida_respuesta_2021=f"Presupuesto: \n {costo_2019_2020}"

        cards=[]
        tipo_pregunta=['Presupuesto funcionamiento', 'Presupuesto inversión']

        rel_dist_pre = statistics.mean([float(presupuesto_2021_dis), float(presupuesto_2022_dis)])
        rel_dist_cos = statistics.mean([float(costo_2021_dis), float(costo_2022_dis)])
        res_dis = rel_dist_cos*100/rel_dist_pre

        rel_enti_pre = statistics.mean([float(presupuesto_2021_ent.iloc[0]), float(presupuesto_2022_ent.iloc[0])])
        rel_enti_cos = statistics.mean([float(costo_2021_ent.iloc[0]), float(costo_2022_ent.iloc[0])])
        res_ent=rel_enti_cos*100/rel_enti_pre
            
        card_2023=card_p3_p4_p5_p6(
            tip_preg=tipo_pregunta[0],

            pre_2021_dis=presupuesto_2021_dis,
            pre_2022_dis=presupuesto_2022_dis,
            pre_med_dis=rel_dist_pre,
            cos_2021_dis=costo_2021_dis,
            cos_2022_dis=costo_2022_dis,
            cos_med_dis=rel_dist_cos,
            res_dist=res_dis,

            pre_2021_ent=list(presupuesto_2021_ent)[0],
            pre_2022_ent=list(presupuesto_2022_ent)[0],
            pre_med_ent=rel_enti_pre,
            cos_2021_ent=list(costo_2021_ent)[0],
            cos_2022_ent=list(costo_2022_ent)[0],
            cos_med_ent=rel_enti_cos,
            res_enti=res_ent,

            sop_car_2023=list(soporte_2023)[0],
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])
        
        salida_criterio=criterio_5()
        salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        
    #Presupuesto inversión innovación
    elif pregunta_seleccionada=='p6':

        try:
            costo_2019_2020 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]
        except Exception as e:
            costo_2019_2020 = 'N/A'
        
        presupuesto_2021_dis = respuestas_2023_df[f'p5_val_1'].median()
        presupuesto_2022_dis = respuestas_2023_df[f'p5_val_2'].median()
        costo_2021_dis = respuestas_2023_df[f'p6_val_1'].median()
        costo_2022_dis = respuestas_2023_df[f'p6_val_2'].median()

        presupuesto_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p5_val_1']
        presupuesto_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p5_val_2']
        costo_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p6_val_1']
        costo_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p6_val_2']

        soporte_2023 = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        salida_respuesta_2021=f"Presupuesto: \n {costo_2019_2020}"

        cards=[]
        tipo_pregunta=['Presupuesto funcionamiento', 'Presupuesto inversión']

        rel_dist_pre = statistics.mean([float(presupuesto_2021_dis), float(presupuesto_2022_dis)])
        rel_dist_cos = statistics.mean([float(costo_2021_dis), float(costo_2022_dis)])
        res_dis = rel_dist_cos*100/rel_dist_pre

        rel_enti_pre = statistics.mean([float(presupuesto_2021_ent.iloc[0]), float(presupuesto_2022_ent.iloc[0])])
        rel_enti_cos = statistics.mean([float(costo_2021_ent.iloc[0]), float(costo_2022_ent.iloc[0])])
        res_ent=rel_enti_cos*100/rel_enti_pre
            
        card_2023=card_p3_p4_p5_p6(
            tip_preg=tipo_pregunta[0],

            pre_2021_dis=presupuesto_2021_dis,
            pre_2022_dis=presupuesto_2022_dis,
            pre_med_dis=rel_dist_pre,
            cos_2021_dis=costo_2021_dis,
            cos_2022_dis=costo_2022_dis,
            cos_med_dis=rel_dist_cos,
            res_dist=res_dis,

            pre_2021_ent=list(presupuesto_2021_ent)[0],
            pre_2022_ent=list(presupuesto_2022_ent)[0],
            pre_med_ent=rel_enti_pre,
            cos_2021_ent=list(costo_2021_ent)[0],
            cos_2022_ent=list(costo_2022_ent)[0],
            cos_med_ent=rel_enti_cos,
            res_enti=res_ent,

            sop_car_2023=list(soporte_2023)[0],
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])
        
        salida_criterio=criterio_6()
        salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        
    #Funcionarios total
    elif pregunta_seleccionada=='p7':

        try:
            funcionarios_ent = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]
        except Exception as e:
            funcionarios_ent = 'N/A'

        cantidad_2021_dis = respuestas_2023_df[f'p7_val_1'].median()
        cantidad_2022_dis = respuestas_2023_df[f'p7_val_2'].median()
        manual_2021_dis = respuestas_2023_df[f'p8_val_1'].median()
        manual_2022_dis = respuestas_2023_df[f'p8_val_2'].median()
        ocasionales_2021_dis = respuestas_2023_df[f'p9_val_1'].median()
        ocasionales_2022_dis = respuestas_2023_df[f'p9_val_2'].median()
        
        cantidad_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p7_val_1']
        cantidad_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p7_val_2']
        manual_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p8_val_1']
        manual_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p8_val_2']
        ocasionales_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p9_val_1']
        ocasionales_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p9_val_2']

        soporte = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        salida_respuesta_2021=f"Funcionarios: \n {funcionarios_ent}"

        cards=[]
        tipo_pregunta=['Funcionarios', 'Contratistas']

        rel_dist_tot = statistics.mean([float(cantidad_2021_dis), float(cantidad_2022_dis)])
        rel_dist_man = statistics.mean([float(manual_2021_dis), float(manual_2022_dis)])
        rel_dist_oca = statistics.mean([float(ocasionales_2021_dis), float(ocasionales_2022_dis)])
        res_dis = rel_dist_man*100/rel_dist_tot

        rel_enti_tot = statistics.mean([float(cantidad_2021_ent.iloc[0]), float(cantidad_2022_ent.iloc[0])])
        rel_enti_man = statistics.mean([float(manual_2021_ent.iloc[0]), float(manual_2022_ent.iloc[0])])
        rel_enti_oca = statistics.mean([float(ocasionales_2021_ent.iloc[0]), float(ocasionales_2022_ent.iloc[0])])
        res_ent = rel_enti_man*100/rel_enti_tot
            
        card_2023=card_p7_p8_p9_p10_p11_p12(
            tip_preg=tipo_pregunta[0],

            can_2021_dis=cantidad_2021_dis,
            can_2022_dis=cantidad_2022_dis,
            can_med_dis=rel_dist_tot,
            fun_2021_dis=manual_2021_dis,
            fun_2022_dis=manual_2022_dis,
            fun_med_dis=rel_dist_man,
            oca_2021_dis=ocasionales_2021_dis,
            oca_2022_dis=ocasionales_2022_dis,
            oca_med_dis=rel_dist_oca,
            res_dist=res_dis,

            can_2021_ent=list(cantidad_2021_ent)[0],
            can_2022_ent=list(cantidad_2022_ent)[0],
            can_med_ent=rel_enti_tot,
            fun_2021_ent=list(manual_2021_ent)[0],
            fun_2022_ent=list(manual_2022_ent)[0],
            fun_med_ent=rel_enti_man,
            oca_2021_ent=list(ocasionales_2021_ent)[0],
            oca_2022_ent=list(ocasionales_2022_ent)[0],
            oca_med_ent=rel_enti_oca,
            res_enti=res_ent,

            sop_car=list(soporte)[0]
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])
        
        salida_criterio=criterio_7()
        salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        
    #Funcionarios manual en innovación 
    elif pregunta_seleccionada=='p8':

        try:
            funcionarios_ent = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]
        except Exception as e:
            funcionarios_ent = 'N/A'
        
        cantidad_2021_dis = respuestas_2023_df[f'p7_val_1'].median()
        cantidad_2022_dis = respuestas_2023_df[f'p7_val_2'].median()
        manual_2021_dis = respuestas_2023_df[f'p8_val_1'].median()
        manual_2022_dis = respuestas_2023_df[f'p8_val_2'].median()
        ocasionales_2021_dis = respuestas_2023_df[f'p9_val_1'].median()
        ocasionales_2022_dis = respuestas_2023_df[f'p9_val_2'].median()
        
        cantidad_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p7_val_1']
        cantidad_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p7_val_2']
        manual_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p8_val_1']
        manual_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p8_val_2']
        ocasionales_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p9_val_1']
        ocasionales_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p9_val_2']

        soporte = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        salida_respuesta_2021=f"Funcionarios: \n {funcionarios_ent}"

        cards=[]
        tipo_pregunta=['Funcionarios', 'Contratistas']

        rel_dist_tot = statistics.mean([float(cantidad_2021_dis), float(cantidad_2022_dis)])
        rel_dist_man = statistics.mean([float(manual_2021_dis), float(manual_2022_dis)])
        rel_dist_oca = statistics.mean([float(ocasionales_2021_dis), float(ocasionales_2022_dis)])
        res_dis = rel_dist_man*100/rel_dist_tot

        rel_enti_tot = statistics.mean([float(cantidad_2021_ent.iloc[0]), float(cantidad_2022_ent.iloc[0])])
        rel_enti_man = statistics.mean([float(manual_2021_ent.iloc[0]), float(manual_2022_ent.iloc[0])])
        rel_enti_oca = statistics.mean([float(ocasionales_2021_ent.iloc[0]), float(ocasionales_2022_ent.iloc[0])])
        res_ent = rel_enti_man*100/rel_enti_tot
            
        card_2023=card_p7_p8_p9_p10_p11_p12(
            tip_preg=tipo_pregunta[0],

            can_2021_dis=cantidad_2021_dis,
            can_2022_dis=cantidad_2022_dis,
            can_med_dis=rel_dist_tot,
            fun_2021_dis=manual_2021_dis,
            fun_2022_dis=manual_2022_dis,
            fun_med_dis=rel_dist_man,
            oca_2021_dis=ocasionales_2021_dis,
            oca_2022_dis=ocasionales_2022_dis,
            oca_med_dis=rel_dist_oca,
            res_dist=res_dis,

            can_2021_ent=list(cantidad_2021_ent)[0],
            can_2022_ent=list(cantidad_2022_ent)[0],
            can_med_ent=rel_enti_tot,
            fun_2021_ent=list(manual_2021_ent)[0],
            fun_2022_ent=list(manual_2022_ent)[0],
            fun_med_ent=rel_enti_man,
            oca_2021_ent=list(ocasionales_2021_ent)[0],
            oca_2022_ent=list(ocasionales_2022_ent)[0],
            oca_med_ent=rel_enti_oca,
            res_enti=res_ent,

            sop_car=list(soporte)[0]
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])
        
        salida_criterio=criterio_8()
        salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        
    #Funcionarios ocasionales
    elif pregunta_seleccionada=='p9':

        try:
            funcionarios_ent = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'p8'])[0]
        except Exception as e:
            funcionarios_ent = 'N/A'

        cantidad_2021_dis = respuestas_2023_df[f'p7_val_1'].median()
        cantidad_2022_dis = respuestas_2023_df[f'p7_val_2'].median()
        manual_2021_dis = respuestas_2023_df[f'p8_val_1'].median()
        manual_2022_dis = respuestas_2023_df[f'p8_val_2'].median()
        ocasionales_2021_dis = respuestas_2023_df[f'p9_val_1'].median()
        ocasionales_2022_dis = respuestas_2023_df[f'p9_val_2'].median()
        
        cantidad_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p7_val_1']
        cantidad_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p7_val_2']
        manual_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p8_val_1']
        manual_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p8_val_2']
        ocasionales_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p9_val_1']
        ocasionales_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p9_val_2']

        soporte = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada]['p8']
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        salida_respuesta_2021=f"Funcionarios: \n {funcionarios_ent}"

        cards=[]
        tipo_pregunta=['Funcionarios', 'Contratistas']

        rel_dist_tot = statistics.mean([float(cantidad_2021_dis), float(cantidad_2022_dis)])
        rel_dist_man = statistics.mean([float(manual_2021_dis), float(manual_2022_dis)])
        rel_dist_oca = statistics.mean([float(ocasionales_2021_dis), float(ocasionales_2022_dis)])
        res_dis = rel_dist_man*100/rel_dist_tot

        rel_enti_tot = statistics.mean([float(cantidad_2021_ent.iloc[0]), float(cantidad_2022_ent.iloc[0])])
        rel_enti_man = statistics.mean([float(manual_2021_ent.iloc[0]), float(manual_2022_ent.iloc[0])])
        rel_enti_oca = statistics.mean([float(ocasionales_2021_ent.iloc[0]), float(ocasionales_2022_ent.iloc[0])])
        res_ent = rel_enti_man*100/rel_enti_tot
            
        card_2023=card_p7_p8_p9_p10_p11_p12(
            tip_preg=tipo_pregunta[0],

            can_2021_dis=cantidad_2021_dis,
            can_2022_dis=cantidad_2022_dis,
            can_med_dis=rel_dist_tot,
            fun_2021_dis=manual_2021_dis,
            fun_2022_dis=manual_2022_dis,
            fun_med_dis=rel_dist_man,
            oca_2021_dis=ocasionales_2021_dis,
            oca_2022_dis=ocasionales_2022_dis,
            oca_med_dis=rel_dist_oca,
            res_dist=res_dis,

            can_2021_ent=list(cantidad_2021_ent)[0],
            can_2022_ent=list(cantidad_2022_ent)[0],
            can_med_ent=rel_enti_tot,
            fun_2021_ent=list(manual_2021_ent)[0],
            fun_2022_ent=list(manual_2022_ent)[0],
            fun_med_ent=rel_enti_man,
            oca_2021_ent=list(ocasionales_2021_ent)[0],
            oca_2022_ent=list(ocasionales_2022_ent)[0],
            oca_med_ent=rel_enti_oca,
            res_enti=res_ent,

            sop_car=list(soporte)[0]
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])
        
        salida_criterio=criterio_9()
        salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        
    #Contratistas total
    elif pregunta_seleccionada=='p10':
        
        try:
            contratistas_ent = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]
        except Exception as e:
            contratistas_ent = 'N/A'
        
        cantidad_2021_dis = respuestas_2023_df[f'p10_val_1'].median()
        cantidad_2022_dis = respuestas_2023_df[f'p10_val_2'].median()
        manual_2021_dis = respuestas_2023_df[f'p11_val_1'].median()
        manual_2022_dis = respuestas_2023_df[f'p11_val_2'].median()
        ocasionales_2021_dis = respuestas_2023_df[f'p12_val_1'].median()
        ocasionales_2022_dis = respuestas_2023_df[f'p12_val_2'].median()
        
        cantidad_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p10_val_1']
        cantidad_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p10_val_2']
        manual_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p11_val_1']
        manual_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p11_val_2']
        ocasionales_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p12_val_1']
        ocasionales_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p12_val_2']

        soporte = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        salida_respuesta_2021=f"Funcionarios: \n {contratistas_ent}"

        cards=[]
        tipo_pregunta=['Funcionarios', 'Contratistas']

        rel_dist_tot = statistics.mean([float(cantidad_2021_dis), float(cantidad_2022_dis)])
        rel_dist_man = statistics.mean([float(manual_2021_dis), float(manual_2022_dis)])
        rel_dist_oca = statistics.mean([float(ocasionales_2021_dis), float(ocasionales_2022_dis)])
        res_dis = rel_dist_man*100/rel_dist_tot

        rel_enti_tot = statistics.mean([float(cantidad_2021_ent.iloc[0]), float(cantidad_2022_ent.iloc[0])])
        rel_enti_man = statistics.mean([float(manual_2021_ent.iloc[0]), float(manual_2022_ent.iloc[0])])
        rel_enti_oca = statistics.mean([float(ocasionales_2021_ent.iloc[0]), float(ocasionales_2022_ent.iloc[0])])
        res_ent = rel_enti_man*100/rel_enti_tot
            
        card_2023=card_p7_p8_p9_p10_p11_p12(
            tip_preg=tipo_pregunta[1],

            can_2021_dis=cantidad_2021_dis,
            can_2022_dis=cantidad_2022_dis,
            can_med_dis=rel_dist_tot,
            fun_2021_dis=manual_2021_dis,
            fun_2022_dis=manual_2022_dis,
            fun_med_dis=rel_dist_man,
            oca_2021_dis=ocasionales_2021_dis,
            oca_2022_dis=ocasionales_2022_dis,
            oca_med_dis=rel_dist_oca,
            res_dist=res_dis,

            can_2021_ent=list(cantidad_2021_ent)[0],
            can_2022_ent=list(cantidad_2022_ent)[0],
            can_med_ent=rel_enti_tot,
            fun_2021_ent=list(manual_2021_ent)[0],
            fun_2022_ent=list(manual_2022_ent)[0],
            fun_med_ent=rel_enti_man,
            oca_2021_ent=list(ocasionales_2021_ent)[0],
            oca_2022_ent=list(ocasionales_2022_ent)[0],
            oca_med_ent=rel_enti_oca,
            res_enti=res_ent,

            sop_car=list(soporte)[0]
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])
        
        salida_criterio=criterio_10()
        salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        
    #Contratistas en innovación 
    elif pregunta_seleccionada=='p11':

        try:
            contratistas_ent = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]
        except Exception as e:
            contratistas_ent = 'N/A'
        
        cantidad_2021_dis = respuestas_2023_df[f'p10_val_1'].median()
        cantidad_2022_dis = respuestas_2023_df[f'p10_val_2'].median()
        manual_2021_dis = respuestas_2023_df[f'p11_val_1'].median()
        manual_2022_dis = respuestas_2023_df[f'p11_val_2'].median()
        ocasionales_2021_dis = respuestas_2023_df[f'p12_val_1'].median()
        ocasionales_2022_dis = respuestas_2023_df[f'p12_val_2'].median()
        
        cantidad_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p10_val_1']
        cantidad_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p10_val_2']
        manual_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p11_val_1']
        manual_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p11_val_2']
        ocasionales_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p12_val_1']
        ocasionales_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p12_val_2']

        soporte = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        salida_respuesta_2021=f"Funcionarios: \n {contratistas_ent}"

        cards=[]
        tipo_pregunta=['Funcionarios', 'Contratistas']

        rel_dist_tot = statistics.mean([float(cantidad_2021_dis), float(cantidad_2022_dis)])
        rel_dist_man = statistics.mean([float(manual_2021_dis), float(manual_2022_dis)])
        rel_dist_oca = statistics.mean([float(ocasionales_2021_dis), float(ocasionales_2022_dis)])
        res_dis = rel_dist_man*100/rel_dist_tot

        rel_enti_tot = statistics.mean([float(cantidad_2021_ent.iloc[0]), float(cantidad_2022_ent.iloc[0])])
        rel_enti_man = statistics.mean([float(manual_2021_ent.iloc[0]), float(manual_2022_ent.iloc[0])])
        rel_enti_oca = statistics.mean([float(ocasionales_2021_ent.iloc[0]), float(ocasionales_2022_ent.iloc[0])])
        res_ent = rel_enti_man*100/rel_enti_tot
            
        card_2023=card_p7_p8_p9_p10_p11_p12(
            tip_preg=tipo_pregunta[1],

            can_2021_dis=cantidad_2021_dis,
            can_2022_dis=cantidad_2022_dis,
            can_med_dis=rel_dist_tot,
            fun_2021_dis=manual_2021_dis,
            fun_2022_dis=manual_2022_dis,
            fun_med_dis=rel_dist_man,
            oca_2021_dis=ocasionales_2021_dis,
            oca_2022_dis=ocasionales_2022_dis,
            oca_med_dis=rel_dist_oca,
            res_dist=res_dis,

            can_2021_ent=list(cantidad_2021_ent)[0],
            can_2022_ent=list(cantidad_2022_ent)[0],
            can_med_ent=rel_enti_tot,
            fun_2021_ent=list(manual_2021_ent)[0],
            fun_2022_ent=list(manual_2022_ent)[0],
            fun_med_ent=rel_enti_man,
            oca_2021_ent=list(ocasionales_2021_ent)[0],
            oca_2022_ent=list(ocasionales_2022_ent)[0],
            oca_med_ent=rel_enti_oca,
            res_enti=res_ent,

            sop_car=list(soporte)[0]
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])

        salida_criterio=criterio_11()
        salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        
    #Contratistas ocasionales
    elif pregunta_seleccionada=='p12':

        try:
            contratistas_ent = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'p11'])[0]
        except Exception as e:
            contratistas_ent = 'N/A'

        cantidad_2021_dis = respuestas_2023_df[f'p10_val_1'].median()
        cantidad_2022_dis = respuestas_2023_df[f'p10_val_2'].median()
        manual_2021_dis = respuestas_2023_df[f'p11_val_1'].median()
        manual_2022_dis = respuestas_2023_df[f'p11_val_2'].median()
        ocasionales_2021_dis = respuestas_2023_df[f'p12_val_1'].median()
        ocasionales_2022_dis = respuestas_2023_df[f'p12_val_2'].median()
        
        cantidad_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p10_val_1']
        cantidad_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p10_val_2']
        manual_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p11_val_1']
        manual_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p11_val_2']
        ocasionales_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p12_val_1']
        ocasionales_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p12_val_2']

        soporte = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada]['p11']
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        salida_respuesta_2021=f"Funcionarios: \n {contratistas_ent}"

        cards=[]
        tipo_pregunta=['Funcionarios', 'Contratistas']

        rel_dist_tot = statistics.mean([float(cantidad_2021_dis), float(cantidad_2022_dis)])
        rel_dist_man = statistics.mean([float(manual_2021_dis), float(manual_2022_dis)])
        rel_dist_oca = statistics.mean([float(ocasionales_2021_dis), float(ocasionales_2022_dis)])
        res_dis = rel_dist_man*100/rel_dist_tot

        rel_enti_tot = statistics.mean([float(cantidad_2021_ent.iloc[0]), float(cantidad_2022_ent.iloc[0])])
        rel_enti_man = statistics.mean([float(manual_2021_ent.iloc[0]), float(manual_2022_ent.iloc[0])])
        rel_enti_oca = statistics.mean([float(ocasionales_2021_ent.iloc[0]), float(ocasionales_2022_ent.iloc[0])])
        res_ent = rel_enti_man*100/rel_enti_tot
            
        card_2023=card_p7_p8_p9_p10_p11_p12(
            tip_preg=tipo_pregunta[1],

            can_2021_dis=cantidad_2021_dis,
            can_2022_dis=cantidad_2022_dis,
            can_med_dis=rel_dist_tot,
            fun_2021_dis=manual_2021_dis,
            fun_2022_dis=manual_2022_dis,
            fun_med_dis=rel_dist_man,
            oca_2021_dis=ocasionales_2021_dis,
            oca_2022_dis=ocasionales_2022_dis,
            oca_med_dis=rel_dist_oca,
            res_dist=res_dis,

            can_2021_ent=list(cantidad_2021_ent)[0],
            can_2022_ent=list(cantidad_2022_ent)[0],
            can_med_ent=rel_enti_tot,
            fun_2021_ent=list(manual_2021_ent)[0],
            fun_2022_ent=list(manual_2022_ent)[0],
            fun_med_ent=rel_enti_man,
            oca_2021_ent=list(ocasionales_2021_ent)[0],
            oca_2022_ent=list(ocasionales_2022_ent)[0],
            oca_med_ent=rel_enti_oca,
            res_enti=res_ent,

            sop_car=list(soporte)[0]
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])
        
        salida_criterio=criterio_12()
        salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        
    # Recursos digitales
    elif pregunta_seleccionada=='p13':

        indices_carousel = p13_df[p13_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p13_df[p13_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_nom']
        descripciones_carousel = p13_df[p13_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_des']
        costo_carousel = p13_df[p13_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_cos']
        soportes_carousel = p13_df[p13_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p13(
                        ind_car=list(indices_carousel)[i],
                        nom_car=list(codigos_carousel)[i],
                        des_car=list(descripciones_carousel)[i],
                        cos_car=list(costo_carousel)[i],
                        sop_car=list(soportes_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_13()
        
    #retos SDQS
    elif pregunta_seleccionada=='p14':

        indices_carousel = p14_df[p14_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p14_df[p14_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_nom']
        act_1_carousel = p14_df[p14_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_1']
        act_2_carousel = p14_df[p14_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_2']
        act_3_carousel = p14_df[p14_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_3']
        act_4_carousel = p14_df[p14_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_4']
        act_5_carousel = p14_df[p14_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_5']
        acciones_carousel = p14_df[p14_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_post']
        soportes_carousel = p14_df[p14_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][pregunta_seleccionada])[0]
        except:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:

                if list(act_4_carousel)[0]==1:
                    act_4_otr = p14_df[p14_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_otr']
                else:
                    act_4_otr=['N/A' for x in range(len(indices_carousel)+1)]

                cards=[]                
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p14_15_16_19_20(
                        ind_car=list(indices_carousel)[i],
                        nom_car=list(codigos_carousel)[i],
                        act_1=list(act_1_carousel)[i],
                        act_2=list(act_2_carousel)[i],
                        act_3=list(act_3_carousel)[i],
                        act_4=list(act_4_carousel)[i],
                        act_5=list(act_5_carousel)[i],
                        act_otr=list(act_4_otr)[i],
                        acc_car=list(acciones_carousel)[i],
                        sop_car=list(soportes_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_14()
        
    #retos otros para ciudadanos
    elif pregunta_seleccionada=='p15':

        indices_carousel = p15_df[p15_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p15_df[p15_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_nom']
        act_1_carousel = p15_df[p15_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_1']
        act_2_carousel = p15_df[p15_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_2']
        act_3_carousel = p15_df[p15_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_3']
        act_4_carousel = p15_df[p15_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_4']
        act_5_carousel = p15_df[p15_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_5']
        acciones_carousel = p15_df[p15_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_post']
        soportes_carousel = p15_df[p15_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                if list(act_4_carousel)[0]==1:
                    act_4_otr = p15_df[p15_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_otr']
                else:
                    act_4_otr=['N/A' for x in range(len(indices_carousel)+1)]

                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p14_15_16_19_20(
                        ind_car=list(indices_carousel)[i],
                        nom_car=list(codigos_carousel)[i],
                        act_1=list(act_1_carousel)[i],
                        act_2=list(act_2_carousel)[i],
                        act_3=list(act_3_carousel)[i],
                        act_4=list(act_4_carousel)[i],
                        act_5=list(act_5_carousel)[i],
                        act_otr=list(act_4_otr)[i],
                        acc_car=list(acciones_carousel)[i],
                        sop_car=list(soportes_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_15()
        
    #retos por funcionarios/contratistas
    elif pregunta_seleccionada=='p16':

        indices_carousel = p16_df[p16_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p16_df[p16_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_rom']
        act_1_carousel = p16_df[p16_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_1']
        act_2_carousel = p16_df[p16_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_2']
        act_3_carousel = p16_df[p16_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_3']
        act_4_carousel = p16_df[p16_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_4']
        act_5_carousel = p16_df[p16_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_5']
        acciones_carousel = p16_df[p16_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_post']
        soportes_carousel = p16_df[p16_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']
        
        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""
        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                if list(act_4_carousel)[0]==1:
                    act_4_otr = p16_df[p16_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_otr']
                else:
                    act_4_otr=['N/A' for x in range(len(indices_carousel)+1)]

                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p14_15_16_19_20(
                        ind_car=list(indices_carousel)[i],
                        nom_car=list(codigos_carousel)[i],
                        act_1=list(act_1_carousel)[i],
                        act_2=list(act_2_carousel)[i],
                        act_3=list(act_3_carousel)[i],
                        act_4=list(act_4_carousel)[i],
                        act_5=list(act_5_carousel)[i],
                        act_otr=list(act_4_otr)[i],
                        acc_car=list(acciones_carousel)[i],
                        sop_car=list(soportes_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_16()
        
    #canales retos
    elif pregunta_seleccionada=='p17':
        
        indices_carousel = p17_df[p17_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p17_df[p17_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_can']
        usuarios_carousel = p17_df[p17_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_usr']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if indices_carousel.empty == True:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            cards=[]
            
            for i in range(len(indices_carousel)):
                
                card=card_p17_18_21_22(
                    ind_car=list(indices_carousel)[i],
                    nom_car=list(codigos_carousel)[i],
                    usr_car=list(usuarios_carousel)[i])
                cards.append(card)

            salida_respuesta_2023 = html.Div([
                    html.Div(children=cards,style=estilo)
                ])
            salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
            
        salida_criterio=criterio_17()
        
    #actividades retos
    elif pregunta_seleccionada=='p18':

        indices_carousel = p18_df[p18_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p18_df[p18_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act']
        usuarios_carousel = p18_df[p18_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_usr']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'p17'])[0]

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if indices_carousel.empty == True:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=["N/A"]
        else:
            cards=[]
            
            for i in range(len(indices_carousel)):
                
                card=card_p17_18_21_22(
                    ind_car=list(indices_carousel)[i],
                    nom_car=list(codigos_carousel)[i],
                    usr_car=list(usuarios_carousel)[i])
                cards.append(card)

            salida_respuesta_2023 = html.Div([
                    html.Div(children=cards,style=estilo)
                ])
            salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())

        salida_criterio=criterio_18()
        
    #ideas ciudadanos
    elif pregunta_seleccionada=='p19':

        indices_carousel = p19_df[p19_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p19_df[p19_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_nom']
        act_1_carousel = p19_df[p19_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_1']
        act_2_carousel = p19_df[p19_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_2']
        act_3_carousel = p19_df[p19_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_3']
        act_4_carousel = p19_df[p19_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_4']
        act_5_carousel = p19_df[p19_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_5']
        acciones_carousel = p19_df[p19_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_post']
        soportes_carousel = p19_df[p19_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']
        
        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                if list(act_4_carousel)[0]==1:
                    act_4_otr = p19_df[p19_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_otr']
                else:
                    act_4_otr=['N/A' for x in range(len(indices_carousel)+1)]

                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p14_15_16_19_20(
                        ind_car=list(indices_carousel)[i],
                        nom_car=list(codigos_carousel)[i],
                        act_1=list(act_1_carousel)[i],
                        act_2=list(act_2_carousel)[i],
                        act_3=list(act_3_carousel)[i],
                        act_4=list(act_4_carousel)[i],
                        act_5=list(act_5_carousel)[i],
                        act_otr=list(act_4_otr)[i],
                        acc_car=list(acciones_carousel)[i],
                        sop_car=list(soportes_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_19()
        
    #ideas funcionarios
    elif pregunta_seleccionada=='p20':

        indices_carousel = p20_df[p20_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p20_df[p20_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_nom']
        act_1_carousel = p20_df[p20_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_1']
        act_2_carousel = p20_df[p20_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_2']
        act_3_carousel = p20_df[p20_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_3']
        act_4_carousel = p20_df[p20_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_4']
        act_5_carousel = p20_df[p20_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_5']
        acciones_carousel = p20_df[p20_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_post']
        soportes_carousel = p20_df[p20_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']
        
        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                if list(act_4_carousel)[0]==1:
                    act_4_otr = p20_df[p20_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_otr']
                else:
                    act_4_otr=['N/A' for x in range(len(indices_carousel)+1)]

                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p14_15_16_19_20(
                        ind_car=list(indices_carousel)[i],
                        nom_car=list(codigos_carousel)[i],
                        act_1=list(act_1_carousel)[i],
                        act_2=list(act_2_carousel)[i],
                        act_3=list(act_3_carousel)[i],
                        act_4=list(act_4_carousel)[i],
                        act_5=list(act_5_carousel)[i],
                        act_otr=list(act_4_otr)[i],
                        acc_car=list(acciones_carousel)[i],
                        sop_car=list(soportes_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_20()
        
    #canales ideas
    elif pregunta_seleccionada=='p21':

        indices_carousel = p21_df[p21_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p21_df[p21_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_can']
        usuarios_carousel = p21_df[p21_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_usr']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if indices_carousel.empty == True:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            cards=[]
            
            for i in range(len(indices_carousel)):
                
                card=card_p17_18_21_22(
                    ind_car=list(indices_carousel)[i],
                    nom_car=list(codigos_carousel)[i],
                    usr_car=list(usuarios_carousel)[i])
                cards.append(card)

            salida_respuesta_2023 = html.Div([
                    html.Div(children=cards,style=estilo)
                ])
            salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
            
        salida_criterio=criterio_21()
        
    #actividades ideas
    elif pregunta_seleccionada=='p22':

        indices_carousel = p22_df[p22_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p22_df[p22_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act']
        usuarios_carousel = p22_df[p22_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_usr']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'p21'])[0]

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if indices_carousel.empty == True:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad='N/A'
        else:
            cards=[]
            
            for i in range(len(indices_carousel)):
                
                card=card_p17_18_21_22(
                    ind_car=list(indices_carousel)[i],
                    nom_car=list(codigos_carousel)[i],
                    usr_car=list(usuarios_carousel)[i])
                cards.append(card)

            salida_respuesta_2023 = html.Div([
                    html.Div(children=cards,style=estilo)
                ])
            salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
            
        salida_criterio=criterio_22()
        
    #innovaciones diseñadas
    elif pregunta_seleccionada=='p23':

        indices_carousel = p23_df[p23_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p23_df[p23_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_nom']
        descripciones_carousel = p23_df[p23_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_des']
        soportes_carousel = p23_df[p23_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']
        usr_1_carousel = p23_df[p23_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_usr/{pregunta_seleccionada}_usr_1']
        usr_2_carousel = p23_df[p23_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_usr/{pregunta_seleccionada}_usr_2']
        usr_3_carousel = p23_df[p23_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_usr/{pregunta_seleccionada}_usr_3']
        prototipado = p23_df[p23_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_pro']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']
        
        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                if list(prototipado)[0] == 'Si':
                    vali_usr_1_carousel = p23_df[p23_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_val/{pregunta_seleccionada}_val_1']
                    vali_usr_2_carousel = p23_df[p23_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_val/{pregunta_seleccionada}_val_2']
                    vali_usr_3_carousel = p23_df[p23_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_val/{pregunta_seleccionada}_val_3']
                else:
                    vali_usr_1_carousel = ['N/A' for x in range(len(indices_carousel)+1)]
                    vali_usr_2_carousel = ['N/A' for x in range(len(indices_carousel)+1)]
                    vali_usr_3_carousel = ['N/A' for x in range(len(indices_carousel)+1)]
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p23(
                        ind_car=list(indices_carousel)[i],
                        nom_car=list(codigos_carousel)[i],
                        des_car=list(descripciones_carousel)[i],
                        us1_car=list(usr_1_carousel)[i],
                        us2_car=list(usr_2_carousel)[i],
                        us3_car=list(usr_3_carousel)[i],
                        pro_car=list(prototipado)[i],
                        va1_car=list(vali_usr_1_carousel)[i],
                        va2_car=list(vali_usr_2_carousel)[i],
                        va3_car=list(vali_usr_3_carousel)[i],
                        sop_car=list(soportes_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_23()
        
    #eventos o formación
    elif pregunta_seleccionada=='p24':

        p24_1_indices_carousel = p24_1_df[p24_1_df['_submission__uuid'] == entidad_seleccionada]['_index']
        p24_1_codigos_carousel = p24_1_df[p24_1_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_1_nom']
        p24_1_descripciones_carousel = p24_1_df[p24_1_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_1_des']
        p24_1_impartio_carousel = p24_1_df[p24_1_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_1_imp']
        p24_1_asistentes_carousel = p24_1_df[p24_1_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_1_asi']
        p24_1_soportes_carousel = p24_1_df[p24_1_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_1_sop']

        p24_2_indices_carousel = p24_2_df[p24_2_df['_submission__uuid'] == entidad_seleccionada]['_index']
        p24_2_codigos_carousel = p24_2_df[p24_2_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_2_nom']
        p24_2_descripciones_carousel = p24_2_df[p24_2_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_2_des']
        p24_2_impartio_carousel = p24_2_df[p24_2_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_2_imp']
        p24_2_asistentes_carousel = p24_2_df[p24_2_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_2_asi']
        p24_2_soportes_carousel = p24_2_df[p24_2_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_2_sop']

        p24_3_indices_carousel = p24_3_df[p24_3_df['_submission__uuid'] == entidad_seleccionada]['_index']
        p24_3_codigos_carousel = p24_3_df[p24_3_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_3_nom']
        p24_3_descripciones_carousel = p24_3_df[p24_3_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_3_des']
        p24_3_impartio_carousel = p24_3_df[p24_3_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_3_imp']
        p24_3_asistentes_carousel = p24_3_df[p24_3_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_3_asi']
        p24_3_soportes_carousel = p24_3_df[p24_3_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_3_sop']

        p24_4_indices_carousel = p24_4_df[p24_4_df['_submission__uuid'] == entidad_seleccionada]['_index']
        p24_4_codigos_carousel = p24_4_df[p24_4_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_4_nom']
        p24_4_descripciones_carousel = p24_4_df[p24_4_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_4_des']
        p24_4_impartio_carousel = p24_4_df[p24_4_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_4_imp']
        p24_4_asistentes_carousel = p24_4_df[p24_4_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_4_asi']
        p24_4_soportes_carousel = p24_4_df[p24_4_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_4_sop']

        p24_5_indices_carousel = p24_5_df[p24_5_df['_submission__uuid'] == entidad_seleccionada]['_index']
        p24_5_codigos_carousel = p24_5_df[p24_5_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_5_nom']
        p24_5_descripciones_carousel = p24_5_df[p24_5_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_5_des']
        p24_5_impartio_carousel = p24_5_df[p24_5_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_5_imp']
        p24_5_asistentes_carousel = p24_5_df[p24_5_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_5_asi']
        p24_5_soportes_carousel = p24_5_df[p24_5_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_5_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""
        except:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':

            if p24_1_indices_carousel.empty == False:
                cards1=[]
                for i in range(len(p24_1_indices_carousel)):
                    
                    card=card_p24(
                        ind_car=list(p24_1_indices_carousel)[i],
                        nom_car=list(p24_1_codigos_carousel)[i],
                        des_car=list(p24_1_descripciones_carousel)[i],
                        imp_car=list(p24_1_impartio_carousel)[i],
                        asi_car=list(p24_1_asistentes_carousel)[i],
                        sop_car=list(p24_1_soportes_carousel)[i])
                    cards1.append(card)
            else:
                cards1=[html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)]),html.Br()]
            
            if p24_2_indices_carousel.empty == False:
                cards2=[]
                for i in range(len(p24_2_indices_carousel)):
                    
                    card=card_p24(
                        ind_car=list(p24_2_indices_carousel)[i],
                        nom_car=list(p24_2_codigos_carousel)[i],
                        des_car=list(p24_2_descripciones_carousel)[i],
                        imp_car=list(p24_2_impartio_carousel)[i],
                        asi_car=list(p24_2_asistentes_carousel)[i],
                        sop_car=list(p24_2_soportes_carousel)[i])
                    cards2.append(card)
            else:
                cards2=[html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)]),html.Br()]

            if p24_3_indices_carousel.empty == False:
                cards3=[]
                for i in range(len(p24_3_indices_carousel)):
                    
                    card=card_p24(
                        ind_car=list(p24_3_indices_carousel)[i],
                        nom_car=list(p24_3_codigos_carousel)[i],
                        des_car=list(p24_3_descripciones_carousel)[i],
                        imp_car=list(p24_3_impartio_carousel)[i],
                        asi_car=list(p24_3_asistentes_carousel)[i],
                        sop_car=list(p24_3_soportes_carousel)[i])
                    cards3.append(card)
            else:
                cards3=[html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)]),html.Br()]

            if p24_4_indices_carousel.empty == False:
                cards4=[]
                for i in range(len(p24_4_indices_carousel)):
                    
                    card=card_p24(
                        ind_car=list(p24_4_indices_carousel)[i],
                        nom_car=list(p24_4_codigos_carousel)[i],
                        des_car=list(p24_4_descripciones_carousel)[i],
                        imp_car=list(p24_4_impartio_carousel)[i],
                        asi_car=list(p24_4_asistentes_carousel)[i],
                        sop_car=list(p24_4_soportes_carousel)[i])
                    cards4.append(card)
            else:
                cards4=[html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)]),html.Br()]
            
            if p24_5_indices_carousel.empty == False:
                cards5=[]
                for i in range(len(p24_5_indices_carousel)):
                    
                    card=card_p24(
                        ind_car=list(p24_5_indices_carousel)[i],
                        nom_car=list(p24_5_codigos_carousel)[i],
                        des_car=list(p24_5_descripciones_carousel)[i],
                        imp_car=list(p24_5_impartio_carousel)[i],
                        asi_car=list(p24_5_asistentes_carousel)[i],
                        sop_car=list(p24_5_soportes_carousel)[i])
                    cards5.append(card)
            else:
                cards5=[html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)]),html.Br()]

            salida_respuesta_2023 = html.Div([
                    html.H5('Eventos Auspiciados y/o financiados directamente por esa entidad'),
                    html.Div(children=cards1,style=estilo),
                    html.H5('Eventos Auspiciados y/o financiados directamente por otras entidades'),
                    html.Div(children=cards2,style=estilo),
                    html.H5('Formación Auspiciada y/o financiada directamente por esa entidad'),
                    html.Div(children=cards3,style=estilo),
                    html.H5('Formación Auspiciada y/o financiada directamente por otras entidades'),
                    html.Div(children=cards4,style=estilo),
                    html.H5('Otras actividades de esa entidad'),
                    html.Div(children=cards5,style=estilo),
                ])
            
            salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_24()
        
    #promoción de una cultura de innovación
    elif pregunta_seleccionada=='p25':

        indices_carousel = p25_df[p25_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p25_df[p25_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_nom']
        descripciones_carousel = p25_df[p25_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_des']
        recomendacion_carousel = p25_df[p25_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_rec']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""
        except:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p25_p26(
                        ind_car=list(indices_carousel)[i],
                        nom_car=list(codigos_carousel)[i],
                        des_car=list(descripciones_carousel)[i],
                        rec_car=list(recomendacion_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_25()
        
    #espacios de experimentación
    elif pregunta_seleccionada=='p26':

        indices_carousel = p26_df[p26_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p26_df[p26_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_nom']
        descripciones_carousel = p26_df[p26_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_des']
        recomendacion_carousel = p26_df[p26_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_rec']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""
        except:
            salida_respuesta_2021 = 'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p25_p26(
                        ind_car=list(indices_carousel)[i],
                        nom_car=list(codigos_carousel)[i],
                        des_car=list(descripciones_carousel)[i],
                        rec_car=list(recomendacion_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_26()
        
    #unidades de innovación
    elif pregunta_seleccionada=='p27':

        indices_carousel = p27_df[p27_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p27_df[p27_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_nom']
        descripciones_carousel = p27_df[p27_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_des']
        tematica_carousel = p27_df[p27_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_des_001']
        tamano_carousel = p27_df[p27_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_c']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p27(
                        ind_car=list(indices_carousel)[i],
                        nom_car=list(codigos_carousel)[i],
                        des_car=list(descripciones_carousel)[i],
                        tem_car=list(tematica_carousel)[i],
                        tam_car=list(tamano_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_27()
        
    #implementación de innovaciones
    elif pregunta_seleccionada=='p28':

        indices_carousel = p28_df[p28_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p28_df[p28_df['_submission__uuid'] == entidad_seleccionada][f'nom_inno']
        implementado_carousel = p28_df[p28_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_imp']
        validado_carousel = p28_df[p28_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_val']
        metodologia_carousel = p28_df[p28_df['_submission__uuid'] == entidad_seleccionada][f'meto']
        beneficia_carousel = p28_df[p28_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_ben']
        ahorro_carousel = p28_df[p28_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_aho']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                if list(beneficia_carousel)[0]=='Si':
                    beneficiados_carousel = p28_df[p28_df['_submission__uuid'] == entidad_seleccionada][f'beneficiados']
                else:
                    beneficiados_carousel=['N/A' for x in range(len(indices_carousel)+1)]
                
                if list(ahorro_carousel)[0]=='Si':
                    ahorrado_carousel = p28_df[p28_df['_submission__uuid'] == entidad_seleccionada][f'recursos_ahorrados']
                else:
                    ahorrado_carousel=['N/A' for x in range(len(indices_carousel)+1)]
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p28(
                        ind_car=list(indices_carousel)[i],
                        nom_car=list(codigos_carousel)[i],
                        imp_car=list(implementado_carousel)[i],
                        val_car=list(validado_carousel)[i],
                        met_car=list(metodologia_carousel)[i],
                        ben_car=list(beneficia_carousel)[i],
                        aho_car=list(ahorro_carousel)[i],
                        b1_car=list(beneficiados_carousel)[i],
                        a1_car=list(ahorrado_carousel)[i],
                        )
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_28()
        
    #funcionarios formados
    elif pregunta_seleccionada=='p29':

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            form_2021 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]
        except Exception as e:
            form_2021 = 'N/A'

        salida_respuesta_2021=f"Funcionarios y contratistas formados: \n {form_2021}"

        total_2021_dis = respuestas_2023_df[f'p7_val_1'].median()
        total_2022_dis = respuestas_2023_df[f'p7_val_2'].median()
        formados_2021_dis = respuestas_2023_df[f'p29_val_1'].median()
        formados_2022_dis = respuestas_2023_df[f'p29_val_2'].median()
        
        total_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p7_val_1']
        total_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p7_val_2']
        formados_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p29_val_1']
        formados_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p29_val_2']

        cards=[]
        tipo_pregunta=['Funcionarios', 'Contratistas']

        rel_dist_tot = statistics.mean([float(total_2021_dis), float(total_2022_dis)])
        rel_dist_for = statistics.mean([float(formados_2021_dis), float(formados_2022_dis)])
        res_dis = rel_dist_for*100/rel_dist_tot

        rel_enti_tot = statistics.mean([float(total_2021_ent.iloc[0]), float(total_2022_ent.iloc[0])])
        rel_enti_for = statistics.mean([float(formados_2021_ent.iloc[0]), float(formados_2022_ent.iloc[0])])
        res_ent = rel_enti_for*100/rel_enti_tot
            
        card_2023=card_p29_p30(
            tip_preg=tipo_pregunta[0],

            can_2021_dis=total_2021_dis,
            can_2022_dis=total_2022_dis,
            can_med_dis=rel_dist_tot,
            fun_2021_dis=formados_2021_dis,
            fun_2022_dis=formados_2022_dis,
            fun_med_dis=rel_dist_for,
            res_dist=res_dis,

            can_2021_ent=list(total_2021_ent)[0],
            can_2022_ent=list(total_2022_ent)[0],
            can_med_ent=rel_enti_tot,
            fun_2021_ent=list(formados_2021_ent)[0],
            fun_2022_ent=list(formados_2022_ent)[0],
            fun_med_ent=rel_enti_for,
            res_enti=res_ent,
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])
        
        salida_criterio=criterio_29()
        salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        
    #contratistas formados
    elif pregunta_seleccionada=='p30':

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            form_2021 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]
        except Exception as e:
            form_2021 = 'N/A'

        salida_respuesta_2021=f"Funcionarios y contratistas formados: \n {form_2021}"

        total_2021_dis = respuestas_2023_df[f'p10_val_1'].median()
        total_2022_dis = respuestas_2023_df[f'p10_val_2'].median()
        formados_2021_dis = respuestas_2023_df[f'p30_val_1'].median()
        formados_2022_dis = respuestas_2023_df[f'p30_val_2'].median()
        
        total_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p10_val_1']
        total_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p10_val_2']
        formados_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p30_val_1']
        formados_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p30_val_2']

        cards=[]
        tipo_pregunta=['Funcionarios', 'Contratistas']

        rel_dist_tot = statistics.mean([float(total_2021_dis), float(total_2022_dis)])
        rel_dist_for = statistics.mean([float(formados_2021_dis), float(formados_2022_dis)])
        res_dis = rel_dist_for*100/rel_dist_tot

        rel_enti_tot = statistics.mean([float(total_2021_ent.iloc[0]), float(total_2022_ent.iloc[0])])
        rel_enti_for = statistics.mean([float(formados_2021_ent.iloc[0]), float(formados_2022_ent.iloc[0])])
        res_ent = rel_enti_for*100/rel_enti_tot
            
        card_2023=card_p29_p30(
            tip_preg=tipo_pregunta[1],

            can_2021_dis=total_2021_dis,
            can_2022_dis=total_2022_dis,
            can_med_dis=rel_dist_tot,
            fun_2021_dis=formados_2021_dis,
            fun_2022_dis=formados_2022_dis,
            fun_med_dis=rel_dist_for,
            res_dist=res_dis,

            can_2021_ent=list(total_2021_ent)[0],
            can_2022_ent=list(total_2022_ent)[0],
            can_med_ent=rel_enti_tot,
            fun_2021_ent=list(formados_2021_ent)[0],
            fun_2022_ent=list(formados_2022_ent)[0],
            fun_med_ent=rel_enti_for,
            res_enti=res_ent,
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])
        
        salida_criterio=criterio_30()
        salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        
    #acuerdos o actos en gestión del conocimiento
    elif pregunta_seleccionada=='p31':

        indices_carousel = p31_df[p31_df['_submission__uuid'] == entidad_seleccionada][f'_index']
        codigos_carousel = p31_df[p31_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_cod']
        nombres_carousel = p31_df[p31_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_nom']
        descripciones_carousel = p31_df[p31_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_des']
        soportes_carousel = p31_df[p31_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p31_p32(
                        ind_car=list(indices_carousel)[i],
                        cod_car=list(codigos_carousel)[i],
                        nom_car=list(nombres_carousel)[i],
                        des_car=list(descripciones_carousel)[i],
                        sop_car=list(soportes_carousel)[i],
                        )
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_31()
        
    #proyectos o lineas en gestión del conocimiento
    elif pregunta_seleccionada=='p32':

        indices_carousel = p32_df[p32_df['_submission__uuid'] == entidad_seleccionada][f'_index']
        codigos_carousel = p32_df[p32_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_cod']
        nombres_carousel = p32_df[p32_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_nom']
        descripciones_carousel = p32_df[p32_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_des']
        soportes_carousel = p32_df[p32_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p31_p32(
                        ind_car=list(indices_carousel)[i],
                        cod_car=list(codigos_carousel)[i],
                        nom_car=list(nombres_carousel)[i],
                        des_car=list(descripciones_carousel)[i],
                        sop_car=list(soportes_carousel)[i],
                        )
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_32()
        
    #sistematización de retos ciudadanos
    elif pregunta_seleccionada=='p33':

        indices_carousel = p33_df[p33_df['_submission__uuid'] == entidad_seleccionada][f'_index']
        codigos_carousel = p33_df[p33_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_cod']
        soportes_carousel = p33_df[p33_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p33_p34_p35_p36_p37_p38(
                        ind_car=list(indices_carousel)[i],
                        cod_car=list(codigos_carousel)[i],
                        sop_car=list(soportes_carousel)[i],
                        )
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_33()
        
    #sistematización de retos de funcionarios contratistas
    elif pregunta_seleccionada=='p34':

        indices_carousel = p34_df[p34_df['_submission__uuid'] == entidad_seleccionada][f'_index']
        codigos_carousel = p34_df[p34_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_cod']
        soportes_carousel = p34_df[p34_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p33_p34_p35_p36_p37_p38(
                        ind_car=list(indices_carousel)[i],
                        cod_car=list(codigos_carousel)[i],
                        sop_car=list(soportes_carousel)[i],
                        )
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_34()
        
    #sistematización ideas de ciudadanos
    elif pregunta_seleccionada=='p35':

        indices_carousel = p35_df[p35_df['_submission__uuid'] == entidad_seleccionada][f'_index']
        codigos_carousel = p35_df[p35_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_cod']
        soportes_carousel = p35_df[p35_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p33_p34_p35_p36_p37_p38(
                        ind_car=list(indices_carousel)[i],
                        cod_car=list(codigos_carousel)[i],
                        sop_car=list(soportes_carousel)[i],
                        )
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_35()
        
    #sistematización ideas de funcionarios contratistas
    elif pregunta_seleccionada=='p36':

        indices_carousel = p36_df[p36_df['_submission__uuid'] == entidad_seleccionada][f'_index']
        codigos_carousel = p36_df[p36_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_cod']
        soportes_carousel = p36_df[p36_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p33_p34_p35_p36_p37_p38(
                        ind_car=list(indices_carousel)[i],
                        cod_car=list(codigos_carousel)[i],
                        sop_car=list(soportes_carousel)[i],
                        )
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_36()
        
    #buenas prácticas y lecciones aprendidas en innovación
    elif pregunta_seleccionada=='p37':

        indices_carousel = p37_df[p37_df['_submission__uuid'] == entidad_seleccionada][f'_index']
        codigos_carousel = p37_df[p37_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_cod']
        soportes_carousel = p37_df[p37_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p33_p34_p35_p36_p37_p38(
                        ind_car=list(indices_carousel)[i],
                        cod_car=list(codigos_carousel)[i],
                        sop_car=list(soportes_carousel)[i],
                        )
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_37()
        
    #buenas prácticas y lecciones aprendidas generales
    elif pregunta_seleccionada=='p38':

        indices_carousel = p38_df[p38_df['_submission__uuid'] == entidad_seleccionada][f'_index']
        codigos_carousel = p38_df[p38_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_cod']
        soportes_carousel = p38_df[p38_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p33_p34_p35_p36_p37_p38(
                        ind_car=list(indices_carousel)[i],
                        cod_car=list(codigos_carousel)[i],
                        sop_car=list(soportes_carousel)[i],
                        )
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_38()
        
    #Monitoreo y seguimiento a innovaciones
    elif pregunta_seleccionada=='p39':

        indices_carousel = p39_df[p39_df['_submission__uuid'] == entidad_seleccionada][f'_index']
        codigos_carousel = p39_df[p39_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_cod']
        soportes_carousel = p39_df[p39_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p39(
                        ind_car=list(indices_carousel)[i],
                        cod_car=list(codigos_carousel)[i],
                        sop_car=list(soportes_carousel)[i],
                        )
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_39()
        
    #Cualquier caso no definido
    else:
        salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Caso no definido',
                    color="danger",
                    dismissable=True,
                    is_open=True)])


    if pregunta_seleccionada == 'p3':
        salida_iniciativas=[]

        try:
            salida_iniciativa_seleccionada=str(salida_iniciativas[0])
        except:
            salida_iniciativa_seleccionada='N/A'


        try:
            salida_criterios_entidad_seleccionado=str(salida_criterios_entidad[0])
        except:
            salida_criterios_entidad_seleccionado='N/A'

    elif pregunta_seleccionada == 'p4':
        salida_iniciativas=[]

        try:
            salida_iniciativa_seleccionada=str(salida_iniciativas[0])
        except:
            salida_iniciativa_seleccionada='N/A'


        try:
            salida_criterios_entidad_seleccionado=str(salida_criterios_entidad[0])
        except:
            salida_criterios_entidad_seleccionado='N/A'

    elif pregunta_seleccionada == 'p5':
        salida_iniciativas=[]

        try:
            salida_iniciativa_seleccionada=str(salida_iniciativas[0])
        except:
            salida_iniciativa_seleccionada='N/A'


        try:
            salida_criterios_entidad_seleccionado=str(salida_criterios_entidad[0])
        except:
            salida_criterios_entidad_seleccionado='N/A'

    elif pregunta_seleccionada == 'p6':
        salida_iniciativas=[]

        try:
            salida_iniciativa_seleccionada=str(salida_iniciativas[0])
        except:
            salida_iniciativa_seleccionada='N/A'


        try:
            salida_criterios_entidad_seleccionado=str(salida_criterios_entidad[0])
        except:
            salida_criterios_entidad_seleccionado='N/A'

    elif pregunta_seleccionada == 'p7':
        salida_iniciativas=[]

        try:
            salida_iniciativa_seleccionada=str(salida_iniciativas[0])
        except:
            salida_iniciativa_seleccionada='N/A'


        try:
            salida_criterios_entidad_seleccionado=str(salida_criterios_entidad[0])
        except:
            salida_criterios_entidad_seleccionado='N/A'

    elif pregunta_seleccionada == 'p8':
        salida_iniciativas=[]

        try:
            salida_iniciativa_seleccionada=str(salida_iniciativas[0])
        except:
            salida_iniciativa_seleccionada='N/A'


        try:
            salida_criterios_entidad_seleccionado=str(salida_criterios_entidad[0])
        except:
            salida_criterios_entidad_seleccionado='N/A'
    
    elif pregunta_seleccionada == 'p9':
        salida_iniciativas=[]

        try:
            salida_iniciativa_seleccionada=str(salida_iniciativas[0])
        except:
            salida_iniciativa_seleccionada='N/A'


        try:
            salida_criterios_entidad_seleccionado=str(salida_criterios_entidad[0])
        except:
            salida_criterios_entidad_seleccionado='N/A'

    elif pregunta_seleccionada == 'p10':
        salida_iniciativas=[]

        try:
            salida_iniciativa_seleccionada=str(salida_iniciativas[0])
        except:
            salida_iniciativa_seleccionada='N/A'


        try:
            salida_criterios_entidad_seleccionado=str(salida_criterios_entidad[0])
        except:
            salida_criterios_entidad_seleccionado='N/A'

    elif pregunta_seleccionada == 'p11':
        salida_iniciativas=[]

        try:
            salida_iniciativa_seleccionada=str(salida_iniciativas[0])
        except:
            salida_iniciativa_seleccionada='N/A'


        try:
            salida_criterios_entidad_seleccionado=str(salida_criterios_entidad[0])
        except:
            salida_criterios_entidad_seleccionado='N/A'

    elif pregunta_seleccionada == 'p12':
        salida_iniciativas=[]

        try:
            salida_iniciativa_seleccionada=str(salida_iniciativas[0])
        except:
            salida_iniciativa_seleccionada='N/A'


        try:
            salida_criterios_entidad_seleccionado=str(salida_criterios_entidad[0])
        except:
            salida_criterios_entidad_seleccionado='N/A'

    elif pregunta_seleccionada == 'p24':
        salida_iniciativas=list(itertools.chain(p24_1_indices_carousel,p24_2_indices_carousel,p24_3_indices_carousel,p24_4_indices_carousel))

        try:
            salida_iniciativa_seleccionada=str(salida_iniciativas[0])
        except:
            salida_iniciativa_seleccionada='N/A'


        try:
            salida_criterios_entidad_seleccionado=str(salida_criterios_entidad[0])
        except:
            salida_criterios_entidad_seleccionado='N/A'

    elif pregunta_seleccionada == 'p29':
        salida_iniciativas=[]

        try:
            salida_iniciativa_seleccionada=str(salida_iniciativas[0])
        except:
            salida_iniciativa_seleccionada='N/A'


        try:
            salida_criterios_entidad_seleccionado=str(salida_criterios_entidad[0])
        except:
            salida_criterios_entidad_seleccionado='N/A'

    elif pregunta_seleccionada == 'p30':
        salida_iniciativas=[]

        try:
            salida_iniciativa_seleccionada=str(salida_iniciativas[0])
        except:
            salida_iniciativa_seleccionada='N/A'


        try:
            salida_criterios_entidad_seleccionado=str(salida_criterios_entidad[0])
        except:
            salida_criterios_entidad_seleccionado='N/A'

    else:
        salida_iniciativas=list(indices_carousel)
        
        try:
            salida_iniciativa_seleccionada=str(salida_iniciativas[0])
        except:
            salida_iniciativa_seleccionada='N/A'


        try:
            salida_criterios_entidad_seleccionado=str(salida_criterios_entidad[0])
        except:
            salida_criterios_entidad_seleccionado='N/A'

    return pregunta,salida_criterio,salida_respuesta_2021,salida_nota_2021,salida_max_2021,salida_respuesta_2023,salida_iniciativas,salida_iniciativa_seleccionada,salida_criterios_entidad,salida_criterios_entidad_seleccionado

#Callback descarga respuestas 2023
@dash.callback(
    Output("download_respuestas_2023", "data"),
    Input("btn_download_respuestas_2023", "n_clicks"),
    prevent_initial_call=True,
)
def descargar_2023(n_clicks):
    path =f'./files/respuestas/2023/respuestas_2023.xlsx'

    return dcc.send_file(path)

#Callback descarga resultados 2023
@dash.callback(
    Output("download_resultados_2023", "data"),
    Input("btn_download_resultados_2023", "n_clicks"),
    prevent_initial_call=True,
)
def descargar_2023(n_clicks):
    path =f'./files/resultados/2023/resultados_2023.xlsx'

    return dcc.send_file(path)

#Callback descarga individuales
@dash.callback(
    Output("download_repeats", "data"),
    Input("btn_download_repeats", "n_clicks"),
    prevent_initial_call=True,
)
def descargar_individuales(n_clicks):
    path =f'./files/separadas/'
    loczip ='./files/exports/bucles.zip'

    zf = zipfile.ZipFile(loczip, "w")
    for dirname, subdirs, files in os.walk(path):
        zf.write(dirname)
        for filename in files:
            zf.write(os.path.join(dirname, filename))
    zf.close()

    return dcc.send_file(loczip)