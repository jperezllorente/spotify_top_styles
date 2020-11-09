import src.cleaning as cl
import src.frame as fr
import src.scraping as sc
import pandas as pd

# KAGGLE DATASET TOP50 - top 50 songs from spotify in 2019 

# In this section we do a little cleaning of the original data (top50.csv)


data = pd.read_csv("C:\\Users\\juanp\\Ironhack\\pipelines-project\\src\\top50.csv", encoding='cp1252')


data = data.drop(["Unnamed: 0","Beats.Per.Minute", "Energy", "Danceability", "Loudness..dB..", "Liveness", "Valence.","Length.", "Acousticness..", "Speechiness.", "Popularity"], axis = 1)


fr.col_names(data, 'title','artists', 'style')

data["style"] = data["style"].replace(['canadian pop', 'dance pop', 'electropop', 'panamanian pop', 'pop house', 'australian pop'], 'pop')

data['style'] = data['style'].replace(['canadian hip hop', 'atl hip hop','r&b en espanol' ], 'hip hop')

data['style'] = data['style'].replace(['dfw rap', 'country rap' ], 'rap')

data['style'] = data['style'].replace(['reggaeton flow' ], 'reggaeton')

data

'Create and add the playlist column to the df'

fr.add_playlist('GLB_top 2019', 50, data)


'Obtain the percentage of each music style by playlist and add as column to df'

fr.perce(data, 50)

data

#EXTRACTING INFORMATION FROM SPOTIFY 


    ## TOP 30 SPAIN - top 30 songs from Spotify in 2020

url = "https://open.spotify.com/playlist/37i9dQZEVXbNFJfN1Vw8d9"

ESP = sc.extract(url)

author = sc.findall_artists(ESP)

title = sc.findall_title(ESP)

ESP_top30 = fr.dataframe(title, author)


'''
Some of the artists have an extra space and • between names, so we proceed to change them
for nothing ('')

'''

ESP_top30.artists = ESP_top30.artists.replace(to_replace = r'\s\•', value = '', regex = True)


'''
As it is explained in the frame.py, the styles have been found manually, so we have to create a list and store them inside
in order to add them to the dataframe

'''

style = ['rumbachata', 'trap', 'rumbachatea', 'latin', 'reggaeton',
         'trap', 'reggaeton', 'trap', 'latin', 'trap', 'latin', 'latin', 'reggaeton', 'reggaeton', 'latin', 
         'latin', 'latin', 'trap','reggaeton', 'latin', 'latin', 'reggaeton', 'latin', 'reggaeton', 'trap', 'rumbachata', 
          'reggaeton', 'latin', 'rap', 'trap']



'We add the style column to the df'

fr.add_col(ESP_top30, style)


'We set the column names'

fr_colnames(ESP_top50,'title','artists', 'style' )


'Create and add the playlist column to the df'

fr.add_playlist('ESP_top 2020', 30, ESP_top50)


'Obtain the percentage of each music style by playlist and add as column to df'

perce(ESP_top30, 30)





    ## TOP 30 USA - top 30 songs from Spotify in 2020

url = "https://open.spotify.com/playlist/37i9dQZEVXbLRQDuF5jeBp"

USA = sc.extract(url)

author = sc.findall_artists(USA)

title = sc.findall_title(USA)

USA_top30 = fr.dataframe(title, author)

USA_top50.artists = USA_top50.artists.replace(to_replace = r'\s\•', value = '', regex = True)


'We create the list with the music styles for the USA top songs from SPotify'

style = ['pop', 'hip hop', 'trap', 'hip hop', 'hip hop', 'hip hop', 'hip hop', 'pop', 'hip hop', 'hip hop', 'pop', 'hip hop', 
        'hip hop', 'edm', 'pop', 'hip hop', 'country', 'latin', 'rap', 'pop', 'pop', 'pop', 'pop', 'hip hop', 'pop',
        'hip hop', 'pop', 'hip hop', 'hip hop', 'pop' ]


'We add the style column to the df'

add_col(USA_top50, style)


'We set the column names'

col_names(USA_top50, 'title','artists', 'style')


'Create and add the playlist column to the df'

fr.add_playlist('USA_top 2020', 30, USA_top50)


'Obtain the percentage of each music style by playlist and add as column to df'

perce(USA_top30, 30)





    ## TOP 30 GLOBAL - top 30 songs from Spotify in 2020

url = "https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF"

GLB = sc.extract(url)

author = sc.findall_artists(GLB)

title = sc.findall_title(GLB)

GLB_top30_2020 = fr.dataframe(title, author)


GLB_top50_2020.artists = GLB_top50_2020.artists.replace(to_replace = r'\s\•', value = '', regex = True)


'Create the list with the music styles'

style = ['trap', 'pop', 'hip hop', 'hip hop', 'hip hop','pop', 'latin', 'pop', 'hip hop', 'pop', 'pop', 'hip hop', 'pop', 'edm', 
         'pop', 'latin', 'reggaeton', 'pop', 'hip hop', 'pop', 'latin', 'reggaeton', 'latin', 'hip hop', 'latin', 'pop',
         'trap', 'pop', 'pop', 'trap']


'Add the style column to the df'

add_col(GLB_top50_2020, style)


'Set column names'

GLB_top50_2020.columns = ['title', 'artists', 'style']


'Create and add the playlist column to the df'

fr.add_playlist('GLB_top 2020', 30, GLB_top30_2020)


'Obtain the percentage of each music style by playlist and add as column to df'

perce(GLB_top30_2020, 30)




# JOINING ALL DATAFRAMES INTO DATA_FINAL

frames = [data, GLB_top30_2020, ESP_top30, USA_top30]

data_final = pd.concat(frames)



#VISUALIZATION

import seaborn as sns
import matplotlib as plt


    ## COUNTPLOT OF THE MUSIC STYLES OF ALL PLAYLISTS

'''
The first thing we want to check is the which are the most popular styles in general (including the four playlists)

The results will show that the most popular music styles are: pop, hip hp, latin, reggaeton and trap

'''

sns.countplot(y="style", data=data_final, palette="icefire",
              order=data_final["style"].value_counts().iloc[:20].index)



    ## COUNTPLOT OF MUSIC STYLES COMPARISON BETWEEN 2019 AND 2020 GLOBALLY

'''

Next, we will check how the styles popularity haas changed from 2019 to 2020. In order to do this, 
we will create a subdataframe that includes only the observations of GLB_top30_2020 and data(top 2019)

'''

year_ev = data_final[data_final["playlist"].isin(['GLB_top 2020', 'GLB_top 2019'])]

'''
Afterwards, we create a countplot with style as x-axis and playlist as hue

'''

sns.countplot(y="style", data = year_ev, hue = 'playlist' ,palette="icefire",
              order=data_final["style"].value_counts().iloc[:30].index)




    ## COUNTPLOT OF MUSIC STYLES FROM SPAIN TOP 30

'''

From the plot we can observe that the most popular music styles in Spain are related to the latin style,
includin reggaeton, latin music and trap

'''

sns.countplot(ESP_top50["style"])



    ## COUNTPLOT OF MUSIC STYLES FROM SPAIN TOP 30

'''

In this case we can see that pop music and hip hop are the clear leaders in USA

'''

sns.countplot(USA_top50["style"])



## SCATTERPLOT OF THE PERCENTAGE OF EACH MUSIC STYLE IN ALL PLAYLISTS


sns.scatterplot(x="percentage", y="style", hue="playlist", data=data_final)