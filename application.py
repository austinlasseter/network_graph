import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
application = app.server
app.title='Dash on AWS EB!'

mylist = ['fist', 'head-butt', 'roundhouse-kick']
app.layout=html.Div([
    html.H2('Chuck Norris execution method'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label':i, 'value': i} for i in mylist],
        value=None
    ),
    html.Div(id='display-value')
])

@app.callback(dash.dependencies.Output('display-value', 'children'),
                [dash.dependencies.Input('dropdown', 'value')]
)
def display_value(value):
    return 'Chuck Norris will now execute you by {}'.format(value)

########### Run the app
if __name__ == '__main__':
    application.run(debug=True, port=8080)
