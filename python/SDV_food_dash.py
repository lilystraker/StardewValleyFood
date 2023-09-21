import plotly.graph_objects as go
import plotly.io as pio
import pandas
import plotly.express as px
from PIL import Image
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

def main():
    #filename = input("Food: ")
    #extension = '.csv'
    food_dict = {}
    value = 0
    graph_name = []
    value_list = []
    name_order = []
    final_color_list = []
    name_value_list = []    
    wanted_status = ""
    while wanted_status.lower() != 'quit':
        wanted_status = input("Food: ")
        
        if wanted_status.lower() != 'quit':
            extension = '.csv'
            fileexten = wanted_status.lower() + extension.lower()
            
            data = open(fileexten)
            lines = data.readlines()
            lines = [line for line in lines if line.strip() != ""]    
            
            for line in lines:
                line = line.rstrip()
                line = line.split()
                
                if 'Food:' == line[0]:
                    food = line[1]
                    
                elif 'Love' == line[0]:
                    status = line[0]
                    value = 5
                    name_list = []
        
                elif 'Like' == line[0]:
                    status = line[0]
                    name_list = []
                    value = 4
                  
                elif 'Neutral' == line[0]:
                    status = line[0]
                    name_list = []
                    value = 3
                elif 'Dislike' == line[0]:
                    status = line[0]
                    name_list = []
                    value = 2
                elif 'Hate' == line[0]:
                    status = line[0]
                    name_list = []            
                    value = 1
                else:
                    name = line[0]
                    name_value_list.append((name, value))
                    name_order.append(name)
                    name_list.append(name)
                    graph_name.append(name)
                    value_list.append(value)
                    food_dict[status] = name_list            
                    
            print(food_dict)
            

            #fig = go.Figure(
                #data=go.Bar(x=graph_name, y=value_list), 
                ##layout = layout
                ##hovertext=['27% market share', '24% market share', '19% market share']
            #)        

            #fig.show()
    return food_dict


     

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}


app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    #html.H1(
        #children='Hello Dash',
        #style={
            #'textAlign': 'center',
            #'color': colors['text']
        #}
    #),
    #html.Div(children='Dash: A web application framework for Python.', style={
        #'textAlign': 'center',
        #'color': colors['text']
    #}),
    
    #dcc.Graph(
        #id='Graph1',
        #figure={
            #'data': [
                #{'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                #{'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montreal'},
            #],
            #'layout': {
                #'plot_bgcolor': colors['background'],
                #'paper_bgcolor': colors['background'],
                #'font': {
                    #'color': colors['text']
                #}
            #}
        #}
    #)
    dcc.RadioItems(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montreal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
    )      
    
 
])    





if __name__ == '__main__':
    app.run_server(debug=True)

