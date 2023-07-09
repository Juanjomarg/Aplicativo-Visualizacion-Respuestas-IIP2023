from assets.libraries import *

LOGO_LAB='./static/logolab.png'
LOGO_IIP='./static/logoiip.png'
PREGUNTAS_TODAS=    ['p1','p2','p3','p4','p5','p6','p7','p8','p9','p10','p11','p12','p13','p14','p15','p16','p17','p18','p19','p20','p21','p22','p23','p24','p25','p26','p27','p28','p29','p30','p31','p32','p33','p34','p35','p36','p37','p38','p39']
PREGUNTAS_BINARIAS= ['p1','p2','p13','p14','p15','p16',            'p19','p20',            'p23','p24','p25','p26','p27','p28','p29','p30','p31','p32','p33','p34','p35','p36','p37','p38','p39']
PREGUNTAS_BUCLES=   ['p1','p2','p13','p14','p15','p16','p17','p18','p19','p20','p21','p22','p23','p24_1','p24_2','p24_3','p24_4','p24_5','p25','p26','p27','p28',            'p31','p32','p33','p34','p35','p36','p37','p38','p39']
ENTIDAD_INICIAL='Universidad Distrital Francisco Jose De Caldas'
PREGUNTA_INICIAL='p1'


preguntas_df=pd.read_excel('./files/preguntas/leyenda_columnas.xlsx')


respuestas_2021_df=pd.read_excel('./files/respuestas/2021/respuestas_2021.xlsx')
respuestas_2023_df=pd.read_excel('./files/respuestas/2023/respuestas_2023.xlsx')


resultados_2021_df=pd.read_excel('./files/resultados/2021/resultados_2021.xlsx')
resultados_2023_df=pd.read_excel('./files/resultados/2023/resultados_2023.xlsx')


p1_df=pd.read_excel('./files/separadas/repeat_p1.xlsx')
p2_df=pd.read_excel('./files/separadas/repeat_p2.xlsx')
p13_df=pd.read_excel('./files/separadas/repeat_p13.xlsx')
p14_df=pd.read_excel('./files/separadas/repeat_p14.xlsx')
p15_df=pd.read_excel('./files/separadas/repeat_p15.xlsx')
p16_df=pd.read_excel('./files/separadas/repeat_p16.xlsx')
p17_df=pd.read_excel('./files/separadas/repeat_p17.xlsx')
p18_df=pd.read_excel('./files/separadas/repeat_p18.xlsx')
p19_df=pd.read_excel('./files/separadas/repeat_p19.xlsx')
p20_df=pd.read_excel('./files/separadas/repeat_p20.xlsx')
p21_df=pd.read_excel('./files/separadas/repeat_p21.xlsx')
p22_df=pd.read_excel('./files/separadas/repeat_p22.xlsx')
p23_df=pd.read_excel('./files/separadas/repeat_p23.xlsx')
p24_1_df=pd.read_excel('./files/separadas/repeat_p24_1.xlsx')
p24_2_df=pd.read_excel('./files/separadas/repeat_p24_2.xlsx')
p24_3_df=pd.read_excel('./files/separadas/repeat_p24_3.xlsx')
p24_4_df=pd.read_excel('./files/separadas/repeat_p24_4.xlsx')
p24_5_df=pd.read_excel('./files/separadas/repeat_p24_5.xlsx')
p25_df=pd.read_excel('./files/separadas/repeat_p25.xlsx')
p26_df=pd.read_excel('./files/separadas/repeat_p26.xlsx')
p27_df=pd.read_excel('./files/separadas/repeat_p27.xlsx')
p28_df=pd.read_excel('./files/separadas/repeat_p28.xlsx')
p31_df=pd.read_excel('./files/separadas/repeat_p31.xlsx')
p32_df=pd.read_excel('./files/separadas/repeat_p32.xlsx')
p33_df=pd.read_excel('./files/separadas/repeat_p33.xlsx')
p34_df=pd.read_excel('./files/separadas/repeat_p34.xlsx')
p35_df=pd.read_excel('./files/separadas/repeat_p35.xlsx')
p36_df=pd.read_excel('./files/separadas/repeat_p36.xlsx')
p37_df=pd.read_excel('./files/separadas/repeat_p37.xlsx')
p38_df=pd.read_excel('./files/separadas/repeat_p38.xlsx')
p39_df=pd.read_excel('./files/separadas/repeat_p39.xlsx')

entidades_2023=list(respuestas_2023_df['entidad'].sort_values())

CRITS_PREGUNTAS_BASE={
    'p1':{},
    'p2':{'c1':0,'c2':0,'c3':0},
    'p3':{},
    'p4':{'c1':0,'c2':0},
    'p5':{},
    'p6':{'c1':0,'c2':0},
    'p7':{},
    'p8':{'c1':0,'c2':0},
    'p9':{},
    'p10':{},
    'p11':{'c1':0,'c2':0},
    'p12':{},
    'p13':{'c1':0,'c2':0},
    'p14':{'c1':0,'c2':0},
    'p15':{'c1':0,'c2':0},
    'p16':{'c1':0,'c2':0},
    'p17':{'c1':0,'c2':0},
    'p18':{'c1':0,'c2':0},
    'p19':{'c1':0,'c2':0},
    'p20':{'c1':0,'c2':0},
    'p21':{'c1':0,'c2':0},
    'p22':{'c1':0,'c2':0},
    'p23':{'c1':['c1'],'c2':['c2'],'c3':['c3'],'c4':['c4']},
    'p24':{'c1':0,'c2':0,'c3':0,'c4':0},
    'p25':{'c1':0,'c2':0},
    'p26':{'c1':0,'c2':0},
    'p27':{'c1':0},
    'p28':{'c1':0,'c2':0,'c3':0,'c4':['c4'],'c5':['c5']},
    'p29':{'c1':0},
    'p30':{'c1':0},
    'p31':{},
    'p32':{'c1':0,'c2':0},
    'p33':{'c1':0,'c2':0},
    'p34':{'c1':0,'c2':0},
    'p35':{'c1':0,'c2':0},
    'p36':{'c1':0,'c2':0},
    'p37':{'c1':0,'c2':0},
    'p38':{'c1':0,'c2':0},
    'p39':{'c1':0,'c2':0},
    }

"""
def backup(pregunta_seleccionada):

    if pregunta_seleccionada=='p1':
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

    elif pregunta_seleccionada=='p2':
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                        html.Th(f'c3'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'],2),rowSpan=2),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'],2),rowSpan=2),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c3'],2)),
                    ],
                    ),
                    html.Tr([
                        html.Td(p2_df.loc[p2_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

    elif pregunta_seleccionada=='p3':
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

    elif pregunta_seleccionada=='p4':
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
        return tabla_criterios

    elif pregunta_seleccionada=='p5':
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

    elif pregunta_seleccionada=='p6':
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
        return tabla_criterios

    elif pregunta_seleccionada=='p7':
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

    elif pregunta_seleccionada=='p8':
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
        return tabla_criterios
        
    elif pregunta_seleccionada=='p9':
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

    elif pregunta_seleccionada=='p10':
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

    elif pregunta_seleccionada=='p11':
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
        return tabla_criterios

    elif pregunta_seleccionada=='p12':
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

    elif pregunta_seleccionada=='p13':
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
                        html.Td(p13_df.loc[p13_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

    elif pregunta_seleccionada=='p14':
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
                        html.Td(p14_df.loc[p14_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

    elif pregunta_seleccionada=='p15':
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
                        html.Td(p15_df.loc[p15_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

    elif pregunta_seleccionada=='p16':
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
                        html.Td(p16_df.loc[p16_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

    elif pregunta_seleccionada=='p17':
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
                        html.Td(p17_df.loc[p17_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

    elif pregunta_seleccionada=='p18':
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
                        html.Td(p18_df.loc[p18_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

    elif pregunta_seleccionada=='p19':
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
                        html.Td(p19_df.loc[p19_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

    elif pregunta_seleccionada=='p20':
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
                        html.Td(p20_df.loc[p20_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

    elif pregunta_seleccionada=='p21':
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
                        html.Td(p21_df.loc[p21_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

    elif pregunta_seleccionada=='p22':
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
                        html.Td(p22_df.loc[p22_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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
        return tabla_criterios

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
        return tabla_criterios

    elif pregunta_seleccionada=='p25':
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
                        html.Td(p25_df.loc[p25_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

    elif pregunta_seleccionada=='p26':
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
                        html.Td(p26_df.loc[p26_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

    elif pregunta_seleccionada=='p27':
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
                        html.Td(p27_df.loc[p27_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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
                        html.Th(f'c5'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'],2),rowSpan=2),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'],2),rowSpan=2),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c3'],2),rowSpan=2),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c4'],2)),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c5'],2)),
                    ],
                    ),
                    html.Tr([
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
        return tabla_criterios

    elif pregunta_seleccionada=='p29':
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
        return tabla_criterios

    elif pregunta_seleccionada=='p30':
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
        return tabla_criterios

    elif pregunta_seleccionada=='p31':
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

    elif pregunta_seleccionada=='p32':
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
                        html.Td(p32_df.loc[p32_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

    elif pregunta_seleccionada=='p33':
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
                        html.Td(p33_df.loc[p33_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

    elif pregunta_seleccionada=='p34':
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
                        html.Td(p34_df.loc[p34_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

    elif pregunta_seleccionada=='p35':
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
                        html.Td(p35_df.loc[p35_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

    elif pregunta_seleccionada=='p36':
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
                        html.Td(p36_df.loc[p36_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

    elif pregunta_seleccionada=='p37':
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
                        html.Td(p37_df.loc[p37_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

    elif pregunta_seleccionada=='p38':
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
                        html.Td(p38_df.loc[p38_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

    elif pregunta_seleccionada=='p39':
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
                        html.Td(p39_df.loc[p39_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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
"""

"""
def keep(clicks,entidad_seleccionada,pregunta_seleccionada,iniciativa_seleccionada,criterio_seleccionado,criterio_seleccionado_bucle,criterios_disponibles_bucle,nota):

    def tabla_c(pregunta_seleccionada):

        if pregunta_seleccionada=='p1':
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

        elif pregunta_seleccionada=='p2':
            tabla_criterios=html.Div(children=[
                dbc.Table(
                    children=[
                    html.Thead(children=[
                        html.Tr([
                            html.Th(f'c1'),
                            html.Th(f'c2'),
                            html.Th(f'c3'),
                        ],
                        )                  
                    ]),

                    html.Tbody([
                        html.Tr([
                            html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'],2),rowSpan=2),
                            html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'],2),rowSpan=2),
                            html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c3'],2)),
                        ],
                        ),
                        html.Tr([
                            html.Td(p2_df.loc[p2_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

        elif pregunta_seleccionada=='p3':
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

        elif pregunta_seleccionada=='p4':
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
            return tabla_criterios

        elif pregunta_seleccionada=='p5':
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

        elif pregunta_seleccionada=='p6':
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
            return tabla_criterios

        elif pregunta_seleccionada=='p7':
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

        elif pregunta_seleccionada=='p8':
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
            return tabla_criterios
            
        elif pregunta_seleccionada=='p9':
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

        elif pregunta_seleccionada=='p10':
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

        elif pregunta_seleccionada=='p11':
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
            return tabla_criterios

        elif pregunta_seleccionada=='p12':
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

        elif pregunta_seleccionada=='p13':
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
                            html.Td(p13_df.loc[p13_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

        elif pregunta_seleccionada=='p14':
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
                            html.Td(p14_df.loc[p14_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

        elif pregunta_seleccionada=='p15':
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
                            html.Td(p15_df.loc[p15_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

        elif pregunta_seleccionada=='p16':
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
                            html.Td(p16_df.loc[p16_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

        elif pregunta_seleccionada=='p17':
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
                            html.Td(p17_df.loc[p17_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

        elif pregunta_seleccionada=='p18':
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
                            html.Td(p18_df.loc[p18_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

        elif pregunta_seleccionada=='p19':
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
                            html.Td(p19_df.loc[p19_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

        elif pregunta_seleccionada=='p20':
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
                            html.Td(p20_df.loc[p20_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

        elif pregunta_seleccionada=='p21':
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
                            html.Td(p21_df.loc[p21_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

        elif pregunta_seleccionada=='p22':
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
                            html.Td(p22_df.loc[p22_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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
            return tabla_criterios

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
            return tabla_criterios

        elif pregunta_seleccionada=='p25':
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
                            html.Td(p25_df.loc[p25_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

        elif pregunta_seleccionada=='p26':
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
                            html.Td(p26_df.loc[p26_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

        elif pregunta_seleccionada=='p27':
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
                            html.Td(p27_df.loc[p27_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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
                            html.Th(f'c5'),
                        ],
                        )                  
                    ]),

                    html.Tbody([
                        html.Tr([
                            html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'],2),rowSpan=2),
                            html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'],2),rowSpan=2),
                            html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c3'],2),rowSpan=2),
                            html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c4'],2)),
                            html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c5'],2)),
                        ],
                        ),
                        html.Tr([
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
            return tabla_criterios

        elif pregunta_seleccionada=='p29':
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
            return tabla_criterios

        elif pregunta_seleccionada=='p30':
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
            return tabla_criterios

        elif pregunta_seleccionada=='p31':
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

        elif pregunta_seleccionada=='p32':
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
                            html.Td(p32_df.loc[p32_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

        elif pregunta_seleccionada=='p33':
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
                            html.Td(p33_df.loc[p33_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

        elif pregunta_seleccionada=='p34':
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
                            html.Td(p34_df.loc[p34_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

        elif pregunta_seleccionada=='p35':
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
                            html.Td(p35_df.loc[p35_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

        elif pregunta_seleccionada=='p36':
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
                            html.Td(p36_df.loc[p36_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

        elif pregunta_seleccionada=='p37':
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
                            html.Td(p37_df.loc[p37_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

        elif pregunta_seleccionada=='p38':
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
                            html.Td(p38_df.loc[p38_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

        elif pregunta_seleccionada=='p39':
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
                            html.Td(p39_df.loc[p39_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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
        tabla_criterios=tabla_c(pregunta_seleccionada)

    elif pregunta_seleccionada=='p2':
        p2_df=pd.read_excel('./files/separadas/repeat_p2.xlsx')
        resultados_2023_df=pd.read_excel('./files/resultados/2023/resultados_2023.xlsx')
        respuestas_2023_df=pd.read_excel('./files/respuestas/2023/respuestas_2023.xlsx')

        tabla_criterios=tabla_c(pregunta_seleccionada)
        if criterio_seleccionado=='c1':  
            CRITS_PREGUNTAS_BASE[pregunta_seleccionada][criterio_seleccionado]=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota
        
        elif criterio_seleccionado=='c2':
            CRITS_PREGUNTAS_BASE[pregunta_seleccionada][criterio_seleccionado]=respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota
        
        elif criterio_seleccionado=='c3':
            
            #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO
            c3=p2_df.loc[p2_df['_index']==iniciativa_seleccionada, 'nota_iniciativa']=nota
            
            CRITS_PREGUNTAS_BASE[pregunta_seleccionada][criterio_seleccionado],nota_entidad = round(p2_df.loc[p2_df['_submission__uuid']==entidad_seleccionada]['nota_iniciativa'].mean(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c3'] = nota_entidad
            
        else:
            pass

        nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c3'].sum().sum(),2)
        respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
        resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta
        tabla_criterios=tabla_c(pregunta_seleccionada)
        p2_df.to_excel(f'./files/separadas/repeat_p2.xlsx',index=False)
        respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
        resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

    elif pregunta_seleccionada=='p3':
        tabla_criterios=tabla_c(pregunta_seleccionada)

    elif pregunta_seleccionada=='p4':
        resultados_2023_df=pd.read_excel('./files/resultados/2023/resultados_2023.xlsx')
        respuestas_2023_df=pd.read_excel('./files/respuestas/2023/respuestas_2023.xlsx')
        
        tabla_criterios=tabla_c(pregunta_seleccionada)
        if criterio_seleccionado=='c1':  
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota

        elif criterio_seleccionado=='c2':
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota
            
        else:
            pass
        nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
        respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
        resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta
        tabla_criterios=tabla_c(pregunta_seleccionada)
        respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
        resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

    elif pregunta_seleccionada=='p5':
        tabla_criterios=tabla_c(pregunta_seleccionada)

    elif pregunta_seleccionada=='p6':
        resultados_2023_df=pd.read_excel('./files/resultados/2023/resultados_2023.xlsx')
        respuestas_2023_df=pd.read_excel('./files/respuestas/2023/respuestas_2023.xlsx')
        
        tabla_criterios=tabla_c(pregunta_seleccionada)
        if criterio_seleccionado=='c1':  
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota

        elif criterio_seleccionado=='c2':
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota
            
        else:
            pass

        nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
        respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
        resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta
        tabla_criterios=tabla_c(pregunta_seleccionada)
        respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
        resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

    elif pregunta_seleccionada=='p7':
        tabla_criterios=tabla_c(pregunta_seleccionada)

    elif pregunta_seleccionada=='p8':
        resultados_2023_df=pd.read_excel('./files/resultados/2023/resultados_2023.xlsx')
        respuestas_2023_df=pd.read_excel('./files/respuestas/2023/respuestas_2023.xlsx')

        tabla_criterios=tabla_c(pregunta_seleccionada)
        if criterio_seleccionado=='c1':  
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota

        elif criterio_seleccionado=='c2':
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota
            
        else:
            pass

        nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
        respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
        resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta
        tabla_criterios=tabla_c(pregunta_seleccionada)
        respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
        resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

    elif pregunta_seleccionada=='p9':
        tabla_criterios=tabla_c(pregunta_seleccionada)

    elif pregunta_seleccionada=='p10':
        tabla_criterios=tabla_c(pregunta_seleccionada)

    elif pregunta_seleccionada=='p11':
        resultados_2023_df=pd.read_excel('./files/resultados/2023/resultados_2023.xlsx')
        respuestas_2023_df=pd.read_excel('./files/respuestas/2023/respuestas_2023.xlsx')

        tabla_criterios=tabla_c(pregunta_seleccionada)
        if criterio_seleccionado=='c1':  
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota

        elif criterio_seleccionado=='c2':
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota
            
        else:
            pass

        nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
        respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
        resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta
        tabla_criterios=tabla_c(pregunta_seleccionada)
        respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
        resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

    elif pregunta_seleccionada=='p12':
        tabla_criterios=tabla_c(pregunta_seleccionada)

    elif pregunta_seleccionada=='p13':
        p13_df=pd.read_excel('./files/separadas/repeat_p13.xlsx')
        resultados_2023_df=pd.read_excel('./files/resultados/2023/resultados_2023.xlsx')
        respuestas_2023_df=pd.read_excel('./files/respuestas/2023/respuestas_2023.xlsx')
        
        tabla_criterios=tabla_c(pregunta_seleccionada)
        if criterio_seleccionado=='c1':   
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota
        
        elif criterio_seleccionado=='c2':
            
            #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
            p13_df.loc[p13_df['_index']==iniciativa_seleccionada, 'nota_iniciativa']=nota

            nota_entidad = round(p13_df.loc[p13_df['_submission__uuid']==entidad_seleccionada]['nota_iniciativa'].mean(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota_entidad

        else:
            pass

        nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
        respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
        resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta
        tabla_criterios=tabla_c(pregunta_seleccionada)
        p13_df.to_excel(f'./files/separadas/repeat_p13.xlsx',index=False)
        respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
        resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

    elif pregunta_seleccionada=='p14':
        p14_df=pd.read_excel('./files/separadas/repeat_p14.xlsx')
        resultados_2023_df=pd.read_excel('./files/resultados/2023/resultados_2023.xlsx')
        respuestas_2023_df=pd.read_excel('./files/respuestas/2023/respuestas_2023.xlsx')

        tabla_criterios=tabla_c(pregunta_seleccionada)
        if criterio_seleccionado=='c1':  

            #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
            p14_df.loc[p14_df['_index']==iniciativa_seleccionada, 'nota_iniciativa']=nota

            nota_entidad = round(p14_df.loc[p14_df['_submission__uuid']==entidad_seleccionada]['nota_iniciativa'].mean(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota_entidad

        elif criterio_seleccionado=='c2':
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota

        else:
            pass

        nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
        respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
        resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta
        tabla_criterios=tabla_c(pregunta_seleccionada)
        p14_df.to_excel(f'./files/separadas/repeat_p14.xlsx',index=False)
        respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
        resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

    elif pregunta_seleccionada=='p15':
        p15_df=pd.read_excel('./files/separadas/repeat_p15.xlsx')
        resultados_2023_df=pd.read_excel('./files/resultados/2023/resultados_2023.xlsx')
        respuestas_2023_df=pd.read_excel('./files/respuestas/2023/respuestas_2023.xlsx')

        tabla_criterios=tabla_c(pregunta_seleccionada)
        if criterio_seleccionado=='c1':  

            #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
            p15_df.loc[p15_df['_index']==iniciativa_seleccionada, 'nota_iniciativa']=nota
            
            nota_entidad = round(p15_df.loc[p15_df['_submission__uuid']==entidad_seleccionada]['nota_iniciativa'].mean(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota_entidad

        elif criterio_seleccionado=='c2':
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota
            
        else:
            pass

        nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
        respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
        resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta
        tabla_criterios=tabla_c(pregunta_seleccionada)
        p15_df.to_excel(f'./files/separadas/repeat_p15.xlsx',index=False)
        respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
        resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

    elif pregunta_seleccionada=='p16':
        p16_df=pd.read_excel('./files/separadas/repeat_p16.xlsx')
        resultados_2023_df=pd.read_excel('./files/resultados/2023/resultados_2023.xlsx')
        respuestas_2023_df=pd.read_excel('./files/respuestas/2023/respuestas_2023.xlsx')

        tabla_criterios=tabla_c(pregunta_seleccionada)
        if criterio_seleccionado=='c1':  

            #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
            p16_df.loc[p16_df['_index']==iniciativa_seleccionada, 'nota_iniciativa']=nota
    
            nota_entidad = round(p16_df.loc[p16_df['_submission__uuid']==entidad_seleccionada]['nota_iniciativa'].mean(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota_entidad                

        elif criterio_seleccionado=='c2':
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota

        else:
            pass

        nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
        respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
        resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta
        tabla_criterios=tabla_c(pregunta_seleccionada)
        p16_df.to_excel(f'./files/separadas/repeat_p16.xlsx',index=False)
        respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
        resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

    elif pregunta_seleccionada=='p17':
        p17_df=pd.read_excel('./files/separadas/repeat_p17.xlsx')
        resultados_2023_df=pd.read_excel('./files/resultados/2023/resultados_2023.xlsx')
        respuestas_2023_df=pd.read_excel('./files/respuestas/2023/respuestas_2023.xlsx')

        tabla_criterios=tabla_c(pregunta_seleccionada)
        if criterio_seleccionado=='c1':  

            #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
            p17_df.loc[p17_df['_index']==iniciativa_seleccionada, 'nota_iniciativa']=nota
    
            nota_entidad = round(p17_df.loc[p17_df['_submission__uuid']==entidad_seleccionada]['nota_iniciativa'].mean(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota_entidad                

        elif criterio_seleccionado=='c2':
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota
            
        else:
            pass

        nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
        respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
        resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta
        tabla_criterios=tabla_c(pregunta_seleccionada)
        p17_df.to_excel(f'./files/separadas/repeat_p17.xlsx',index=False)
        respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
        resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

    elif pregunta_seleccionada=='p18':
        p18_df=pd.read_excel('./files/separadas/repeat_p18.xlsx')
        resultados_2023_df=pd.read_excel('./files/resultados/2023/resultados_2023.xlsx')
        respuestas_2023_df=pd.read_excel('./files/respuestas/2023/respuestas_2023.xlsx')

        tabla_criterios=tabla_c(pregunta_seleccionada)
        if criterio_seleccionado=='c1':  

            #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
            p18_df.loc[p18_df['_index']==iniciativa_seleccionada, 'nota_iniciativa']=nota

            nota_entidad = round(p18_df.loc[p18_df['_submission__uuid']==entidad_seleccionada]['nota_iniciativa'].mean(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota_entidad

        elif criterio_seleccionado=='c2':
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota
            
        else:
            pass

        nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
        respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
        resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta
        tabla_criterios=tabla_c(pregunta_seleccionada)
        p18_df.to_excel(f'./files/separadas/repeat_p18.xlsx',index=False)
        respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
        resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

    elif pregunta_seleccionada=='p19':
        p19_df=pd.read_excel('./files/separadas/repeat_p19.xlsx')
        resultados_2023_df=pd.read_excel('./files/resultados/2023/resultados_2023.xlsx')
        respuestas_2023_df=pd.read_excel('./files/respuestas/2023/respuestas_2023.xlsx')

        tabla_criterios=tabla_c(pregunta_seleccionada)
        if criterio_seleccionado=='c1':  
            #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
            p19_df.loc[p19_df['_index']==iniciativa_seleccionada, 'nota_iniciativa']=nota

            nota_entidad = round(p19_df.loc[p19_df['_submission__uuid']==entidad_seleccionada]['nota_iniciativa'].mean(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota_entidad

        elif criterio_seleccionado=='c2':
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota
            
        else:
            pass


        nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
        respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
        resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta
        tabla_criterios=tabla_c(pregunta_seleccionada)
        p19_df.to_excel(f'./files/separadas/repeat_p19.xlsx',index=False)
        respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
        resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

    elif pregunta_seleccionada=='p20':
        p20_df=pd.read_excel('./files/separadas/repeat_p20.xlsx')
        resultados_2023_df=pd.read_excel('./files/resultados/2023/resultados_2023.xlsx')
        respuestas_2023_df=pd.read_excel('./files/respuestas/2023/respuestas_2023.xlsx')

        tabla_criterios=tabla_c(pregunta_seleccionada)
        if criterio_seleccionado=='c1':  

            #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
            p20_df.loc[p20_df['_index']==iniciativa_seleccionada, 'nota_iniciativa']=nota

            nota_entidad = round(p20_df.loc[p20_df['_submission__uuid']==entidad_seleccionada]['nota_iniciativa'].mean(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota_entidad

        elif criterio_seleccionado=='c2':
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota
            
        else:
            pass

        nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
        respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
        resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta
        tabla_criterios=tabla_c(pregunta_seleccionada)
        p20_df.to_excel(f'./files/separadas/repeat_p20.xlsx',index=False)
        respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
        resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

    elif pregunta_seleccionada=='p21':
        p21_df=pd.read_excel('./files/separadas/repeat_p21.xlsx')
        resultados_2023_df=pd.read_excel('./files/resultados/2023/resultados_2023.xlsx')
        respuestas_2023_df=pd.read_excel('./files/respuestas/2023/respuestas_2023.xlsx')

        tabla_criterios=tabla_c(pregunta_seleccionada)
        if criterio_seleccionado=='c1':  

            #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
            p21_df.loc[p21_df['_index']==iniciativa_seleccionada, 'nota_iniciativa']=nota

            nota_entidad = round(p21_df.loc[p21_df['_submission__uuid']==entidad_seleccionada]['nota_iniciativa'].mean(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota_entidad

        elif criterio_seleccionado=='c2':
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota
            
        else:
            pass

        nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
        respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
        resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta
        tabla_criterios=tabla_c(pregunta_seleccionada)
        p21_df.to_excel(f'./files/separadas/repeat_p21.xlsx',index=False)
        respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
        resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

    elif pregunta_seleccionada=='p22':
        p22_df=pd.read_excel('./files/separadas/repeat_p22.xlsx')
        resultados_2023_df=pd.read_excel('./files/resultados/2023/resultados_2023.xlsx')
        respuestas_2023_df=pd.read_excel('./files/respuestas/2023/respuestas_2023.xlsx')

        tabla_criterios=tabla_c(pregunta_seleccionada)
        if criterio_seleccionado=='c1':  

            #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
            p22_df.loc[p22_df['_index']==iniciativa_seleccionada, 'nota_iniciativa']=nota

            nota_entidad = round(p22_df.loc[p22_df['_submission__uuid']==entidad_seleccionada]['nota_iniciativa'].mean(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota_entidad

        elif criterio_seleccionado=='c2':
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota
            
        else:
            pass

        
        nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
        respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
        resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta
        tabla_criterios=tabla_c(pregunta_seleccionada)
        p22_df.to_excel(f'./files/separadas/repeat_p22.xlsx',index=False)
        respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
        resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

    elif pregunta_seleccionada=='p23':
        p23_df=pd.read_excel('./files/separadas/repeat_p23.xlsx')
        resultados_2023_df=pd.read_excel('./files/resultados/2023/resultados_2023.xlsx')
        respuestas_2023_df=pd.read_excel('./files/respuestas/2023/respuestas_2023.xlsx') 

        tabla_criterios=tabla_c(pregunta_seleccionada)
        if criterio_seleccionado=='c1':  

            #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
            p23_df.loc[p23_df['_index']==iniciativa_seleccionada, 'c1']=nota

            nota_entidad = round(p23_df.loc[p23_df['_submission__uuid']==entidad_seleccionada]['c1'].mean(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota_entidad
        
        elif criterio_seleccionado=='c2':

            #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
            p23_df.loc[p23_df['_index']==iniciativa_seleccionada, 'c2']=nota

            nota_entidad = round(p23_df.loc[p23_df['_submission__uuid']==entidad_seleccionada]['c2'].mean(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota_entidad

        elif criterio_seleccionado=='c3':

            #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
            p23_df.loc[p23_df['_index']==iniciativa_seleccionada, 'c3']=nota

            nota_entidad = round(p23_df.loc[p23_df['_submission__uuid']==entidad_seleccionada]['c3'].mean(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c3'] = nota_entidad

        elif criterio_seleccionado=='c4':

            #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
            p23_df.loc[p23_df['_index']==iniciativa_seleccionada, 'c4']=nota

            nota_entidad = round(p23_df.loc[p23_df['_submission__uuid']==entidad_seleccionada]['c4'].mean(),4)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c4'] = nota_entidad
        
        else:
            pass


        p23_df['nota_iniciativa']=p23_df['c1']+p23_df['c2']+p23_df['c3']+p23_df['c4']

        nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c4'].sum().sum(),2)
        respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
        resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta
        tabla_criterios=tabla_c(pregunta_seleccionada)
        p23_df.to_excel(f'./files/separadas/repeat_p23.xlsx',index=False)
        respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
        resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

    elif pregunta_seleccionada=='p24':
        resultados_2023_df=pd.read_excel('./files/resultados/2023/resultados_2023.xlsx')
        respuestas_2023_df=pd.read_excel('./files/respuestas/2023/respuestas_2023.xlsx') 

        tabla_criterios=tabla_c(pregunta_seleccionada)
        if criterio_seleccionado=='c1':  
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota
        
        elif criterio_seleccionado=='c2':
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota

        elif criterio_seleccionado=='c3':
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c3'] = nota

        elif criterio_seleccionado=='c4':
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c4'] = nota

        else:
            pass
        
        nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c4'].sum().sum(),2)
        respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
        resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta
        tabla_criterios=tabla_c(pregunta_seleccionada)
        respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
        resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

    elif pregunta_seleccionada=='p25':
        p25_df=pd.read_excel('./files/separadas/repeat_p25.xlsx')
        resultados_2023_df=pd.read_excel('./files/resultados/2023/resultados_2023.xlsx')
        respuestas_2023_df=pd.read_excel('./files/respuestas/2023/respuestas_2023.xlsx') 

        tabla_criterios=tabla_c(pregunta_seleccionada)
        if criterio_seleccionado=='c1':  

            #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
            p25_df.loc[p25_df['_index']==iniciativa_seleccionada, 'nota_iniciativa']=nota

            nota_entidad = round(p25_df.loc[p25_df['_submission__uuid']==entidad_seleccionada]['nota_iniciativa'].mean(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota_entidad

        elif criterio_seleccionado=='c2':
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota

        else:
            pass
        
        nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
        respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
        resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta
        tabla_criterios=tabla_c(pregunta_seleccionada)
        p25_df.to_excel(f'./files/separadas/repeat_p25.xlsx',index=False)
        respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
        resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

    elif pregunta_seleccionada=='p26':
        p26_df=pd.read_excel('./files/separadas/repeat_p26.xlsx')
        resultados_2023_df=pd.read_excel('./files/resultados/2023/resultados_2023.xlsx')
        respuestas_2023_df=pd.read_excel('./files/respuestas/2023/respuestas_2023.xlsx')

        tabla_criterios=tabla_c(pregunta_seleccionada)
        if criterio_seleccionado=='c1':  

            #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
            p26_df.loc[p26_df['_index']==iniciativa_seleccionada, 'nota_iniciativa']=nota

            nota_entidad = round(p26_df.loc[p26_df['_submission__uuid']==entidad_seleccionada]['nota_iniciativa'].mean(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota_entidad

        elif criterio_seleccionado=='c2':
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota
            
        else:
            pass

        nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
        respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
        resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta
        tabla_criterios=tabla_c(pregunta_seleccionada)
        p26_df.to_excel(f'./files/separadas/repeat_p26.xlsx',index=False)
        respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
        resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

    elif pregunta_seleccionada=='p27':
        p27_df=pd.read_excel('./files/separadas/repeat_p27.xlsx')
        resultados_2023_df=pd.read_excel('./files/resultados/2023/resultados_2023.xlsx')
        respuestas_2023_df=pd.read_excel('./files/respuestas/2023/respuestas_2023.xlsx') 

        tabla_criterios=tabla_c(pregunta_seleccionada)
        if criterio_seleccionado=='c1':  

            #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
            p27_df.loc[p27_df['_index']==iniciativa_seleccionada, 'nota_iniciativa']=nota

            nota_entidad = round(p27_df.loc[p27_df['_submission__uuid']==entidad_seleccionada]['nota_iniciativa'].mean(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota_entidad

        else:
            pass
        
        nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'].sum().sum(),2)
        respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
        resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta
        tabla_criterios=tabla_c(pregunta_seleccionada)
        p27_df.to_excel(f'./files/separadas/repeat_p27.xlsx',index=False)
        respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
        resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

    elif pregunta_seleccionada=='p28':
        p28_df=pd.read_excel('./files/separadas/repeat_p28.xlsx')
        resultados_2023_df=pd.read_excel('./files/resultados/2023/resultados_2023.xlsx')
        respuestas_2023_df=pd.read_excel('./files/respuestas/2023/respuestas_2023.xlsx')

        tabla_criterios=tabla_c(pregunta_seleccionada)
        if criterio_seleccionado=='c1':  
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota

        elif criterio_seleccionado=='c2':
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota

        elif criterio_seleccionado=='c3':
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c3'] = nota

        elif criterio_seleccionado=='c4':

            #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
            p28_df.loc[p28_df['_index']==iniciativa_seleccionada, 'c4']=nota

            nota_entidad = round(p28_df.loc[p28_df['_submission__uuid']==entidad_seleccionada]['c4'].mean(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c4'] = nota_entidad

        elif criterio_seleccionado=='c5':

            #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
            p28_df.loc[p28_df['_index']==iniciativa_seleccionada, 'c5']=nota

            nota_entidad = round(p28_df.loc[p28_df['_submission__uuid']==entidad_seleccionada]['c5'].mean(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c5'] = nota_entidad
        
        else:
            pass

        p28_df['nota_iniciativa']=p28_df['c4']+p28_df['c5']

        nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c5'].sum().sum(),2)
        respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
        resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta
        tabla_criterios=tabla_c(pregunta_seleccionada)
        p28_df.to_excel(f'./files/separadas/repeat_p28.xlsx',index=False)
        respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
        resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

    elif pregunta_seleccionada=='p29':
        resultados_2023_df=pd.read_excel('./files/resultados/2023/resultados_2023.xlsx')
        respuestas_2023_df=pd.read_excel('./files/respuestas/2023/respuestas_2023.xlsx') 

        tabla_criterios=tabla_c(pregunta_seleccionada)
        if criterio_seleccionado=='c1':  
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota
            
        else:
            pass

        nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'].sum().sum(),2)
        respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
        resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta
        tabla_criterios=tabla_c(pregunta_seleccionada)
        respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
        resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

    elif pregunta_seleccionada=='p30':
        resultados_2023_df=pd.read_excel('./files/resultados/2023/resultados_2023.xlsx')
        respuestas_2023_df=pd.read_excel('./files/respuestas/2023/respuestas_2023.xlsx') 

        tabla_criterios=tabla_c(pregunta_seleccionada)
        if criterio_seleccionado=='c1':  
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota
            
        else:
            pass

        nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'].sum().sum(),2)
        respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
        resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta
        tabla_criterios=tabla_c(pregunta_seleccionada)
        respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
        resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

    elif pregunta_seleccionada=='p31':
        tabla_criterios=tabla_c(pregunta_seleccionada)

    elif pregunta_seleccionada=='p32':
        p32_df=pd.read_excel('./files/separadas/repeat_p32.xlsx')
        resultados_2023_df=pd.read_excel('./files/resultados/2023/resultados_2023.xlsx')
        respuestas_2023_df=pd.read_excel('./files/respuestas/2023/respuestas_2023.xlsx') 

        tabla_criterios=tabla_c(pregunta_seleccionada)
        if criterio_seleccionado=='c1':  
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota
        
        elif criterio_seleccionado=='c2':
            
            #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
            p32_df.loc[p32_df['_index']==iniciativa_seleccionada, 'nota_iniciativa']=nota

            nota_entidad = round(p32_df.loc[p32_df['_submission__uuid']==entidad_seleccionada]['nota_iniciativa'].mean(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota_entidad
        
        else:
            pass

        nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
        respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
        resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta
        tabla_criterios=tabla_c(pregunta_seleccionada)
        p32_df.to_excel(f'./files/separadas/repeat_p32.xlsx',index=False)
        respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
        resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

    elif pregunta_seleccionada=='p33':
        p33_df=pd.read_excel('./files/separadas/repeat_p33.xlsx')
        resultados_2023_df=pd.read_excel('./files/resultados/2023/resultados_2023.xlsx')
        respuestas_2023_df=pd.read_excel('./files/respuestas/2023/respuestas_2023.xlsx') 

        tabla_criterios=tabla_c(pregunta_seleccionada)
        if criterio_seleccionado=='c1':   
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota
        
        elif criterio_seleccionado=='c2':
            
            #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
            p33_df.loc[p33_df['_index']==iniciativa_seleccionada, 'nota_iniciativa']=nota

            nota_entidad = round(p33_df.loc[p33_df['_submission__uuid']==entidad_seleccionada]['nota_iniciativa'].mean(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota_entidad
        
        else:
            pass

        nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
        respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
        resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta
        tabla_criterios=tabla_c(pregunta_seleccionada)
        p33_df.to_excel(f'./files/separadas/repeat_p33.xlsx',index=False)
        respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
        resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

    elif pregunta_seleccionada=='p34':
        p34_df=pd.read_excel('./files/separadas/repeat_p34.xlsx')
        resultados_2023_df=pd.read_excel('./files/resultados/2023/resultados_2023.xlsx')
        respuestas_2023_df=pd.read_excel('./files/respuestas/2023/respuestas_2023.xlsx') 

        tabla_criterios=tabla_c(pregunta_seleccionada)
        if criterio_seleccionado=='c1':  
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota
        
        elif criterio_seleccionado=='c2':
            
            #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
            p34_df.loc[p34_df['_index']==iniciativa_seleccionada, 'nota_iniciativa']=nota

            nota_entidad = round(p34_df.loc[p34_df['_submission__uuid']==entidad_seleccionada]['nota_iniciativa'].mean(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota_entidad
        
        else:
            pass

        nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
        respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
        resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta
        tabla_criterios=tabla_c(pregunta_seleccionada)
        p34_df.to_excel(f'./files/separadas/repeat_p34.xlsx',index=False)
        respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
        resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

    elif pregunta_seleccionada=='p35':
        p35_df=pd.read_excel('./files/separadas/repeat_p35.xlsx')
        resultados_2023_df=pd.read_excel('./files/resultados/2023/resultados_2023.xlsx')
        respuestas_2023_df=pd.read_excel('./files/respuestas/2023/respuestas_2023.xlsx')

        tabla_criterios=tabla_c(pregunta_seleccionada)
        if criterio_seleccionado=='c1':   
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota
        
        elif criterio_seleccionado=='c2':

            #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
            p35_df.loc[p35_df['_index']==iniciativa_seleccionada, 'nota_iniciativa']=nota

            nota_entidad = round(p35_df.loc[p35_df['_submission__uuid']==entidad_seleccionada]['nota_iniciativa'].mean(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota_entidad
        
        else:
            pass

        nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
        respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
        resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta
        tabla_criterios=tabla_c(pregunta_seleccionada)
        p35_df.to_excel(f'./files/separadas/repeat_p35.xlsx',index=False)
        respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
        resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

    elif pregunta_seleccionada=='p36':
        p36_df=pd.read_excel('./files/separadas/repeat_p36.xlsx')
        resultados_2023_df=pd.read_excel('./files/resultados/2023/resultados_2023.xlsx')
        respuestas_2023_df=pd.read_excel('./files/respuestas/2023/respuestas_2023.xlsx') 

        tabla_criterios=tabla_c(pregunta_seleccionada)
        if criterio_seleccionado=='c1':  
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota
        
        elif criterio_seleccionado=='c2':
            
            #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
            p36_df.loc[p36_df['_index']==iniciativa_seleccionada, 'nota_iniciativa']=nota

            nota_entidad = round(p36_df.loc[p36_df['_submission__uuid']==entidad_seleccionada]['nota_iniciativa'].mean(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota_entidad
        
        else:
            pass

        nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
        respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
        resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta
        tabla_criterios=tabla_c(pregunta_seleccionada)
        p36_df.to_excel(f'./files/separadas/repeat_p36.xlsx',index=False)
        respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
        resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

    elif pregunta_seleccionada=='p37':
        p37_df=pd.read_excel('./files/separadas/repeat_p37.xlsx')
        resultados_2023_df=pd.read_excel('./files/resultados/2023/resultados_2023.xlsx')
        respuestas_2023_df=pd.read_excel('./files/respuestas/2023/respuestas_2023.xlsx')

        tabla_criterios=tabla_c(pregunta_seleccionada)
        if criterio_seleccionado=='c1':   
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota
        
        elif criterio_seleccionado=='c2':
            
            #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
            p37_df.loc[p37_df['_index']==iniciativa_seleccionada, 'nota_iniciativa']=nota
            
            nota_entidad = round(p37_df.loc[p37_df['_submission__uuid']==entidad_seleccionada]['nota_iniciativa'].mean(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota_entidad
        
        else:
            pass

        nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
        respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
        resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta
        tabla_criterios=tabla_c(pregunta_seleccionada)
        p37_df.to_excel(f'./files/separadas/repeat_p37.xlsx',index=False)
        respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
        resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

    elif pregunta_seleccionada=='p38':
        p38_df=pd.read_excel('./files/separadas/repeat_p38.xlsx')
        resultados_2023_df=pd.read_excel('./files/resultados/2023/resultados_2023.xlsx')
        respuestas_2023_df=pd.read_excel('./files/respuestas/2023/respuestas_2023.xlsx')

        tabla_criterios=tabla_c(pregunta_seleccionada)
        if criterio_seleccionado=='c1':  
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota
        
        elif criterio_seleccionado=='c2':
            
            #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
            p38_df.loc[p38_df['_index']==iniciativa_seleccionada, 'nota_iniciativa']=nota

            nota_entidad = round(p38_df.loc[p38_df['_submission__uuid']==entidad_seleccionada]['nota_iniciativa'].mean(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota_entidad
        
        else:
            pass

        nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
        respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
        resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta
        tabla_criterios=tabla_c(pregunta_seleccionada)
        p38_df.to_excel(f'./files/separadas/repeat_p38.xlsx',index=False)
        respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
        resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

    elif pregunta_seleccionada=='p39':
        p39_df=pd.read_excel('./files/separadas/repeat_p39.xlsx')
        resultados_2023_df=pd.read_excel('./files/resultados/2023/resultados_2023.xlsx')
        respuestas_2023_df=pd.read_excel('./files/respuestas/2023/respuestas_2023.xlsx') 

        tabla_criterios=tabla_c(pregunta_seleccionada)
        if criterio_seleccionado=='c1':  
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'] = nota
        
        elif criterio_seleccionado=='c2':
            
            #ASIGNACIÓN DE NOTA DE INICIATIVA EN CRITERIO                
            p39_df.loc[p39_df['_index']==iniciativa_seleccionada, 'nota_iniciativa']=nota
            
            nota_entidad = round(p39_df.loc[p39_df['_submission__uuid']==entidad_seleccionada]['nota_iniciativa'].mean(),2)
            respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'] = nota_entidad
        
        else:
            pass

        nota_total_pregunta=round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1':f'cri_{pregunta_seleccionada}_c2'].sum().sum(),2)
        respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'{pregunta_seleccionada}_nota_pregunta'] = nota_total_pregunta
        resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,pregunta_seleccionada] = nota_total_pregunta
        tabla_criterios=tabla_c(pregunta_seleccionada)
        p39_df.to_excel(f'./files/separadas/repeat_p39.xlsx',index=False)
        respuestas_2023_df.to_excel('./files/respuestas/2023/respuestas_2023.xlsx',index=False)
        resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)

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

"""


"""
resultados_2023_df=pd.read_excel('./files/resultados/2023/resultados_2023.xlsx')

resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,'res_c1'] = round(resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,'p1':'p13'].sum().sum(),2)
resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,'res_c2'] = round(resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,'p14':'p27'].sum().sum(),2)
resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,'res_c3'] = round(resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,'p28':'p30'].sum().sum(),2)
resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,'res_c4'] = round(resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,'p31':'p39'].sum().sum(),2)
resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,'total'] = round(resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,'res_c1':'res_c4'].sum().sum(),2)

resultados_2023_df.to_excel('./files/resultados/2023/resultados_2023.xlsx',index=False)
#"""


"""

        table_out={
            'p1':{},
            'p2':{'c1':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,},'c2':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,},'c3':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,}},
            'p3':{},
            'p4':{'c1':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,},'c2':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,}},
            'p5':{},
            'p6':{'c1':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,},'c2':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,}},
            'p7':{},
            'p8':{'c1':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,},'c2':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,}},
            'p9':{},
            'p10':{},
            'p11':{'c1':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,},'c2':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,}},
            'p12':{},
            'p13':{'c1':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,},'c2':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,}},
            'p14':{'c1':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,},'c2':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,}},
            'p15':{'c1':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,},'c2':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,}},
            'p16':{'c1':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,},'c2':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,}},
            'p17':{'c1':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,},'c2':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,}},
            'p18':{'c1':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,},'c2':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,}},
            'p19':{'c1':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,},'c2':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,}},
            'p20':{'c1':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,},'c2':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,}},
            'p21':{'c1':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,},'c2':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,}},
            'p22':{'c1':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,},'c2':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,}},
            'p23':{'c1':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,},'c2':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,},'c3':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,},'c4':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,}},
            'p24':{'c1':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,},'c2':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,},'c3':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,},'c4':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,}},
            'p25':{'c1':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,},'c2':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,}},
            'p26':{'c1':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,},'c2':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,}},
            'p27':{'c1':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,}},
            'p28':{'c1':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,},'c2':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,},'c3':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,},'c4':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,},'c5':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,}},
            'p29':{'c1':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,}},
            'p30':{'c1':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,}},
            'p31':{},
            'p32':{'c1':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,},'c2':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,}},
            'p33':{'c1':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,},'c2':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,}},
            'p34':{'c1':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,},'c2':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,}},
            'p35':{'c1':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,},'c2':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,}},
            'p36':{'c1':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,},'c2':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,}},
            'p37':{'c1':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,},'c2':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,}},
            'p38':{'c1':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,},'c2':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,}},
            'p39':{'c1':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,},'c2':{'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,}},
        }

"""


"""

#Callback cargar tabla
@dash.callback(
    Output('tabla_criterios', 'children'),

    Input('tabla_crits', 'data'),
    Input('entidad_seleccionada', 'data'),
    Input('pregunta_seleccionada', 'data'),
    Input('iniciativa_seleccionada', 'data'),
    Input('criterio_seleccionado_entidad', 'data'),
    Input('criterio_seleccionado_bucle', 'data'),
    Input('criterios_disponibles_bucle', 'data')
)
def cargar_tabla(tabla_crits,entidad_seleccionada,pregunta_seleccionada,iniciativa_seleccionada,criterio_seleccionado_entidad,criterio_seleccionado_bucle,criterios_disponibles_bucle):

    print(tabla_crits)

    if pregunta_seleccionada=='p1':
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

    elif pregunta_seleccionada=='p2':
        tabla_criterios=html.Div(children=[
            dbc.Table(
                children=[
                html.Thead(children=[
                    html.Tr([
                        html.Th(f'c1'),
                        html.Th(f'c2'),
                        html.Th(f'c3'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(tabla_crits['p2']['c1']['c1'],rowSpan=2),
                        html.Td(tabla_crits['p2']['c2']['c1'],rowSpan=2),
                        html.Td(tabla_crits['p2']['c3']['c1']),
                    ],
                    ),
                    html.Tr([
                        html.Td(tabla_crits['p2']['c3']['c2']),
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

    elif pregunta_seleccionada=='p3':
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

    elif pregunta_seleccionada=='p4':
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
        return tabla_criterios

    elif pregunta_seleccionada=='p5':
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

    elif pregunta_seleccionada=='p6':
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
        return tabla_criterios

    elif pregunta_seleccionada=='p7':
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

    elif pregunta_seleccionada=='p8':
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
        return tabla_criterios
        
    elif pregunta_seleccionada=='p9':
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

    elif pregunta_seleccionada=='p10':
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

    elif pregunta_seleccionada=='p11':
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
        return tabla_criterios

    elif pregunta_seleccionada=='p12':
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

    elif pregunta_seleccionada=='p13':
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
                        html.Td(p13_df.loc[p13_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

    elif pregunta_seleccionada=='p14':
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
                        html.Td(p14_df.loc[p14_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

    elif pregunta_seleccionada=='p15':
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
                        html.Td(p15_df.loc[p15_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

    elif pregunta_seleccionada=='p16':
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
                        html.Td(p16_df.loc[p16_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

    elif pregunta_seleccionada=='p17':
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
                        html.Td(p17_df.loc[p17_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

    elif pregunta_seleccionada=='p18':
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
                        html.Td(p18_df.loc[p18_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

    elif pregunta_seleccionada=='p19':
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
                        html.Td(p19_df.loc[p19_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

    elif pregunta_seleccionada=='p20':
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
                        html.Td(p20_df.loc[p20_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

    elif pregunta_seleccionada=='p21':
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
                        html.Td(p21_df.loc[p21_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

    elif pregunta_seleccionada=='p22':
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
                        html.Td(p22_df.loc[p22_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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
        return tabla_criterios

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
        return tabla_criterios

    elif pregunta_seleccionada=='p25':
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
                        html.Td(p25_df.loc[p25_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

    elif pregunta_seleccionada=='p26':
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
                        html.Td(p26_df.loc[p26_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

    elif pregunta_seleccionada=='p27':
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
                        html.Td(p27_df.loc[p27_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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
                        html.Th(f'c5'),
                    ],
                    )                  
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c1'],2),rowSpan=2),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c2'],2),rowSpan=2),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c3'],2),rowSpan=2),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c4'],2)),
                        html.Td(round(respuestas_2023_df.loc[respuestas_2023_df['_uuid']==entidad_seleccionada,f'cri_{pregunta_seleccionada}_c5'],2)),
                    ],
                    ),
                    html.Tr([
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
        return tabla_criterios

    elif pregunta_seleccionada=='p29':
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
        return tabla_criterios

    elif pregunta_seleccionada=='p30':
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
        return tabla_criterios

    elif pregunta_seleccionada=='p31':
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

    elif pregunta_seleccionada=='p32':
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
                        html.Td(p32_df.loc[p32_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

    elif pregunta_seleccionada=='p33':
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
                        html.Td(p33_df.loc[p33_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

    elif pregunta_seleccionada=='p34':
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
                        html.Td(p34_df.loc[p34_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

    elif pregunta_seleccionada=='p35':
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
                        html.Td(p35_df.loc[p35_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

    elif pregunta_seleccionada=='p36':
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
                        html.Td(p36_df.loc[p36_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

    elif pregunta_seleccionada=='p37':
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
                        html.Td(p37_df.loc[p37_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

    elif pregunta_seleccionada=='p38':
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
                        html.Td(p38_df.loc[p38_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

    elif pregunta_seleccionada=='p39':
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
                        html.Td(p39_df.loc[p39_df['_index']==iniciativa_seleccionada,'nota_iniciativa']),
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

"""