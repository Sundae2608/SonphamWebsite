import dash
import plotly.express as px
import pandas as pd

from dash.dependencies import Input, Output
from flask import Flask
from dash import dcc
from dash import html

# Create a Flask instance
server = Flask(__name__)

# Create a Dash instance
app = dash.Dash(__name__, server=server, url_base_pathname='/')

# Sample DataFrame
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Grapes"],
    "Amount": [4, 1, 2, 2]
})

# Initial plot
fig = px.bar(df, x="Fruit", y="Amount", title="Fruit Amounts")

# Layout of the Dash app
app.layout = html.Div(children=[
    html.H1(children='Interactive Graph Blog'),

    html.Div(children='''
        This is an example of an interactive graph using Plotly Dash.
    '''),

    # User input for the title of the graph
    dcc.Input(id='input-title', value='Fruit Amounts', type='text'),

    # Graph component
    dcc.Graph(
        id='example-graph',
        figure=fig,
        config={
            'staticPlot': False,
            'displayModeBar': False,
            'scrollZoom': False,
            'doubleClick': 'reset',
            'showTips': False,
            'displaylogo': False,
            'modeBarButtonsToRemove': ['pan2d', 'select2d', 'lasso2d', 'zoomIn2d', 'zoomOut2d', 'autoScale2d', 'resetScale2d', 'hoverClosestCartesian', 'hoverCompareCartesian']
        }
    )
])

# Callback to update the graph based on user input
@app.callback(
    Output('example-graph', 'figure'),
    [Input('input-title', 'value')]
)
def update_graph(input_value):
    # Update the figure title based on user input
    fig.update_layout(title=input_value)
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)