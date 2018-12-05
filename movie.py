#!/opt/anaconda2/envs/ py35
# -*- coding: utf-8 -*-
"""
Created on Wed Dec.01 2018

@author: nghiadt 
"""

from xpath import *
from chrome_crawler import Chrome_Crawler

CHROME_OPTION = webdriver.ChromeOptions()
CHROME_OPTION.add_argument("headless")

MOVIE = 'https://www.boxofficemojo.com/movies/?id=%s.htm'



class Movie_Crawler(Chrome_Crawler):
    """
    Docstring
    """
    def __init__(self):
        super().__init__()


    def get_movie_info(self, movie_id, num_actor=-1):
        """
        Get informations of movie

        Parameters
        ----------
            - movie_id: id of movie in boxofficemojo.com
            - num_actor: number of maximum actor to get,
                        default: -1 (get all)

        Returns
        -------
        Dictionary of movie info
        Format:  {
                'id':'',
                'name':'',
                'domestic':'',
                'revenue':'',
                'release_date':'',
                'genre':'',
                'runtime':'',
                'mpaa_rating':'',
                'budget':'',
                'director':'',
                'writer':'',
                'actor':'',
                'actor':'',
                'producer':'',
                'lastseen':''
            }
        """

        movie = {
                'id':'',
                'name':'',
                'domestic':'',
                'revenue':'',
                'release_date':'',
                'genre':'',
                'runtime':'',
                'mpaa_rating':'',
                'budget':'',
                'director':'',
                'writer':'',
                'actor':'',
                'producer':'',
                'lastseen':''
            }
        # Get URL:
        url = MOVIE%movie_id
        movie['id'] = movie_id
        self.driver.get(url)

        multival_feats = ['director', 'writer', 'actor', 'producer']
        for feature in np.setdiff1d(list(MOVIE_XPATH.keys()), multival_feats):
            try:
                if feature != 'composer':
                    movie[feature] = self.driver.find_element_by_xpath(MOVIE_XPATH[feature]).text
                else:
                    movie['composer'] = self.driver.find_element_by_xpath(MOVIE_XPATH['composer']).get_attribute('href')
            except:
                movie[feature] = '-'
        
        for feature in multival_feats:
            try:
                movie[feature] = [e.get_attribute('href') for e in self.driver.find_elements_by_xpath(MOVIE_XPATH[feature])]
            except:
                movie[feature] = []

        # Filter actors:
        if num_actor > 0 and len(movie['actor']) > num_actor:
            movie['actor'] = movie['actor'][:num_actor]

        # Return movie information:
        return movie
