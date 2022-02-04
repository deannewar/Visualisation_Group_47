

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
from datetime import datetime as dt
import pandas as pd
import numpy as np
import plotly.io as pio



df = pd.read_csv('C:\\Users\\deann\\Documents\\University\\Visualization\\Visualization_Project_TU-e\\data\\Final_df1.csv')

#df = df.sort_values(by="Date", key=pd.to_datetime)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])





app.layout = html.Div([
    #html.Img(src='/assets/bgGrey.png', style={'width':"100%", 'height':"100%", 'margin':'0px'}),
                
   
                html.H1(children="England Accidents 2015",className="header",
                        style={
                            'paddingTop': '2rem',
                            'color':'rgba(153, 160, 161)',
                            'text-align':'center',
                            'font_size': '26px'
                            }),
                html.P(
                        children="Visualization tool for accidents in England",
                        style={
                            'color':'rgba(153, 160, 161)',
                            'text-align':'center',
                            'font_size': '26px'
                            }
                        ),
           
                html.Div([ 
                #####Left top box#####
                    html.Div([
                        html.H5('Filter Box', style={'paddingTop': '2rem', 'font_size':'26px', 'color':'rgba(153, 160, 161)'}),
                        ################ Date Filter ################
                        html.Label('Filter by date (M-D-Y):', style={'paddingTop': 'auto', 'font_size':'30px'}),
                        dcc.DatePickerRange(
                            id='input_date',
                            number_of_months_shown=2,
                            persistence=True,
                            month_format='DD/MM/YYYY',
                            show_outside_days=True,
                            minimum_nights=0,
                            initial_visible_month=dt(2015, 1, 1),
                            min_date_allowed=dt(2015, 1, 1),
                            max_date_allowed=dt(2015, 12, 31),
                            start_date=dt.strptime("2015-01-01", "%Y-%m-%d").date(),
                            end_date=dt.strptime("2015-12-31", "%Y-%m-%d").date(),
                            style={ 'background-color': 'rgb(26,26,26)'}
                        ),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        ################ Accident Severity Filter ################
                        html.Label('Casualty Severity:', style={'paddingTop': 'auto'}),
                        dcc.Checklist(
                            id='input_cas_sev',
                            options=[
                                {'label': 'Fatal ', 'value': '1'},
                                {'label': 'Serious ', 'value': '2'},
                                {'label': 'Slight ', 'value': '3'}
                            ],
                            value=["1","2","3"]

                        ),
                        html.Br(),
                        html.Br(),
                        html.Br(),

                        html.Label('Junction Detail:', style={'paddingTop': 'auto'}),
                        dcc.Dropdown(
                            id='input_jun_det',
                            options=[
                                {'label': 'All junctions', 'value': '0'},
                                {'label': 'Not at or within 20 metres of junction', 'value': '1'},
                                {'label': 'Roundabout', 'value': '2'},
                                {'label': 'Dual carriageway', 'value': '3'},
                                {'label': 'Mini roundabout', 'value': '4'},
                                {'label': 'T or staggered junction', 'value': '5'},
                                {'label': 'Slip road', 'value': '6'},
                                {'label': 'Crossroads', 'value': '7'},
                                {'label': 'Junction more than four arms (not RAB)', 'value': '8'},
                                {'label': 'Using private drive or entrance', 'value': '9'},
                                {'label': 'Other junction', 'value': '10'}
                            ], value='0'


                        ),


                    ],style={
                        'backgroundColor': 'rgb(26,26,26)',
                        'color':'rgba(153, 160, 161)',
                        'height':'500px',
                        'margin-left':'30px',
                        'text-align':'center',
                        'width':'15%',
                        'display':'inline-block',
                        'vertical-align': 'top',
                        "border":"2px rgba(73, 81, 92) solid",
                        "borderRadius": "10px", 
                        "overflow": "hidden"
                }),


                 
                ##### Map BOX
                html.Div(children=
                dcc.Graph(id='map-data'),className="box2",
                        style={
                        'backgroundColor': 'rgb(26,26,26)',
                        'color':'rgba(153, 160, 161)',
                        'height':'500px',
                        'margin-left':'30px',
                        'margin-right':'30px',
                        'margin-top':'auto',
                        'text-align':'center',
                        'width':'auto',
                        'display':'inline-block',
                        'vertical-align': 'left',
                        "border":"2px rgba(73, 81, 92) solid",
                        "borderRadius": "10px", 
                        "overflow": "hidden"
                }),

               

                
            ]),
            
                html.Div([
                    ##### Time Line Chart #####
                    html.Div(children=
                    dcc.Graph(id="line-chart"),className="line-chart",
                        style={
                            
                            'backgroundColor': 'rgb(26,26,26)',
                            'color':'rgba(153, 160, 161)',
                            'height':'auto',
                            'margin-left':'30px',
                            'margin-right':'15px',
                            'margin-top':'40px',
                            'width':'45%',
                            'text-align':'center',
                            'display':'inline-block',
                            'vertical-align': 'top',
                            "border":"2px rgba(73, 81, 92) solid",
                            "margin-bottom": "15px",
                            "borderRadius": "10px", 
                            "overflow": "hidden"
                    }),
                    
                    ##### bar chart junct_det/Amount #####
                    html.Div(children= 
                    dcc.Graph(id="bar-chart"),className="bar-chart",
                        style={
                            'backgroundColor':'rgba(100, 110, 125)',
                            'color':'rgba(153, 160, 161)',
                            'height':'auto',
                            'margin-right':'10px',
                            'margin-left':'15px',
                            'margin-top':'40px',
                            'text-align':'center',
                            'width':'45%',
                            'display':'inline-block',
                            'vertical-align': 'top',
                            "border":"2px rgba(73, 81, 92) solid",
                            "margin-bottom": "15px",
                            "borderRadius": "10px", 
                            "overflow": "hidden"
                    })

                   
                    
                    
            ])  
             
      ], style={'backgroundImage': 'url(/assets/bgBlack.png)', 
    'backgroundRepeat': 'no-repeat', 
    'backgroundPosition': 'center', 'backgroundSize': 'cover',  'width':'100%', 'height': '100%', 'margin-left': 0,'margin-top': 0})



@app.callback(
    Output('map-data', 'figure'),
    [
    Input('input_date', 'start_date'),
    Input('input_date', 'end_date'),
    Input('input_cas_sev', 'value'),
    Input('input_jun_det', 'value')
    ])

def update_map(start_date, end_date, input_cas_sev , input_jun_det):
    dff = df.copy()
    #dff = dff.loc[(dff['Date'] >= start_date) & (dff['Date'] <= end_date)]

    #print(int(input_cas_sev))
    #df.loc[(df['A'].isin([1, 2])) & (df['B'].isin([100])), 'C'] = "1or2and600or200"
    # if(len(input_cas_sev) == 1):
    #     newdf = dff.loc[dff["Casualty_Severity"] == int(input_cas_sev)]
    # if(len(input_cas_sev) == 2):
    #     newdf = dff.loc[dff["Casualty_Severity"].isin([int(input_cas_sev[0]),int(input_cas_sev[1])])]
    # if(len(input_cas_sev) == 3):
    #     newdf = dff.loc[dff["Casualty_Severity"].isin([int(input_cas_sev[0]),int(input_cas_sev[1])],int(input_cas_sev[2]))]

    if (len(input_cas_sev) == 1):
        newdf = dff.loc[dff["Casualty_Severity"] == int(input_cas_sev[0])]
    if (len(input_cas_sev) == 2):
        if(int(input_cas_sev[0]) == 1 and int(input_cas_sev[1]) == 2):
            newdf = dff.loc[dff["Casualty_Severity"] != 3]
        if(int(input_cas_sev[0]) == 2 and int(input_cas_sev[1]) == 3):
            newdf = dff.loc[dff["Casualty_Severity"] != 1]
        if (int(input_cas_sev[0]) == 1 and int(input_cas_sev[1]) == 3):
            newdf = dff.loc[dff["Casualty_Severity"] != 2]
    if (len(input_cas_sev) == 3):
        newdf = df

    if (int(input_jun_det) == 0):
        newdf2 = newdf
    else:
        newdf2 = newdf.loc[df["Junction_Detail"] == int(input_jun_det)]
    # if(input_jun_det):
    #     filtered_df= filtered_df[filtered_df['Junction_Detail'].isin([input_jun_det[0]])]
    px.set_mapbox_access_token('pk.eyJ1IjoiZG5ud3IiLCJhIjoiY2t6NzFjb2xrMGVhdTJxbXAwbGF0aTZzciJ9.-aAEnp5pqqY5fqh8X0GVMQ')
    

   #fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude",color="Junction_Detail", size="Casualty_Severity",
                  #color_continuous_scale=px.colors.cyclical.IceFire, size_max=20,zoom=12)
    print(input_cas_sev)
    fig = px.scatter_mapbox(
        newdf2,
        lat="Latitude", 
        lon="Longitude",
        color="Casualty_Severity",
        color_continuous_scale= 'reds_r',
        color_continuous_midpoint=2 ,
        height = 496,
        width = 1000,
        zoom = 5,
        opacity = 0.6,
        hover_data= {   
            "Latitude": True,
            "Longitude": True,
            "Age_of_Driver": True
            })
    fig.update_layout(mapbox_style="dark")
    fig.update_layout(paper_bgcolor = 'rgb(26,26,26)', )
    fig.update_layout({"title": {"text": "Map Of Accident In the UK",
                             "font": {"size": 30}}})
    return fig


@app.callback(
    Output('bar-chart', 'figure'),
    [Input('input_cas_sev', 'value'),
     Input('input_date', 'start_date'),
     Input('input_date', 'end_date'),
     Input('input_jun_det','value')])


def update_bar(input_cas_sev,start_date,end_date,input_jun_det):

    # #print(df.keys())
    # #mask = df.loc[df["Junction_Detail"] == "1"]
    # dff = df.copy()
    # dff = dff['Junction_Detail']
    # if int(dff['Junction_Detail']) == input_jun_det:
    #     dff = dff[input_jun_det]
    # #dff = dff['Junction_Detail'].where(dff['Junction_Detail'] == input_jun_det)
    # print(input_jun_det)
    # print(df)
    # for i in range(len(input_jun_det)):
    #     mask = df.loc[df["Junction_Detail" == input_jun_det]]
    #
    # #filtered_df = mask.loc[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    # #mask = filtered_df
    # #filtered_df = mask.loc[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    # #mask = filtered_df
    # for i in range(len(df.head(20))):
    #     print(df[:i])
    #     print(type(df["Junction_Control"][i]))
    if (int(input_jun_det) == 0):
        newdf2 = df
    else:
        newdf2 = df.loc[df["Junction_Detail"] == int(input_jun_det)]

    # for i in range(len(newdf.head(20))):
    #     print(newdf[:][i])
    #     print(type(newdf["Junction_Control"][i]))
    print(type(input_jun_det))
    #print(newdf.head(20))
    dfs = newdf2.groupby(by=["Junction_Control", "Casualty_Severity"]).size().reset_index(name="counts")
    fig = px.bar(dfs, x="Junction_Control",y = "counts", color="Casualty_Severity", color_continuous_scale= 'reds_r',
        color_continuous_midpoint=2 )
    fig.update_layout(paper_bgcolor = 'rgb(26,26,26)',plot_bgcolor='rgb(26,26,26)')


    return(fig)




@app.callback(
    Output('line-chart', 'figure'),
    [Input('input_cas_sev', 'value'),
     Input('input_date', 'start_date'),
     Input('input_date', 'end_date'),
     Input('input_jun_det','value')])


def update_line_chart(input_cas_sev,start_date,end_date,input_jun_det):

    dff = df.copy()
    newdf = df.copy()


    if (len(input_cas_sev) == 1):
        newdf = dff.loc[dff["Casualty_Severity"] == int(input_cas_sev[0])]
    if (len(input_cas_sev) == 2):
        if(int(input_cas_sev[0]) == 1 and int(input_cas_sev[1]) == 2):
            newdf = dff.loc[dff["Casualty_Severity"] != 3]
        if(int(input_cas_sev[0]) == 2 and int(input_cas_sev[1]) == 3):
            newdf = dff.loc[dff["Casualty_Severity"] != 1]
        if (int(input_cas_sev[0]) == 1 and int(input_cas_sev[1]) == 3):
            newdf = dff.loc[dff["Casualty_Severity"] != 2]
    if (len(input_cas_sev) == 3):
        newdf = df



    newdf['Time'] = pd.to_datetime(newdf['Time'], format='%H:%M')
    dfs = newdf.groupby(by=["Time", "Junction_Detail"]).size().reset_index(name="counts")
    fig = px.line(dfs, x="Time", y="counts", color="Junction_Detail")

    
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeslider_bgcolor='rgba(153, 160, 161)',
        tickformatstops=[
            dict(dtickrange=[None, 1000], value="%H:%M:%S.%L ms"),
            dict(dtickrange=[1000, 60000], value="%H:%M:%S s"),
            dict(dtickrange=[60000, 3600000], value="%H:%M m"),
            dict(dtickrange=[3600000, 86400000], value="%H:%M h"),
            dict(dtickrange=[86400000, 604800000], value="%e. %b d"),
            dict(dtickrange=[604800000, "M1"], value="%e. %b w"),
            dict(dtickrange=["M1", "M12"], value="%b '%y M"),
            dict(dtickrange=["M12", None], value="%Y Y")
        ]
    )
    fig.update_layout(paper_bgcolor = 'rgb(26,26,26)',plot_bgcolor='rgb(26,26,26)')
    #### legend to top of graph ###
    fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
))


    return fig
if __name__ == '__main__':
    app.run_server(debug=True)
