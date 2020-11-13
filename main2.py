import pandas as pd
import src.complete as cm


def project():

    cm.esp()

    cm.glb()

    cm.usa()

    frames = [data, GLB_top30_2020, ESP_top30, USA_top30]

    data_final = pd.concat(frames)

    return data_final


project()




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
              order=year_ev["style"].value_counts().iloc[:30].index)




    ## COUNTPLOT OF MUSIC STYLES FROM SPAIN TOP 30

'''

From the plot we can observe that the most popular music styles in Spain are related to the latin style,
includin reggaeton, latin music and trap

'''

sns.countplot(ESP_top30["style"])



    ## COUNTPLOT OF MUSIC STYLES FROM SPAIN TOP 30

'''

In this case we can see that pop music and hip hop are the clear leaders in USA

'''

sns.countplot(USA_top30["style"])



## SCATTERPLOT OF THE PERCENTAGE OF EACH MUSIC STYLE IN ALL PLAYLISTS


sns.scatterplot(x="percentage", y="style", hue="playlist", data=data_final)