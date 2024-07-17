# @title Dashboard
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

# Load the data
data = {
    'Year': [2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015],
    'Total Net Sales': [383285, 394328, 365817, 274515, 196134, 202695, 229234, 215639, 233715],
    'Products Net Sales': [298085, 316199, 297392, 220747, 162354, 173546, None, None, None],
    'Services Net Sales': [85200, 78129, 68425, 53768, 33780, 29149, None, None, None],
    'Revenue by iPhone': [200583, 205489, 191973, 137781, 109019, 128133, None, None, None],
    'Revenue by iPad': [28300, 29292, 31862, 23724, 16624, 14397, None, None, None],
    'Revenue by Mac': [29357, 40177, 35190, 28622, 18749, 17858, None, None, None],
    'Gross Margin': [169148, 170782, 152836, 104956, 74079, 77755, 88186, 84263, 93626],
    'Operating Income': [114301, 119437, 108949, 66288, 48305, 54780, 61344, 60024, 71230],
    'Net Income': [96995, 99803, 94680, 57411, 41570, 45406, 48351, 45687, 53394],
    'EPS (Diluted)': [6.13, 6.11, 5.61, 3.28, 8.86, 8.99, 9.21, 8.31, 9.22],
    'R&D Expenses': [29915, 26251, 21914, 18752, 12107, 10486, 11581, 10045, 8067],
    'ROA': [27.51, 28.29, 26.97, 17.73, 12.9, 12.42, 12.89, 14.21, 18.39],
    'Profit Margin Ratio': [25.3, 25.31, 25.88, 20.92, 21.2, 22.4, 21.1, 21.18, 22.85],
    'Asset Turnover Ratio': [1.09, 1.12, 1.04, 0.85, 0.61, 0.55, 0.61, 0.67, 0.8],
    'Inventory Turnover Ratio': [29.89, 46.79, 34.38, 48.57, 26.08, 25.89, 30.34, 74.06, 59.65]
}

df = pd.DataFrame(data)

# Initialize Dash app
app = Dash(__name__)

# Define layout
app.layout = html.Div([
    html.H1("Company Performance Dashboard"),

    dcc.Tabs([
        dcc.Tab(label='Sales Overview', children=[
            dcc.Graph(
                id='sales-overview',
                figure=px.line(df, x='Year', y=['Total Net Sales', 'Products Net Sales', 'Services Net Sales'],
                               title='Sales Overview', labels={'value': 'Sales (in millions)'})
            )
        ]),

        dcc.Tab(label='Revenue Breakdown', children=[
            dcc.Graph(
                id='revenue-breakdown',
                figure=go.Figure(
                    data=[
                        go.Scatter(name='iPhone', x=df['Year'], y=df['Revenue by iPhone'], stackgroup='one'),
                        go.Scatter(name='iPad', x=df['Year'], y=df['Revenue by iPad'], stackgroup='one'),
                        go.Scatter(name='Mac', x=df['Year'], y=df['Revenue by Mac'], stackgroup='one')
                    ],
                    layout=go.Layout(title='Revenue Breakdown by Product', xaxis=dict(title='Year'), yaxis=dict(title='Revenue (in millions)'))
                )
            )
        ]),

        dcc.Tab(label='Financial Performance', children=[
            dcc.Graph(
                id='financial-performance',
                figure=go.Figure(
                    data=[
                        go.Bar(name='Gross Margin', x=df['Year'], y=df['Gross Margin'], yaxis='y1', marker=dict(color='skyblue')),
                        go.Scatter(name='Operating Income', x=df['Year'], y=df['Operating Income'], yaxis='y2', marker=dict(color='green')),
                        go.Scatter(name='Net Income', x=df['Year'], y=df['Net Income'], yaxis='y2', marker=dict(color='red'))
                    ],
                    layout=go.Layout(
                        title='Financial Performance',
                        xaxis=dict(title='Year'),
                        yaxis=dict(title='Gross Margin (in millions)', side='left'),
                        yaxis2=dict(title='Income (in millions)', overlaying='y', side='right')
                    )
                )
            )
        ]),

        dcc.Tab(label='Earnings Per Share', children=[
            dcc.Graph(
                id='eps-diluted',
                figure=px.line(df, x='Year', y='EPS (Diluted)', title='Earnings Per Share (Diluted)', labels={'EPS (Diluted)': 'EPS (Dollars)'})
            )
        ]),

        dcc.Tab(label='R&D Expenses', children=[
            dcc.Graph(
                id='rd-expenses',
                figure=px.bar(df, x='Year', y='R&D Expenses', title='Research and Development Expenses', labels={'R&D Expenses': 'R&D Expenses (in millions)'}, color='Year')
            )
        ]),

        dcc.Tab(label='Efficiency and Performance Ratios', children=[
            dcc.Graph(
                id='efficiency-ratios',
                figure=px.line(df, x='Year', y=['ROA', 'Profit Margin Ratio', 'Asset Turnover Ratio', 'Inventory Turnover Ratio'],
                               title='Efficiency and Performance Ratios', labels={'value': 'Ratio'})
            )
        ]),
    ])
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

