
# coding: utf-8
# Cricket Analysis

#Import required libraries
import pandas as pd 
import requests
import numpy as np



#import the data set

url = 'http://stats.espncricinfo.com/world-t20/engine/records/averages/batting.html?id=8083;type=tournament'
html = requests.get(url).content
df_list = pd.read_html(html)
df = df_list[0]
df.drop(df.columns[[9,10,11,12,13]],axis=1, inplace=True)



#strip of the Notout* character from the HS colname

df['HS'] = df['HS'].map(lambda x:x.rstrip('*'))

#Convert the values to int or float and replace missing values with Nan
df['Ave']=df.Ave.apply(pd.to_numeric, errors='coerce')
df['Inns']=df.Inns.apply(pd.to_numeric, errors='coerce')
df['NO']=df.NO.apply(pd.to_numeric, errors='coerce')
df['Runs']=df.Runs.apply(pd.to_numeric, errors='coerce')
df['HS']=df.HS.apply(pd.to_numeric, errors='coerce')
df['BF']=df.BF.apply(pd.to_numeric, errors='coerce')
df['SR']=df.SR.apply(pd.to_numeric, errors='coerce')

#drop the players with lesser than 2 innings. 
df = df[np.isfinite(df['Inns'])]
df = df[df.Inns > 2]

#Sort based on Average 
avg_based = df.sort_values(by='Ave', ascending=False)
#reset and start indexing from 1
avg_based = avg_based.reset_index(drop=True)
avg_based.index += 1 

#Import other required data

url_1= "http://stats.espncricinfo.com/ci/engine/stats/index.html?class=3;filter=advanced;host=25;orderby=batting_average;season=2013%2F14;template=results;trophy=89;type=batting;view=innings"
html_1 = requests.get(url_1).content
df_list_1 = pd.read_html(html_1)
df_1 = df_list_1[2]
df_1.index += 1 
df_1.drop(df_1.columns[[2,3,4,5,6,7,8,9,10,11,12]],axis=1, inplace=True)

url_2= "http://stats.espncricinfo.com/ci/engine/stats/index.html?class=3;filter=advanced;host=25;orderby=batting_average;page=2;season=2013%2F14;template=results;trophy=89;type=batting;view=innings"
html_2 = requests.get(url_2).content
df_list_2 = pd.read_html(html_2)
df_2 = df_list_2[2]
df_2.index += 1 
df_2.drop(df_2.columns[[2,3,4,5,6,7,8,9,10,11,12]],axis=1, inplace=True)

url_3= "http://stats.espncricinfo.com/ci/engine/stats/index.html?class=3;filter=advanced;host=25;orderby=batting_average;page=3;season=2013%2F14;template=results;trophy=89;type=batting;view=innings"
html_3 = requests.get(url_3).content
df_list_3 = pd.read_html(html_3)
df_3 = df_list_3[2]
df_3.index += 1 
df_3.drop(df_3.columns[[2,3,4,5,6,7,8,9,10,11,12]],axis=1, inplace=True)

url_4= "http://stats.espncricinfo.com/ci/engine/stats/index.html?class=3;filter=advanced;host=25;orderby=batting_average;page=4;season=2013%2F14;template=results;trophy=89;type=batting;view=innings"
html_4 = requests.get(url_4).content
df_list_4 = pd.read_html(html_4)
df_4 = df_list_4[2]
df_4.index += 1
df_4.drop(df_4.columns[[2,3,4,5,6,7,8,9,10,11,12]],axis=1, inplace=True)

url_5= "http://stats.espncricinfo.com/ci/engine/stats/index.html?class=3;filter=advanced;host=25;orderby=batting_average;page=5;season=2013%2F14;template=results;trophy=89;type=batting;view=innings"
html_5 = requests.get(url_5).content
df_list_5 = pd.read_html(html_5)
df_5 = df_list_5[2]
df_5.index += 1 
df_5.drop(df_5.columns[[2,3,4,5,6,7,8,9,10,11,12]],axis=1, inplace=True)

url_6= "http://stats.espncricinfo.com/ci/engine/stats/index.html?class=3;filter=advanced;host=25;orderby=batting_average;page=6;season=2013%2F14;template=results;trophy=89;type=batting;view=innings"
html_6 = requests.get(url_6).content
df_list_6 = pd.read_html(html_6)
df_6 = df_list_6[2]
df_6.index += 1 
df_6.drop(df_6.columns[[2,3,4,5,6,7,8,9,10,11,12]],axis=1, inplace=True)

url_7= "http://stats.espncricinfo.com/ci/engine/stats/index.html?class=3;filter=advanced;host=25;orderby=batting_average;page=7;season=2013%2F14;template=results;trophy=89;type=batting;view=innings"
html_7 = requests.get(url_7).content
df_list_7 = pd.read_html(html_7)
df_7 = df_list_7[2]
df_7.index += 1
df_7.drop(df_7.columns[[2,3,4,5,6,7,8,9,10,11,12]],axis=1, inplace=True)

url_8= "http://stats.espncricinfo.com/ci/engine/stats/index.html?class=3;filter=advanced;host=25;orderby=batting_average;page=8;season=2013%2F14;template=results;trophy=89;type=batting;view=innings"
html_8 = requests.get(url_8).content
df_list_8 = pd.read_html(html_8)
df_8 = df_list_8[2]
df_8.index += 1 
df_8.drop(df_8.columns[[2,3,4,5,6,7,8,9,10,11,12]],axis=1, inplace=True)

url_9= "http://stats.espncricinfo.com/ci/engine/stats/index.html?class=3;filter=advanced;host=25;orderby=batting_average;page=9;season=2013%2F14;template=results;trophy=89;type=batting;view=innings"
html_9 = requests.get(url_9).content
df_list_9 = pd.read_html(html_9)
df_9 = df_list_9[2]
df_9.index += 1 
df_9.drop(df_9.columns[[2,3,4,5,6,7,8,9,10,11,12]],axis=1, inplace=True)


url_10="http://stats.espncricinfo.com/ci/engine/stats/index.html?class=3;filter=advanced;host=25;orderby=batting_average;page=10;season=2013%2F14;template=results;trophy=89;type=batting;view=innings"
html_10 = requests.get(url_10).content
df_list_10 = pd.read_html(html_10)
df_10 = df_list_10[2]
df_10.index += 1 
df_10.drop(df_10.columns[[2,3,4,5,6,7,8,9,10,11,12]],axis=1, inplace=True)


#merge all the dataframe together in a row
frames = [df_1, df_2, df_3, df_4,df_5,df_6,df_7,df_8,df_9,df_10,]
result = pd.concat(frames)
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
out_scores['Inns_1']=out_scores.Inns_1.apply(pd.to_numeric, errors='coerce')
out_scores['Inns_2']=out_scores.Inns_2.apply(pd.to_numeric, errors='coerce')
out_scores['Inns_3']=out_scores.Inns_3.apply(pd.to_numeric, errors='coerce')
out_scores['Inns_4']=out_scores.Inns_4.apply(pd.to_numeric, errors='coerce')
out_scores['Inns_5']=out_scores.Inns_5.apply(pd.to_numeric, errors='coerce')
out_scores['Inns_6']=out_scores.Inns_6.apply(pd.to_numeric, errors='coerce')
out_scores['Inns_7']=out_scores.Inns_7.apply(pd.to_numeric, errors='coerce')


out_scores['Total'] = out_scores.sum(axis=1)

#-------------------------------
all_scores=more_than_two_inns[:]
all_scores = all_scores.replace(np.nan, '', regex=True)

all_scores['Inns_1'] = all_scores['Inns_1'].map(lambda x:x.rstrip('*'))
all_scores['Inns_2'] = all_scores['Inns_2'].map(lambda x:x.rstrip('*'))
all_scores['Inns_3'] = all_scores['Inns_3'].map(lambda x:x.rstrip('*'))
all_scores['Inns_4'] = all_scores['Inns_4'].map(lambda x:x.rstrip('*'))
all_scores['Inns_5'] = all_scores['Inns_5'].map(lambda x:x.rstrip('*'))
all_scores['Inns_6'] = all_scores['Inns_6'].map(lambda x:x.rstrip('*'))
all_scores['Inns_7'] = all_scores['Inns_7'].map(lambda x:x.rstrip('*'))


all_scores['Inns_1']= pd.to_numeric(all_scores.Inns_1).astype(float)
all_scores['Inns_2']= pd.to_numeric(all_scores.Inns_2).astype(float)
all_scores['Inns_3']= pd.to_numeric(all_scores.Inns_3).astype(float)
all_scores['Inns_4']= pd.to_numeric(all_scores.Inns_4).astype(float)
all_scores['Inns_5']= pd.to_numeric(all_scores.Inns_5).astype(float)
all_scores['Inns_6']= pd.to_numeric(all_scores.Inns_6).astype(float)
all_scores['Inns_7']= pd.to_numeric(all_scores.Inns_7).astype(float)
all_scores['Total_runs']= all_scores.iloc[:, 1:-1].sum(axis=1)


all_scores= all_scores.replace(np.nan, '', regex=True)

result_1 = pd.concat([out_scores, all_scores], axis=1, sort=False)

result_1.columns= ['Player',"","","","","","","",'Sumout','Player_1',"1","2","3","4","5","6","7","Total Runs"]

result_1=result_1.drop(result_1.columns[[1,2,3,4,5,6,7,9]],axis=1)

#rearrange the columns
result_1= result_1[['Player', '1', '2', '3','4','5','6','7','Sumout','Total Runs']]

#Finding the total Not-Out Runs by substracting out runs from Total runs
result_1['Sumno']= result_1['Total Runs']-result_1['Sumout']


#sort the initial dataframe alphabhetically
df_main=df.sort_values('Player', ascending=True)

#Mergedf
df_main = pd.merge(df_main, result_1, on='Player', how='right')

df_main.drop(df_main.columns[[1,4,5,7]],axis=1, inplace=True)


#calculate e2
df_main['e2']= (df_main.Sumout + 2*(df_main.Sumno))/df_main.Inns

#calculate f6
avno= (df_main.Sumno/df_main.NO)

avno = avno.replace(np.nan, '0', regex=True)
avno=avno.apply(pd.to_numeric, errors='coerce')

f6=2.2-0.01*avno

#calculate e6 = (sumout + f6×sumno)/n where f6 = 2.2 – 0.01×avno. 
df_main['e6']=(df_main.Sumout+f6*df_main.Sumno)/df_main.Inns

 #calculate e26
df_main['e26']=(df_main.e2+df_main.e6)/2

#SR average

ASR=df_main.SR.sum(axis=0)/209

#calculate BP wher BP26 = e26 ×RP = e26×(SR/124.0)0.5 

df_main['BP26'] = df_main.e26*(df_main.SR/ASR)**0.5


main_table=df_main[:]

main_table.drop(main_table.columns[[1,4,5,6,7,8,9,10,11]],axis=1, inplace=True)
main_table = main_table.sort_values(by='BP26', ascending=False)
main_table = main_table.reset_index(drop=True)
main_table.index += 1 


print(main_table)




