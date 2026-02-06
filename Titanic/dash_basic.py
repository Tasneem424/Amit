from dash import Dash,html,dcc
from dash.dependencies import input,output

app =Dash(__name__)

app.layout=html.Div([
     html.Button('Submit',id='number'),
     dcc.Input(placeholder="Enter valid number",
               id='Data',type='number'),
     html.H1(id='Result')])

app.run(debug=True)