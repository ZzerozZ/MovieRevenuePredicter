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
        self.driver.get(url)

        # Just crawl closed movie:
        try:
            movie['lastseen'] = self.driver.find_element_by_xpath(MOVIE_XPATH['lastseen']).text.replace('Domestic Total as of ', '')
        except:
            movie['lastseen'] = '-'

        movie['id']           = movie_id
        movie['name']         = self.driver.find_element_by_xpath(MOVIE_XPATH['name']).text.replace('\n', ' ')
        movie['domestic']     = self.driver.find_element_by_xpath(MOVIE_XPATH['domestic']).text
        movie['revenue']      = self.driver.find_element_by_xpath(MOVIE_XPATH['revenue']).text
        movie['release_date'] = self.driver.find_element_by_xpath(MOVIE_XPATH['release_date']).text
        movie['genre']        = self.driver.find_element_by_xpath(MOVIE_XPATH['genre']).text
        movie['runtime']      = self.driver.find_element_by_xpath(MOVIE_XPATH['runtime']).text
        movie['mpaa_rating']  = self.driver.find_element_by_xpath(MOVIE_XPATH['mpaa_rating']).text
        movie['budget']       = self.driver.find_element_by_xpath(MOVIE_XPATH['budget']).text
        movie['composer']     = self.driver.find_element_by_xpath(MOVIE_XPATH['director']).get_attribute('href')
        
        movie['director']     = [e.get_attribute('href') for e in self.driver.find_elements_by_xpath(MOVIE_XPATH['director'])]
        movie['writer']       = [e.get_attribute('href') for e in self.driver.find_elements_by_xpath(MOVIE_XPATH['writer'])]
        movie['actor']        = [e.get_attribute('href') for e in self.driver.find_elements_by_xpath(MOVIE_XPATH['actor'])]
        movie['producer']     = [e.get_attribute('href') for e in self.driver.find_elements_by_xpath(MOVIE_XPATH['producer'])]

        # Filter actors:
        if num_actor > 0 and len(movie['actor']) > num_actor:
            movie['actor'] = movie['actor'][:num_actor]

        # Return movie information:
        return movie
