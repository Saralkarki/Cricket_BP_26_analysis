
# Cricket Analysis

#Import required libraries
import pandas as pd 
import requests
import numpy as np


#import the data set

def fetch_data_from_url(url, drop_columns,df_list_index):
    html = requests.get(url).content
    df_list = pd.read_html(html)
    df = df_list[df_list_index]
    df.index += 1 
    df.drop(df.columns[drop_columns],axis=1, inplace=True)
    return df

url = 'http://stats.espncricinfo.com/world-t20/engine/records/averages/batting.html?id=8083;type=tournament'
drop_columns= [9,10,11,12,13]
df_list_index= 0
df_1= fetch_data_from_url(url,drop_columns,df_list_index) 


def strip_asterix_from_column(dataframe,colname,remove_char):
    if dataframe[colname].dtype.kind == 'O':
        dataframe[colname]=dataframe[colname].map(lambda x:x.rstrip(remove_char))

def to_numeric (dataframe, column):
    dataframe[column]=dataframe[column].apply(pd.to_numeric, errors='coerce')

exclude_columns=['Player']

for column in df_1.columns:
    if not column in exclude_columns:
        strip_asterix_from_column(df_1,column,'*')
        to_numeric(df_1, column)
       
#drop the players with lesser than 1 innings. 
df_1 = df_1[df_1.Inns > 2]

#player ranking function
def ranking_players (dataframe,colname):
    ranking_df = dataframe.sort_values(by=colname,ascending=False).reset_index(drop=True)
    return ranking_df
#index restart function
def restart_index (dataframe):
    dataframe.index += 1
#rank according to ave
Ave_rank= ranking_players(df_1,'Ave')
restart_index (Ave_rank)


def fetch_data_from_url_1(url):
    html = requests.get(url).content
    df_list = pd.read_html(html)
    df = df_list[2]
    df.index += 1 
    df.drop(df.columns[[2,3,4,5,6,7,8,9,10,11,12]],axis=1, inplace=True)
    return df

urls = [
    "http://stats.espncricinfo.com/ci/engine/stats/index.html?class=3;filter=advanced;host=25;orderby=batting_average;season=2013%2F14;template=results;trophy=89;type=batting;view=innings"
    ,"http://stats.espncricinfo.com/ci/engine/stats/index.html?class=3;filter=advanced;host=25;orderby=batting_average;page=2;season=2013%2F14;template=results;trophy=89;type=batting;view=innings"
    ,"http://stats.espncricinfo.com/ci/engine/stats/index.html?class=3;filter=advanced;host=25;orderby=batting_average;page=3;season=2013%2F14;template=results;trophy=89;type=batting;view=innings"
    ,"http://stats.espncricinfo.com/ci/engine/stats/index.html?class=3;filter=advanced;host=25;orderby=batting_average;page=4;season=2013%2F14;template=results;trophy=89;type=batting;view=innings"
    ,"http://stats.espncricinfo.com/ci/engine/stats/index.html?class=3;filter=advanced;host=25;orderby=batting_average;page=5;season=2013%2F14;template=results;trophy=89;type=batting;view=innings"
    ,"http://stats.espncricinfo.com/ci/engine/stats/index.html?class=3;filter=advanced;host=25;orderby=batting_average;page=6;season=2013%2F14;template=results;trophy=89;type=batting;view=innings"
    ,"http://stats.espncricinfo.com/ci/engine/stats/index.html?class=3;filter=advanced;host=25;orderby=batting_average;page=7;season=2013%2F14;template=results;trophy=89;type=batting;view=innings"
    ,"http://stats.espncricinfo.com/ci/engine/stats/index.html?class=3;filter=advanced;host=25;orderby=batting_average;page=8;season=2013%2F14;template=results;trophy=89;type=batting;view=innings"
    ,"http://stats.espncricinfo.com/ci/engine/stats/index.html?class=3;filter=advanced;host=25;orderby=batting_average;page=9;season=2013%2F14;template=results;trophy=89;type=batting;view=innings"
    ,"http://stats.espncricinfo.com/ci/engine/stats/index.html?class=3;filter=advanced;host=25;orderby=batting_average;page=10;season=2013%2F14;template=results;trophy=89;type=batting;view=innings"
]

df = []

for url in urls:
    df.append(fetch_data_from_url_1(url))

#merge all the dataframe together in a row

result = pd.concat(df)

#group by player 
result= result.groupby(['Player'])['Runs'].apply(', '.join).reset_index()
result=pd.concat([result[['Player']], result['Runs'].str.split(', ', expand=True)], axis=1)
result.columns= ['Player','Inns_1','Inns_2','Inns_3','Inns_4','Inns_5','Inns_6','Inns_7']

#Drop rows with cols that have more more than two None
more_than_two_inns=result.dropna(subset=['Inns_1','Inns_2','Inns_3','Inns_4','Inns_5','Inns_6','Inns_7'], thresh=3)

#replace the nan values with blank space
more_than_two_inns = more_than_two_inns.replace(np.nan, '', regex=True)
out_scores= more_than_two_inns[:]
#ignoring the not-out scores

for column in out_scores.columns:
    if not column in exclude_columns:
        to_numeric(out_scores, column)

#Add all the out_scores
out_scores['Total'] = out_scores.sum(axis=1)
out_scores= out_scores.replace(np.nan, '', regex=True)        

all_scores=more_than_two_inns[:]
all_scores = all_scores.replace(np.nan, '', regex=True)
column_names= ['Inns_1','Inns_2', 'Inns_3', 'Inns_4','Inns_5', 'Inns_6','Inns_7']

for column in column_names:
    strip_asterix_from_column(all_scores,column,'*')
    to_numeric(all_scores, column)
        
all_scores['Total_runs']= all_scores.iloc[:, 1:-1].sum(axis=1)
all_scores= all_scores.replace(np.nan, '', regex=True)
result_1 = pd.concat([out_scores, all_scores], axis=1, sort=False)
result_1.columns= ['Player',"","","","","","","",'Sumout','Player_1',"1","2","3","4","5","6","7","Total Runs"]

result_1=result_1.drop(result_1.columns[[1,2,3,4,5,6,7,9]],axis=1)
result_1= result_1[['Player', '1', '2', '3','4','5','6','7','Sumout','Total Runs']]


result_1['Sumno']= result_1['Total Runs']-result_1['Sumout']

#sort the initial dataframe alphabhetically
df_main=df_1.sort_values('Player', ascending=True)
df_3 = pd.merge(df_main, result_1, on='Player', how='right')

df_3.drop(df_3.columns[[1,4,5,7]],axis=1, inplace=True)

#calculate e2
df_3['e2']= (df_3.Sumout + 2*(df_3.Sumno))/df_3.Inns

#calculate f6
avno= (df_3.Sumno/df_3.NO)
avno = avno.replace(np.nan, '0', regex=True)
avno=avno.apply(pd.to_numeric, errors='coerce')
f6=2.2-0.01*avno
#calculate e6 = (sumout + f6×sumno)/n where f6 = 2.2 – 0.01×avno. 
df_3['e6']=(df_3.Sumout+f6*df_3.Sumno)/df_3.Inns
#calculate e26
df_3['e26']=(df_3.e2+df_3.e6)/2
#ASR average
ASR=df_3.SR.sum(axis=0)/209

#calculate BP wher BP26 = e26 ×RP = e26×(SR/124.0)0.5 

df_3['BP26'] = df_3.e26*(df_3.SR/ASR)**0.5


main_table=df_3[:]


#Sort based on BP26

bp26_rank=ranking_players(main_table,'BP26')
bp26_rank.drop(bp26_rank.columns[[4,5,6,7,8,9,10,11]],axis=1, inplace=True)
restart_index(bp26_rank)



print (bp26_rank)

# main_table.to_csv('batting_table.csv')
# df.to_csv('batting1.csv')
# result_1.to_csv('batting_sum.csv')
# result.to_csv('batting_with_not_out_symbol')

