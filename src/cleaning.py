import regex


def regex(x):

    '''

    This function will allow us to replace every \s\• (spce followed by a •)
    for nothing ('').
    The only variable it takes is the dataframe

    '''
    x.replace(to_replace = r'\s\•', value = '', regex = True)

