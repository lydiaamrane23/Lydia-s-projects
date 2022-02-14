#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sqldf
import numpy as np
import plotly.graph_objects as go
#import datapane as dp
from math import floor
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import sqldf
import calendar


# In[2]:


app=dash.Dash(external_stylesheets=['https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css'])


# In[3]:


df=pd.read_csv('all_candidates.csv')


# In[4]:


df.head(3)


# In[5]:


df['date']=pd.to_datetime(df['date'])
df['Month'] = df['date'].dt.month 


# In[6]:


df_new=df[['name','competition','Month','goals','assists','minutes','yellow','red','yellow_x2']]
df_tmp = df_new.groupby(['name','Month','competition']).sum().sort_values(by=['minutes','goals','assists','yellow','red' ],ascending = False)
df_tmp['playing_time']=df_tmp['minutes']//60
del df_tmp['minutes'] 


# In[7]:


df_tmp = pd.DataFrame(data = df_tmp, columns = ['playing_time','goals','assists','yellow','red','yellow_x2'])

df_tmp=df_tmp.reset_index()


# In[8]:


mois=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November']


# In[ ]:


players_names=df.name.unique()
players_names=np.append(players_names,'All')


# In[ ]:


compets=df.competition.unique()
compets=np.append(compets,'All')


# In[ ]:


sdl="""SELECT Distinct name, played_position  
FROM df; 
"""
df_agreg=sqldf.run(sdl)

requet=""" SELECT played_position, COUNT (*) as value  FROM df_agreg  where played_position <> 'None' group  by played_position; """
#run requet
df_agreg_1=sqldf.run(requet)


# In[ ]:


trace0=go.Scatter(
        x=df_tmp.Month,
        y=df_tmp.yellow,
        mode='lines+markers',
        name='yellow cards'

)
trace1=go.Scatter(
        x=df_tmp.Month,
        y=df_tmp.red,
        mode='lines+markers',
        name='red cards'

)
trace2=go.Scatter(
        x=df_tmp.Month,
        y=df_tmp.yellow_x2,
        mode='lines+markers',
        name='yellow_x2'
)


# In[ ]:


df_nouv=df[['name','competition','Month','goals','assists','minutes','yellow','red','yellow_x2']]
df_final = df_nouv.groupby(['competition']).sum().sort_values(by=['minutes','goals','assists','yellow','red' ],ascending = False)
df_final = pd.DataFrame(data = df_final, columns = ['minutes','goals','assists','yellow','red','yellow_x2'])

df_final=df_final.reset_index()


# In[ ]:


df=pd.read_csv('all_candidates.csv')
df['date']=pd.to_datetime(df['date'])
df['Month'] = df['date'].dt.month 
categories =['playing_time', 'goals', 'assists', 'yellow']
df_new=df[['name','yellow','goals','assists','minutes','Month']]

df_tmp_1 = df_new.groupby(['name']).sum().sort_values(by=['minutes','goals','assists','yellow' ],ascending = False)
df_tmp_1['playing_time']=df_tmp_1['minutes']//60
df_tmp_1['playing_time']=df_tmp_1['playing_time']/3
del df_tmp_1['minutes']
df_tmp_1 = pd.DataFrame(data = df_tmp_1, columns = ['playing_time','goals','assists','yellow'])
df_tmp_1=df_tmp_1.reset_index()
df_tmp_1
goals_med=floor(np.median(df_tmp_1['goals']) )
p_med=floor(np.median(df_tmp_1['playing_time']))
a_med=floor(np.median(df_tmp_1['assists']))
y_med=floor(np.median(df_tmp_1['yellow']))


# In[ ]:


import plotly.express as px

figure9 = px.scatter(df_final, x="minutes", y="goals",
             size="assists", color="competition",
                 hover_name="competition", log_x=True, size_max=60)


# In[ ]:


colors = {
    'background': 'rgba(35, 57, 82, 0.45)',
    'text': '#7FDBFF'
}


# In[ ]:


import dash
import plotly.express as px
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
categories =['playing_time', 'goals', 'assists', 'yellow']
df_new=df[['name','yellow','goals','assists','minutes','Month']]
df_tmp_1 = df_new.groupby(['name']).sum().sort_values(by=['minutes','goals','assists','yellow' ],ascending = False)
df_tmp_1['playing_time']=df_tmp_1['minutes']//60
df_tmp_1['playing_time']=df_tmp_1['playing_time']/3
del df_tmp_1['minutes']
df_tmp_1 = pd.DataFrame(data = df_tmp_1, columns = ['playing_time','goals','assists','yellow'])
df_tmp_1=df_tmp_1.reset_index()
df_tmp2=df_tmp_1
df_tmp2['playing_time']=df_tmp2['playing_time']/3
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div( style={'backgroundColor': colors['background']}, children=[
    html.Br(),
    
    html.H1(' ⚽🏆⚽🏆⚽🏆⚽🏆⚽🏆 FIFA Ballon d\'Or 2021   🏆⚽🏆⚽🏆⚽🏆⚽🏆⚽ ',style={"textAlign":"center","color":"white"}),
    
    dcc.Tabs(id="tabs-example-graph", value='tab-1-example-graph',style={'backgroundColor': colors['background']}, children=[
        dcc.Tab(label='Individual player performances', value='tab-1-example-graph'),
        dcc.Tab(label='Data distribution', value='tab-2-example-graph'),
        dcc.Tab(label='Player Comparison', value='tab-3-example-graph'),
    ]),
    html.Div(id='tabs-content-example-graph')
])

@app.callback(Output('tabs-content-example-graph', 'children'),
              Input('tabs-example-graph', 'value'))
def render_content(tab):
    if tab == 'tab-1-example-graph':
        return html.Div([html.Div([html.Div([html.P('Choose a player'),
    dcc.Dropdown(
        id="dropdown",
        options=[{"label": x, "value": x} for x in players_names],
        multi=True,
        value='All'
        
    )
],style={'width':'50%', 'display': 'inline-block'}), 
 html.Div([html.P('Choose a competition'),
    dcc.Dropdown(
        id="dropdown2",
        options=[{"label": x, "value": x} for x in compets],
        multi=True,
        value='All'
        
    ),
],style={'width':'50%', 'display': 'inline-block'})  ])

,html.Div(
    [
        dcc.Graph(
            id="bar-chart",
            figure={
                'data': [
                    go.Bar(
                        x=df_tmp.name,
                        y=df_tmp.playing_time,
                         name='playing_time'
        
                    ),
                     go.Bar(
                        x=df_tmp.name,
                        y=df_tmp.goals,
                         name='goals'
        
                    ),
                     go.Bar(
                        x=df_tmp.name,
                        y=df_tmp.assists,
                         name='assists'
        
                    )
                    
                ],
                'layout':go.Layout(
                     title='Goals, Assists and playing_time by player',
                            
                     xaxis={'title':'Player'},
                    yaxis={'title':'Goals'}
                
                
                )
            },
        ),
        
        
    ]
),html.Br(),html.Div([
            dcc.RangeSlider(
            id='day-slider',
            min=df['Month'].min(),
            max=df['Month'].max(),
            value=[df['Month'].min(), df['Month'].max()],
            step=None,
            marks={str(month): val for (val,month) in zip(mois,np.sort(df['Month'].unique()))}
        )

    ]),html.Div(
    [ html.Div(
    [ dcc.Graph(
            id="bar-chart3", 
        
            figure={'data':[go.Pie(labels=df_agreg_1["played_position"],
            values=df_agreg_1["value"]          
            )],            'layout':go.Layout(
                     title='Goals, Assists and playing_time by player'
                
                
                )})],style={'width':'50%', 'display': 'inline-block'})
                       
    , html.Div(
    [ dcc.Graph(
            id="bar-chart4", 
            figure={'data':[trace0,trace1,trace2]})],style={'width':'50%','display': 'inline-block'})
    
     ])
     #], className="row")
                       
                       

])
    if tab == 'tab-2-example-graph':
        return html.Div([
    html.P("x-axis:"),
    dcc.RadioItems(
        id='x-axis', 
        options=[{'value': x, 'label': x} 
                 for x in ['Month','name']],
        value='name', 
        labelStyle={'display': 'inline-block'}
    ),
    html.P("y-axis:"),
    dcc.RadioItems(
        id='y-axis', 
        options=[{'value': x, 'label': x} 
                 for x in ['goals', 'assists','playing_time']],
        value='goals', 
        labelStyle={'display': 'inline-block'}
    ),
    dcc.Graph(id="box-plot"),
     html.Div(
    [ dcc.Graph(
            id="bar-chart4", 
            figure=figure9)])
    

])
    elif tab == 'tab-3-example-graph':
        return html.Div([ html.Div([
    html.Div([          
    html.P("Choose Player1:",className='fix_label',style={'color':"Blue"}),
    dcc.Dropdown(
        id='player1', 
        value='Riyad Mahrez', 
        options=[{'value': x, 'label': x} 
                 for x in df.name.unique()],
        clearable=False
    ),],style={'width':'50%', 'display': 'inline-block'}), 
    html.Div([                              
    html.P("Choose Player2:",className='fix_label',style={'color':"Red"}),
    dcc.Dropdown(
        id='player2', 
        value='Pedri', 
        options=[{'value': x, 'label': x} 
                 for x in  df.name.unique() ],
        clearable=False
    ), ],style={'width':'50%', 'display': 'inline-block'})  ,
                                   dcc.Graph(id="pie-chart2"),
],),
                         html.Div(style={'backgroundColor': 'white'},children=[ 
    html.Div([
            
 html.Div([
            html.P("Median_GOALS:",className='fix_label',
                   style={
                       'textAlign': 'center',
                       'color': 'Black',
                       'fontSize': 40}),
                 

 
            html.P(str(goals_med),
                   className='fix_label',
                   style={
                       'textAlign': 'center',
                       'color': 'Red',
                       'fontSize': 45,
                       'margin-top': '-18px'},
                   ),
    ],style={'box-sizing':'border-box','border': 'solid #FFFFFF 10px','margin-right': '10em','margin-left': '0em','width': '50%','background': 'rgba(35, 57, 82, 0.45)'})
     
 , html.Div([
            html.P("Median_PLTM:",className='fix_label',
                   style={
                       'textAlign': 'center',
                       'color': 'Black',
                       'fontSize': 40}),
                 

 
            html.P(str(p_med),className='fix_label',
                   style={
                       'textAlign': 'center',
                       'color': 'Red',
                       'fontSize': 45,
                       'margin-top': '-18px'},
                   ),
    ],style={'box-sizing':'border-box','border': 'solid #FFFFFF 10px', 'margin-right': '0em','width': '50%','background': 'rgba(35, 57, 82, 0.45)'})
     
    ]
          ,className="card_container three columns",style={'display':'flex'}
        ),
        html.Div([

 html.Div([
            html.P("Median_ASSIST:",className='fix_label',
                   style={
                       'textAlign': 'center',
                       'color': 'Black',
                       'fontSize': 40}),
                 

 
            html.P(str(a_med),className='fix_label',
                   style={
                       'textAlign': 'center',
                       'color': 'Red',
                       'fontSize': 45,
                       'margin-top': '-18px'},
                   ),
    ],style={'box-sizing':'border-box','border': 'solid #FFFFFF 10px','margin-right': '10em','margin-left': '0em','width': '50%','background': 'rgba(35, 57, 82, 0.45)'})
     
 , html.Div([
            html.P("Median_YELLOW:",className='fix_label',
                   style={
                       'textAlign': 'center',
                       'color': 'Black',
                       'fontSize': 40}),
                 

 
            html.P(str(y_med),className='fix_label',
                   style={
                       'textAlign': 'center',
                       'color': 'Red',
                       'fontSize': 45,
                       'margin-top': '-18px'},
                   ),
    ],style={'box-sizing':'border-box','border': 'solid #FFFFFF 10px', 'margin-right': '0em','width': '50%','background': 'rgba(35, 57, 82, 0.45)'})
     
    ]
          ,className="card_container three columns",style={'display':'flex'}
        ),
],),],)

@app.callback(
    Output("pie-chart2", "figure"), 
    [Input("player1", "value"), 
     Input("player2", "value")])
def generate_chart2(player1, player2):
    fig = go.Figure()    
    fig.add_trace(go.Scatterpolar(
      r=(df_tmp2[df_tmp2['name']==player1].values)[0][1:6],
      theta=categories,
      fill='toself',
      name=str(player1)))
    fig.add_trace(go.Scatterpolar(
      r=(df_tmp2[df_tmp2['name']==player2].values)[0][1:6],
      theta=categories,
      fill='toself',
      name=str(player2)))
    fig.update_layout(height=500)
    
    
    fig=fig.update_traces(fill='toself')

    return fig


    
@app.callback(
    Output("box-plot", "figure"), 
    [Input("x-axis", "value"), 
     Input("y-axis", "value")])
def generate_chart(x, y):
    fig = px.box(df_tmp, x=x, y=y)
    
    return fig

@app.callback(
    [Output("bar-chart", "figure"),Output("bar-chart4", "figure")], 
    [Input("dropdown", "value"),Input("dropdown2", "value"),Input("day-slider", "value")])
def update_bar_chart(nameval,compval,month_range): 
    if('All' in nameval):
        mask=(df_tmp['Month']>=month_range[0])& (df_tmp['Month']<=month_range[1])
    else:
        mask=(df_tmp["name"] .isin(nameval))& (df_tmp['Month']>=month_range[0])& (df_tmp['Month']<=month_range[1])
    
    if(not 'All' in compval):
        mask=mask & (df_tmp["competition"] .isin(compval))
    
    df_tmp_masked=df_tmp[mask]
    
    df_tmp_masked2 = df_tmp_masked.groupby('Month').sum().sort_values(by=['Month'],ascending = True)
    df_tmp_masked2 = pd.DataFrame(data = df_tmp_masked2, columns = ['yellow','red','yellow_x2'])
    
    df_tmp_masked2=df_tmp_masked2.reset_index()
    
    df_tmp_masked = df_tmp_masked.groupby('name').sum().sort_values(by=['goals','playing_time','assists' ],ascending = False)
    df_tmp_masked = pd.DataFrame(data = df_tmp_masked, columns = ['playing_time','goals','assists'])
    
    df_tmp_masked=df_tmp_masked.reset_index()
    
    figure1=go.Figure(data= [ go.Bar(x=df_tmp_masked.name, y=df_tmp_masked.playing_time,name='playing_time'),
                              go.Bar( x=df_tmp_masked.name, y=df_tmp_masked.goals, name='goals'),
                              go.Bar(x=df_tmp_masked.name,y=df_tmp_masked.assists,name='assists')
                            
                            ],
            layout=go.Layout(title='Goals, Assists and Playing_time by Player',title_x=0.5,xaxis={'title':'Players'},yaxis={'title':'Goals, Assists and playing_time'}))
    
    figure2=go.Figure(data= [go.Scatter( x=df_tmp_masked2.Month,y=df_tmp_masked2.yellow,mode='lines+markers',name='yellow cards'),
                            go.Scatter( x=df_tmp_masked2.Month,y=df_tmp_masked2.red,mode='lines+markers',name='red cards'),
                            go.Scatter( x=df_tmp_masked2.Month,y=df_tmp_masked2.red,mode='lines+markers',name='yellow_x2') 
                            ],
             layout=go.Layout(title='Cards by Month',title_x=0.5,xaxis={'title':'Months'},yaxis={'title':'Cards'}))        
                     
            
    return [figure1,figure2]




if __name__=='__main__':
    app.run_server(host='127.0.0.1',port=4591)

