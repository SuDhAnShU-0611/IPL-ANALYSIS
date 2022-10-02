from os import rename
from typing import Container
from numpy.lib.shape_base import column_stack, row_stack
import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from PIL import Image
#import matplotlib.pyplot as plt

#image = Image.open('ipl_logo.jpg')
#t.image(image, caption='VIVO IPL', width=350)
st.set_page_config(
   page_title="IPL ANALYZER",
   page_icon="📊",
   layout="wide",
   initial_sidebar_state="expanded",
)
st.title('IPL DATA ANALYZER')
st.caption('This app helps in analyzing various aspects of IPL in detail')
menu=['HOME', 'ABOUT US', 'DATA']
nav=st.sidebar.selectbox("Menu",menu)

#---*HOME PAGE*---#
if nav == 'HOME':
  with st.container():
    st.info('This is the HOME PAGE')       
    st.header('HOME PAGE')
    st.subheader('Welcome to the Home Page')
    image1 = Image.open('stadium.jpg')
    st.image(image1, caption='THE IPL FEVER', width=1150, use_column_width= True)
    st.write('Data science is the study of data to extract knowledge and insights from the data and apply knowledge and actionable insights.Here we worked on IPL Data Analysis and Visualization Project using Python where we explored the interesting insights from the data of IPL matches like most run by a player, most wicket taken by a player, and much more from IPL season 2008-2020.')
    st.write('So if you are an IPL cricket fan who loves data analysis then, this analysis is made just for you!')
    
#---*ABOUT PAGE*---#
if nav == 'ABOUT US':
   with st.container(): 
    st.header('ABOUT PAGE')
    st.subheader('Welcome to the About-Us page👥')
    st.write('The effort put by each and every team member of our group through their contribution for this fun and informative analysis that can be viewed in this page along with their respective roles they have in this group.')
    #---X---#
    #col1, col2, col3 = st.columns(3)

    #with col1:
   st.subheader('👉🏻RITIKA AGRAWAL')
   image = Image.open('ritika.jpg')
   st.image(image, caption='Ritika Agrawal', width=350, use_column_width= False)
     #---X---#
    #with col2:
   st.subheader('👉🏻SAHAJ JAIN')
   image = Image.open('sahaj.jpg')
   st.image(image, caption='Sahaj Jain', width=350, use_column_width= False)
     #---X---#
   #with col3:
   st.subheader('👉🏻SUDHANSHU DUBEY')
   image = Image.open('Sudhanshu.jpg')
   st.image(image, caption='Sudhanshu Dubey', width=350, use_column_width= False)
    


#---*DATA PAGE*---#
if nav== 'DATA':
#st.header("Match Data")
 M_data = pd.read_csv("C:/Users/sudhi/Desktop/streamlit/IPLMatch.csv") #path folder of the data file
#st.header("Ball Data")
 B_data = pd.read_csv("C:/Users/sudhi/Desktop/streamlit/IPLBall.csv") #path folder of the data file

 filter= st.sidebar.selectbox(
   "Filter",
   ("Choose","Season","Match","Batsmen","Bowler","Player Stats")
    
   )       
 if filter== 'Choose':
  with st.container(): 
   st.header('DATA PAGE')
   st.text('Welcome to the DATA page')
   st.write('Here we analyze the different aspects of our IPL Data that we can use to interpret various aspects of the sports')
   image = Image.open('ipl_trophy.jpg')
   st.image(image, caption='THE TROPHY', width=350, use_column_width= True)
   st.caption('This is the trophy for which each team prepares every year rigorously to achieve the glory and fame that the team gains after winning this beautiful trophy..')

#By using Pandas and Streamlit, you can read and upload your CSV file into your localhost.




#--SEASON DATA--
if filter== 'Season':
 with st.container():
    st.header('SEASON DATA')
    st.subheader("CITY/VENUE DATA")
    st.write('➡️The data below shows all the matches that were played between the two teams in various cities and stadiums throughout the IPL History')
    
    city1=(pd.DataFrame(M_data, columns=['city', 'venue', 'date'])) #displays the table of MATCH data
    st.write(city1)
    st.write('➡️Line chart graph indicating the city and venue for various matches')
    st.line_chart(pd.DataFrame(M_data, columns=['city', 'venue']))
    st.header("CITY DATA")
    st.write('➡️The following data shows the different cities where the IPL Matches were held')
    df=M_data['city'].unique()
    st.dataframe(df)

    M_data['Season'] = pd.DatetimeIndex(M_data['date']).year
    M_data.head()

    
    match_per_season = M_data.groupby(['Season'])['id'].count().reset_index().rename(columns={'id':'matches'})
    #st.write(pd.DataFrame(match_per_season))
    #st.columns=["Seasons","matches"]
    #st.bar_chart(match_per_season)
    #st.caption('Number of Matches in each IPL SEASONS') 
    st.subheader('TOSS WINNERS')
    st.write("➡️The data below shows number of times toss won by each team throughout the IPL History( It also includes the temporary IPL Teams):- ")
    toss=M_data['toss_winner'].value_counts() 
    st.dataframe(toss)
    st.write("➡️The graph below shows number of times toss won by each team throughout the IPL History( It also includes the temporary IPL Teams):- ")
    st.bar_chart(toss)
    

     
    season_data=M_data[['id','Season']].merge(B_data, left_on = 'id', right_on = 'id', how = 'left').drop('id', axis = 1)
    season_data.head()
    st.subheader('TOTAL RUNS PER SEASON')
    st.write("➡️The data below shows the total amount of runs scored in every season of IPl throughout the IPL History:- ")
    season=season_data.groupby(['Season'])['total_runs'].sum().reset_index()
    T_Runs=season.set_index('Season')
    T_Runs
    st.write("➡️The graph below shows the total amount of runs scored in every season of IPl throughout the IPL History:- ")
    st.bar_chart(T_Runs)


    matches_per_season1=pd.concat([match_per_season,season.iloc[:,1]],axis=1)
    matches_per_season1.set_index('Season',inplace=True)
    st.subheader('MATCHES PER SEASON') 
    st.write("➡️The graph below shows number of matches played each year throughout the IPL History( It also includes the matches played by the temporary IPL Teams):- ")
    matches_per_season1
    st.write("➡️The graph below shows number of matches played each year throughout the IPL History( It also includes the matches played by the temporary IPL Teams):- ")
    st.bar_chart(matches_per_season1['matches'])
   

    runs_per_season=pd.concat([match_per_season,season.iloc[:,1]],axis=1)
    runs_per_season[' Avg. runs scored per match']=runs_per_season['total_runs']/runs_per_season['matches']
    runs_per_season.set_index('Season',inplace=True)
    st.subheader('AVG. RUNS SCORED PER SEASON') 
    runs_per_season
    #st.bar_chart()

#----------MATCH----------# 
if filter== 'Match':
 with st.container():
    st.header("MATCH DATA")
    
    st.subheader("TEAM DATA")
    M_data = pd.read_csv("C:/Users/sudhi/Desktop/streamlit/IPLMatch.csv") #path folder of the data file
    st.write("➡️The data below shows the Toss data , Toss winner and Match winner of each match through out the IPL history, It also shows their toss winning team's decision after winning the toss:-")
    st.write(pd.DataFrame(M_data, columns=['team1', 'team2', 'toss_winner', 'toss_decision','winner'])) #displays the table of MATCH data
    df=pd.DataFrame(M_data)
    toss_Winner= df.groupby('toss_winner')
    toss_Winner.sum()
    toss = M_data['toss_winner'] == M_data['winner']
    st.write("➡️The data below represents the whether or not the teams who won the toss DID actually win the match or not for their corresponding matches in the IPL:-")
    st.dataframe(toss)
    st.write("➡️The graph below represents the whether or not the teams who won the toss DID actually win the match or not for their corresponding matches in the IPL:-")
    st._arrow_bar_chart(toss)

    
    #st.write(toss_Winner(TEAM_SELECTED))


    st.header("UMPIRE DATA")
    st.write("➡️The following data provides the umpire's data for every IPL match")
    M_data = pd.read_csv("C:/Users/sudhi/Desktop/streamlit/IPLMatch.csv") #path folder of the data file
    st.write(pd.DataFrame(M_data, columns=['umpire1', 'umpire2'])) #displays the table of MATCH data

    st.header("RESULT DATA")
    M_data = pd.read_csv("C:/Users/sudhi/Desktop/streamlit/IPLMatch.csv") #path folder of the data file
    st.write('➡️The data below shows all the final result which includes the winning teams and result margin by which these teams won:-')
    st.write(pd.DataFrame(M_data, columns=['result', 'result_margin','winner','player_of_match','method'])) #displays the table of MATCH data

    #st.write(pd.DataFrame(B_data)) #displays the table of BALL data

#----------BATSMEN----------#

if filter== 'Batsmen':
 with st.container():
    st.header("BATSMEN DATA")
    st.write('The data below shows the top batsmen in terms of their runscoring ability throughout the multiple IPL Seasons')
    with st.expander('NUMBER OF BATSMEN:') :
     value = st.slider('Select the number (increases by 5 batsmen)',  0,100,5,5)
     if value== 0:
        st.write('max batsmen selected is:', value)
     else:
        st.write('max batsmen selected:', value)
    
    runs = B_data.groupby(['batsman'])['batsman_runs'].sum().reset_index()
    runs.columns = ['Batsman', 'runs']
    
    y = runs.sort_values(by='runs', ascending = False).head(value).reset_index().drop('index', axis
        =1)
    st.write(y)
    st.write('TOP',value,"RUNSCORERS IN IPL")
    st.bar_chart(pd.DataFrame(y, columns=['runs', 'Batsmen']))
    st.area_chart(pd.DataFrame(y, columns=['batsmen', 'runs']))

#----------BOWLER----------#
if filter== 'Bowler':
 with st.container():
    st.header("BOWLER DATA")
    st.write('➡️The data below shows the top bowlers in terms of their wicket taking ability throughout the multiple IPL Seasons')
    with st.expander('NUMBER OF BOWLER:') :
     bowler_value = st.slider('Select the number',  0,100,5,5)
     if bowler_value== 0:
        st.write('max bowlers selected is:', bowler_value)
     else:
        st.write('max bowlers selected is:', bowler_value)
    
    wickets = B_data.groupby(['bowler'])['is_wicket'].sum().reset_index()
    wickets.columns = ['Bowler', 'wickets']
    
    wicket = wickets.sort_values(by='wickets', ascending = False).head(bowler_value).reset_index().drop('index', axis=1)
    st.dataframe(wicket)
    st.write("TOP",bowler_value,"WICKETAKERS IN IPL")
    st.bar_chart(pd.DataFrame(wicket, columns=['wickets'])) 

    st.area_chart(pd.DataFrame(wicket, columns=['bowler', 'wickets']))
    #----------BOWLER----------#
if filter== 'Player Stats':
 with st.container():
    st.header("PLAYERS STATISTICS")
    
    user_input = st.text_input("PLAYER NAME","Enter player's name")
    player = (B_data['batsman']==user_input)
    player['batsman']=B_data[player]
    st.header('BALL-BY-BALL DATA')
    st.write('➡️The data below represents the ball-by-ball data of the batsman that he faced throughout his IPL career')
    st.dataframe(player['batsman'])
    dismissal_kind=player['batsman']['dismissal_kind'].value_counts()
    st.header('TYPES OF DISSMISALS☝️')
    st.write('➡️The Different types of methods via which the batsman got dismissed')
    st.dataframe(dismissal_kind)
    st.bar_chart(dismissal_kind)
    st.caption('Different types of dissmisals')
    runs_kind=player['batsman']['total_runs'].value_counts()
    st.header('TYPES OF RUNS🏏')
    st.write('➡️The data below represents the different types of runs that he scored throughout his IPL career')
    st.dataframe(runs_kind)
    st.bar_chart(runs_kind)
    st.caption('Different types of runs')
    

