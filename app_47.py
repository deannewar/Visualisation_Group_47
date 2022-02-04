

from turtle import title
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
import os


url_data = (r'https://raw.githubusercontent.com/oderofrancis/rona/main/Countries-Continents.csv')

df = pd.read_csv(url_data)



app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])


GITHUB_LINK = os.environ.get(
    "GITHUB_LINK",
    "https://github.com/deannewar/Visualisation_Group_47",
)


app.layout = html.Div([
    #html.Img(src='/assets/bgGrey.png', style={'width':"100%", 'height':"100%", 'margin':'0px'}),
                
                html.A(
                    " View on GitHub ",
                    href=GITHUB_LINK,
                    target="_blank",
                    style={
                        "border":"1px rgba(90, 90, 90) solid",
                        "borderRadius": "5px", 
                        "overflow": "hidden",
                        'margin-left': '30px', 'margin-top': '40px', 'text-align':'center',
                        'width': '7%',
                        'height': '5%',
                        'color':'rgba(26,26,26)',
                        'backgroundColor':	'rgb(255,255,255)'
                    }
                ),

                html.H1(children="Visualization Tool Group 47",className="header",
                        style={
                            'paddingTop': '2rem',
                            'color':'rgba(153, 160, 161)',
                            'text-align':'center',
                            'font_size': '26px'
                            }),
                html.P(
                        children="Visualization tool for road accidents in Great Britain in 2015",
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
                                {'label': 'Fatal (1)', 'value': '1'},
                                {'label': 'Serious (2) ', 'value': '2'},
                                {'label': 'Slight (3) ', 'value': '3'}
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
                                {'label': 'All junctions', 'value': '10'},
                                {'label': 'Roundabout (1)', 'value': '1'},
                                {'label': 'Mini roundabout (2)', 'value': '2'},
                                {'label': 'T or staggered junction (3)', 'value': '3'},
                                {'label': 'Slip road (5)', 'value': '5'},
                                {'label': 'Crossroads (6)', 'value': '6'},
                                {'label': 'Junction more than four arms (not RAB) (7)', 'value': '7'},
                                {'label': 'Using private drive or entrance (8)', 'value': '8'},
                                {'label': 'Other junction (9)', 'value': '9'}
                            ], value='10'


                        ),


                    ],style={
                        'backgroundColor': 'rgb(26,26,26)',
                        'color':'rgba(153, 160, 161)',
                        'height':'520px',
                        'margin-left':'20px',
                        'text-align':'center',
                        'width':'15%',
                        'display':'inline-block',
                        'vertical-align': 'top',
                        "border":"2px rgba(90, 90, 90) solid",
                        "borderRadius": "10px",
                        'boxShadow': '#383737 4px 4px 2px'
                }),


                 
                ##### Map BOX
                html.Div(children=
                dcc.Graph(id='map-data'),className="box2",
                        style={
                        'backgroundColor': 'rgb(26,26,26)',
                        'color':'rgba(153, 160, 161)',
                        'height':'520px',
                        'margin-left':'17px',
                        'margin-right':'10px',
                        'margin-top':'auto',
                        'text-align':'center',
                        'width':'auto',
                        'display':'inline-block',
                        'vertical-align': 'left',
                        "border":"2px rgba(90, 90, 90) solid",
                        "borderRadius": "10px", 
                        "overflow": "hidden",
                        'boxShadow': '#383737 4px 4px 2px'
                        }
                
                ),

                
                
                html.Div(children= 
                    dcc.Graph(id="bar-chart"),className="bar-chart",
                        style={
                            'backgroundColor':'rgba(100, 110, 125)',
                            'color':'rgba(153, 160, 161)',
                            'height':'auto',
                            'margin-left':'10px',
                            'margin-right':'15px',
                            'text-align':'center',
                            'width':'30%',
                            'display':'inline-block',
                            'vertical-align': 'top',
                            "border":"2px rgba(90, 90, 90) solid",
                            "margin-bottom": "15px",
                            "borderRadius": "10px", 
                            "overflow": "hidden",
                            'boxShadow': '#383737 4px 4px 2px'
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
                            'margin-left':'20px',
                            'margin-right':'15px',
                            'margin-top':'40px',
                            'width':'45%',
                            'text-align':'center',
                            'display':'inline-block',
                            'vertical-align': 'top',
                            "border":"2px rgba(90, 90, 90) solid",
                            "margin-bottom": "15px",
                            "borderRadius": "10px", 
                            "overflow": "hidden",
                            'boxShadow': '#383737 4px 4px 2px'
                    }),

                    html.Div(children= 
                    dcc.Graph(id="amount-bar"),className="amount-chart",
                        style={
                            'backgroundColor':'rgba(100, 110, 125)',
                            'color':'rgba(153, 160, 161)',
                            'height':'auto',
                            'margin-right':'10px',
                            'margin-left':'15px',
                            'margin-top':'40px',
                            'text-align':'center',
                            'width':'49%',
                            'display':'inline-block',
                            'vertical-align': 'top',
                            "border":"2px rgba(90, 90, 90) solid",
                            "margin-bottom": "15px",
                            "borderRadius": "10px", 
                            "overflow": "hidden",
                            'boxShadow': '#383737 4px 4px 2px'
                    }),
                    
                    ##### bar chart junct_det/Amount #####
                    

                   
                    
                    
            ])  
             
      ], style={'backgroundImage': 'url(/assets/bgBlack.png)', 
    'backgroundRepeat': 'no-repeat', 
    'backgroundPosition': 'center', 'backgroundSize': 'cover',  'width':'100%', 'height': '100%', 'margin-left': 0,'margin-top': 0})

@app.callback(
    Output('amount-bar', 'figure'),
    Input('input_cas_sev', 'value'))
   

def update_bar_amount(input_cas_sev):
    df_amoutns = df['Junction_Detail'].value_counts()/1000
    df_new = df[['Junction_Detail', 'Casualty_Severity']] 

    

            
    df_1 = pd.DataFrame(
    {'Junction Details': [
            '3',
            '6',
            '1',
            '8',
            '9',
            '5',
            '2',
            '7'], 
        'Amount per Junction Detail (x1000)': df_amoutns
        })

        


    fig = px.bar( df_1, x="Junction Details",y = 'Amount per Junction Detail (x1000)',
    color_discrete_sequence=["#e32e27","#FFA15A","#636EFA","#FF6692","#B6E880", "#AB63FA","#EF553B","#19D3F3"],
              
                
    category_orders={"Junction_Details": ['3','6', '1', '8','9','5', '2', '7']},
    title="Amount of Accidents per Junction Detail (x1000)",
    hover_data= {   
            "Junction Details": True,
            'Amount per Junction Detail (x1000)': True

            })

    fig.update_layout(title_font_color="#99A1A6", font_color="#99A1A6")
    fig.update_yaxes(title_font_color="#99A1A6", color="#99A1A6")
    fig.update_xaxes(title_font_color="#99A1A6", color="#99A1A6")
    
    fig.update_layout(paper_bgcolor = 'rgb(26,26,26)',plot_bgcolor='rgb(26,26,26)')
    fig.update_layout(showlegend=False),
   

    return fig



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

    if (int(input_jun_det) == 10):
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
        width = 580,
        zoom = 5,
        title="Interactive Map of Accidents in Great Britain",
        opacity = 0.6,
        
        hover_data= {   
            "Latitude": True,
            "Longitude": True,
            "Age_of_Driver": True, 
            "Casualty_Severity": True,
            })
    fig.update_layout(mapbox_style="dark")
    fig.update_layout(paper_bgcolor = 'rgb(26,26,26)' )
    fig.update_layout(title_font_color="#99A1A6", font_color="#99A1A6")
    fig.update_yaxes(title_font_color="#99A1A6", color="#99A1A6")
    fig.update_xaxes(title_font_color="#99A1A6", color="#99A1A6")
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
    if (int(input_jun_det) == 10):
        newdf2 = df
    else:
        newdf2 = df.loc[df["Junction_Detail"] == int(input_jun_det)]

    # for i in range(len(newdf.head(20))):
    #     print(newdf[:][i])
    #     print(type(newdf["Junction_Control"][i]))
    print(type(input_jun_det))
    #print(newdf.head(20))
    dfs = newdf2.groupby(by=["Junction_Control", "Casualty_Severity"]).size().reset_index(name="Amount")
    fig = px.bar( dfs,  barmode="group", x="Junction_Control",y = "Amount", color="Casualty_Severity",
        color_continuous_scale= 'reds_r',
        color_continuous_midpoint=2,
        height=497,
        title="Casualty Severity per Junction Detail")
    fig.update_layout(paper_bgcolor = 'rgb(26,26,26)',plot_bgcolor='rgb(26,26,26)')
    fig.update_layout(title_font_color="#99A1A6", font_color="#99A1A6")
    fig.update_yaxes(title_font_color="#99A1A6", color="#99A1A6", type="log", range=[0,5])
    fig.update_xaxes(title_font_color="#99A1A6", color="#99A1A6")

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

    if (len(input_cas_sev) == 0):
        newdf = []
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
    fig = px.line(dfs, x="Time", y="counts", color="Junction_Detail", title="Mean Amount of Accidents per Junction Detail over Time")

    
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
    fig.update_layout(title_font_color="#99A1A6", font_color="#99A1A6")
    fig.update_yaxes(title_font_color="#99A1A6", color="#99A1A6")
    fig.update_xaxes(title_font_color="#99A1A6", color="#99A1A6")


    return fig
if __name__ == '__main__':
    app.run_server(debug=True)
