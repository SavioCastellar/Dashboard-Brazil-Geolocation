import py_compile
from datetime import date
from dash import dash, Dash, html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from matplotlib.container import Container

import plotly.express as px
import plotly.graph_objects as go

import numpy as np
import pandas as pd
import json
import psycopg2

from choropleth_query import state_df
from bar_graph_query import bar_graph_df
from scatter_query import scatter_df
from date_picker_query import date_picker_df

########### Tratamento dos dados ###########

# Arquivo que fornece as fronteiras dos estados brasileiros
geojson = json.load(open("json/brazil_geo.json", "r"))

# Dicionário {estado : geojson}
dict_states = {
    "MG": "mg_geo.json",
    "DF": "brasilia_geo.json"
}

########### Instanciando o Dash ###########

app = dash.Dash(__name__, external_stylesheets=[
                dbc.themes.DARKLY], prevent_initial_callbacks=True)

# Criação do mapa coroplético
fig = px.choropleth_mapbox(
    state_df,  # Base de dados para o gráfico
    mapbox_style="carto-darkmatter",
    # Posição para onde o zoom será direcionado
    center={"lat": -14.6633, "lon": -53.54627},
    zoom=3,
    color_continuous_scale="teal",
    locations="state",  # Coluna que faz match com o geojson
    color="count",  # Parâmetro que vai definir a intensidade da cor de cada estado
    geojson=geojson,
)

# Atualizações de layout do mapa
fig.update_layout(
    paper_bgcolor="#222222",
    autosize=True,
    margin=dict(l=0, r=0, t=0, b=0),
    showlegend=False,
    font_color="#FFFFFF"
)

# Criação de um gráfico de barras
fig2 = px.bar(bar_graph_df, x="state", y="quantities",
              color="geoapi_id", barmode="stack")
fig2.update_layout(
    paper_bgcolor="#222222",
    autosize=True,
    margin=dict(l=0, r=0, t=0, b=0),
    font_color="#FFFFFF"
)

# Criação do mapa coroplético com pontos
px.set_mapbox_access_token(open(".mapbox_token").read())
fig3 = px.scatter_mapbox(scatter_df, mapbox_style="carto-darkmatter",
                         lat=scatter_df["latitude"],
                         lon=scatter_df["longitude"],
                         color=scatter_df["geoapi_id"],
                         center={"lat": -14.6633, "lon": -53.54627},
                         zoom=3)

# Atualizações de layout do mapa
fig3.update_layout(
    paper_bgcolor="#222222",
    autosize=True,
    margin=dict(l=0, r=0, t=0, b=0),
    showlegend=True,
    font_color="#FFFFFF"
)

########### Layout ###########

app.layout = dbc.Container(
    children=[
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H4(children="Desafio Data Analytics TerraLAB"),
                ], style={"background-color": "#222222", "margin-top": "30px", "margin-left": "20px"})
            ], md=7),
            dbc.Col([
                html.P("Seleção de data:", style={
                       "margin-top": "25px", "margin-left": "80px"})
            ], md=2),
            dbc.Col([
                html.Div(
                    className="div-for-dropdown",
                    id="div-test",
                    children=[
                        dcc.DatePickerSingle(
                            id="date-picker",
                            min_date_allowed=date(2022, 2, 8),
                            max_date_allowed=date(2022, 5, 26),
                            date=date_picker_df["date"].unique(),
                            style={"margin-top": "10px", "margin-left": "0px", "border": "0px solid black"})]
                )
            ], md=3)
        ]),
        dbc.Row([
            dbc.Col([
                html.P("Geolocalizações por estado", style={
                       "color": "#B8B8B8", "margin-top": "-10px", "margin-left": "0px", "margin-bottom": "5px"}),
                dcc.Graph(id='choropleth-map', figure=fig,
                          style={'height': '80vh'})], md=6, style={
                "padding": "25px",
                "background-color": "#222222",
            }),
            dbc.Col([
                html.P("Localização das APIs", style={
                       "color": "#B8B8B8", "margin-top": "-10px", "margin-left": "0px", "margin-bottom": "5px"}),
                dcc.Graph(id='scatter-map', figure=fig3,
                          style={'height': '80vh'}),
            ], md=6, style={
                "padding": "25px",
                "background-color": "#222222",
            }
            )
        ]),
        dbc.Row([
            html.Div([
                html.P("Selecione que tipo de dado deseja visualizar:", style={
                       "margin-top": "10px", "margin-left": "50px", "margin-bottom": "-15px"}),
                dcc.Graph(
                    id="bar-graph",
                    figure=fig2, style={
                        "background-color": "#222222",
                        "padding": "40px",
                    })
            ])
        ]),
    ], fluid=True
)

########### Interação com o mapa ###########

# Mudar o gráfico de pontos a partir do date picker
# @app.callback(
#     [Output("scatter-map", "figure"),
#     Output("choropleth-map", "figure"),
#     Output("bar-graph", "figure")
#      ]
#       # Id do gráfico - atributo a ser mudado
#     [Input("date-picker", "date")] # Usar o valor exibido no date picker como input
# )
# def update_scatter_mapbox(value):

#     print(value)
#     # Response:
#     # 2022-05-10

#     # print(scatter_df[scatter_df['date'] == value])
#     # Response
#     # Empty DataFrame
#     # Columns: [date, latitude, longitude, geoapi_id]
#     # Index: []

#     date = scatter_df[scatter_df['date'] == value]

#     # Atualizando o gráfico a partir da nova base de dados
#     fig3 = px.scatter_mapbox(date,mapbox_style="carto-darkmatter",
#                         lat= date["latitude"],
#                         lon=date["longitude"],
#                         color=date["geoapi_id"],
#                         center={"lat": -14.6633, "lon": -53.54627},
#                         zoom=3)
#     fig3.update_layout(
#         paper_bgcolor="#222222",
#         autosize=True,
#         margin=dict(l=0, r=0, t=0, b=0),
#         showlegend=True,
#         font_color="#FFFFFF"
#     )
#     return fig3

########### Rodar servidor de teste ###########

if __name__ == '__main__':
    app.run_server(debug=False)
