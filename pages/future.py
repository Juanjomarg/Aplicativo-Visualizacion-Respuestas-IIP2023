from assets.libraries import *
from assets.commons import *
from assets.cards import *

dash.register_page(__name__, path='/future')

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1(children=['Pronto'])
            ],
            width=9,
        ),
        dbc.Col([
            html.Span('Things to come...')
            ],
            width=3,

        )
        ],
        justify="end"
    )
    ]
)

