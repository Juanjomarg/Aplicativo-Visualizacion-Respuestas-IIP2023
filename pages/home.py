from assets.libraries import *
from assets.commons import *
from assets.cards import *

dash.register_page(__name__, path='/')

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1(children=['Estadisticas'])
            ],
            width=9,
        ),
        dbc.Col([
            html.Span('Estadisticas generales')
            ],
            width=3,

        )
        ],
        justify="end"
    )
    ]
)