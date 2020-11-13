import pandas as pd


url_esp = "https://open.spotify.com/playlist/37i9dQZEVXbNFJfN1Vw8d9"

url_usa = "https://open.spotify.com/playlist/37i9dQZEVXbLRQDuF5jeBp"

url_glb = "https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF"


#ESP top 30

def esp():
    
    ESP = sc.extract(url_esp)

    author = sc.findall_artists(ESP)

    title = sc.findall_title(ESP)

    ESP_top30 = fr.dataframe(title, author)


    #Some of the artists have an extra space and • between names, so we proceed to change them for nothing ('')

    ESP_top30.artists = ESP_top30.artists.replace(to_replace = r'\s\•', value = '', regex = True)


    #As it is explained in the frame.py, the styles have been found manually, so we have to create a list and store them inside in order to add them to the dataframe

    style = ['rumbachata', 'trap', 'rumbachatea', 'latin', 'reggaeton','trap', 'reggaeton', 'trap', 'latin', 'trap', 'latin', 'latin', 'reggaeton', 'reggaeton', 'latin', 'latin', 'latin', 'trap','reggaeton', 'latin', 'latin', 'reggaeton', 'latin', 'reggaeton', 'trap', 'rumbachata', 'reggaeton', 'latin', 'rap', 'trap']


    #We add the style column to the df

    fr.add_col(ESP_top30, style)


    #We set the column names'

    fr.col_names(ESP_top30,'title','artists', 'style' )


    'Create and add the playlist column to the df'

    fr.add_playlist('ESP_top 2020', 30, ESP_top30)


    'Obtain the percentage of each music style by playlist and add as column to df'

    fr.perce(ESP_top30, 30)

    return ESP_top30


## USA top 30

def usa():

    USA = sc.extract(url_usa)

    author = sc.findall_artists(USA)

    title = sc.findall_title(USA)

    USA_top30 = fr.dataframe(title, author)

    USA_top30.artists = USA_top30.artists.replace(to_replace = r'\s\•', value = '', regex = True)

    #We create the list with the music styles for the USA top songs from SPotify'

    style = ['pop', 'hip hop', 'trap', 'hip hop', 'hip hop', 'hip hop', 'hip hop', 'pop', 'hip hop', 'hip hop', 'pop', 'hip hop', 'hip hop', 'edm', 'pop', 'hip hop', 'country', 'latin', 'rap', 'pop', 'pop', 'pop', 'pop', 'hip hop', 'pop','hip hop', 'pop', 'hip hop', 'hip hop', 'pop' ]


    #We add the style column to the df

    fr.add_col(USA_top30, style)

    #We set the column names

    fr.col_names(USA_top30, 'title','artists', 'style')


    #Create and add the playlist column to the df

    fr.add_playlist('USA_top 2020', 30, USA_top30)


    #Obtain the percentage of each music style by playlist and add as column to df

    fr.perce(USA_top30, 30)

    return USA_top30




## Global top 30

def glb():

    GLB = sc.extract(url_glb)

    author = sc.findall_artists(GLB)

    title = sc.findall_title(GLB)

    GLB_top30_2020 = fr.dataframe(title, author)


    GLB_top30_2020.artists = GLB_top30_2020.artists.replace(to_replace = r'\s\•', value = '', regex = True)


    #Create the list with the music styles

    style = ['trap', 'pop', 'hip hop', 'hip hop', 'hip hop','pop', 'latin', 'pop', 'hip hop', 'pop', 'pop', 'hip hop', 'pop', 'edm', 'pop', 'latin', 'reggaeton', 'pop', 'hip hop', 'pop', 'latin', 'reggaeton', 'latin', 'hip hop', 'latin', 'pop','trap', 'pop', 'pop', 'trap']


    #Add the style column to the df

    fr.add_col(GLB_top30_2020, style)

    #Set column names

    fr.col_names = (GLB_top30_2020, 'title', 'artists', 'style')

    #Create and add the playlist column to the df

    fr.add_playlist('GLB_top 2020', 30, GLB_top30_2020)


    #Obtain the percentage of each music style by playlist and add as column to df

    fr.perce(GLB_top30_2020, 30)

    return GLB_top30_2020



# JOINING ALL DATAFRAMES INTO DATA_FINAL

def final_df():

    frames = [data, GLB_top30_2020, ESP_top30, USA_top30]

    data_final = pd.concat(frames)

    return data_final