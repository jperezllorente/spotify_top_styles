
import pandas as pd

def dataframe(x,y):
    
    ''' 
    This function combines the results from the two previous ones with the objective
    to create a dataframe with all teh results of a ceratin playlist
    
    '''

    a = pd.DataFrame(x) 
    
    'First, we turn the author into a dataframe (pd.DataFrame)'
    
    b = pd.DataFrame(y) 
    
    'Then, we change the title into a dataframe'
    
    df = pd.concat([a,b], axis = 1) 
    
    'Finally, we concatenate both dataframes so that we have only one'
    
    df.columns = ['title','artists'] 
    
    '''
    We change the name of the colums to title and artists, names we 
    will use as standard for all dataframes

    '''
    
    return df


def add_col(x,y):

    '''
    The songs we extracted from Spotify don't have the musicl style to which they belong,
    so this information needs to be obtained manually. 

    We store the style of each song in a list called style, and we then add it to the dataframe
    keeping the name style

    '''

    x['y'] = y



def col_names(frame,x,y,z):

    '''
    When we add columns some of the names can be changed, specially the added column, so we just
    have to set them again. 

    In this function we give the dataframe and it changes its columns to what we want

    '''

    frame.columns = [x,y,z]



def add_playlist(x,y,frame):

    '''
    As we are going to be working with different playlist, it is important to identify wo which one 
    belong the songs. 

    In this function we create a colmn based on the range of the dataframe and we add the same value
    to all the fields. The value will be the name of the playlist
    
    The arguments required are the name of the playlist (x), the range of the df(y) and the df in which
    we want to add the new column

    '''

    playlist = [x for i in range(y)]
    
    frame['playlist'] = playlist



def perce(frame, total):

    '''
    The final addition we are going to make is the percetage of each music style. This has been done so
    that we can make a quantitative analysis of the weight of each music style in each playlist. 
    
    The arguments required are the dataframe we want to work with and the total number of rows the df has. 
    The total will be used to obtain the percentage of each music style

    '''

    'We create an empty list'

    percentage = [] 
    
    'We obtain the percentage of each music style'
     
    x = dict(frame["style"].value_counts()*100/total)
    
    '''
    We iterate for each of the values in the dataframe["style"] column so that it add to the empty list 
    the corresponding percentage to each style

    '''
    
    for i in frame["style"]:
        
        percentage.append(round(x[i],2))
        
    'Finally, we add the the result to the dataframe using the add_col funtion'

    add_col(frame, percentage) 


        
