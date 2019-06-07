def give_more_information(outcome):
    
    '''The function called give_more_information gives the users more information on the movie that Mr. Chattison recommended. Mr. Chattison will give the user a link to a website that has furthur information on the given movie.'''
    
    print('kk here is some information')

    statement = 'https://www.imdb.com/find?ref_=nv_sr_fn&q=' + 'it'+ '&s=all'
    
    #replace the given movie with 'it' so that it could return a link. 
    statement = statement.replace('it', outcome)
    
    return statement