# Spotify top songs from 2019 to 2020


**Overview**

The objective of this project was to select a Kaggle dataset and complement it with information from another website. This information should be obtained thorugh the website's API or scraping.

The dataset selected form Kaggle is *Top 50 Spotify Songs - 2019*, and additional information has been obtained by scraping Spotify's website. In order to develop this project three playlist have been used: *El Top 50 de España*, *El Top 50 de Estados Unidos* and *El Top 50 Global*. 

In the process of scrapping Spotify's website a problem arose. Only information of the 30 first songs of each playlist could be obtained. 


**Sources and libraries**

Pandas, regex, BeautifulSoup, requests, matplotlib and seaborn

In order to use this libraries I have used the public documentation of each of this libraries. 


**Development**

The first part of this project is centered in importing the Kaggle dataset and obtaining the information from Spotify's playlists using *pd.read_csv* for the first one, and *requests.get()* and *BeautifulSoup(response.content)* for the latters. 

Afterwards, I have followed a process to clean and set the different dataframes with the objective of creating a final dataframe (data_final) from which the final analysis has been done. 

Finnaly, an anlysis has been done using the data_final dataframe. The analysis has been mostly visual, but it has been an included a column in wich we can see the percentage of each music style in their respective playlist. 


**Conclusions**

The results show that the most popular styles in general are: pop, hip hop, latin, reggaeton and trap. 

In 2020 there has been an increase in popularity of the hip hop and trap globally. Pop music keeps its position as most popular music style worldwide. 

In the USA, pop music and hip hop are clearly the most popular genres. 

In Spain there is a certain preference towards latin music, including reggaeton, and trap. 



