import requests
from bs4 import BeautifulSoup

def extract(url):

    '''

    This function will allow us to extract the information of the website 
    we want to scrap with just using the URL.

    The first line gets the info from the url usign request.get

    The second line turns the response into a soup element

    It is important to give the result a name, so that we can follow
    the rest of the progress

    '''
    
    response = requests.get(url, 'lxml')
    
    soup = BeautifulSoup(response.content)
    
    return soup




def findall_artists(x):

    ''' 
    This funtion will allow us to extract the names of the artists
    that made the song

    The only variable we have to use is the soup element we obtained
    using the result from the previous function (extract)

    In this case, we are going to give the result obtained the name 'author', 
    a standarized name that we will use in another function (dataframe)

    '''


    y = x.find_all('span', class_ = 'artists-albums')
    
    return [i.text for i in y]




def findall_title(x):

    '''
    This function receives the same argument as findall_artists, but instead of
    obtaining the artists name, we get the name of the song.

    The result of this function will be given the name of title.

    '''
    
    y = x.find_all('span', class_ = 'track-name')
    
    return [i.text for i in y]



