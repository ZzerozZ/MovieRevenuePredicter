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

GENRE = 'https://www.boxofficemojo.com/genres/chart/?view=main&pagenum=%d&id=%s.htm'


class Genre_Crawler(Chrome_Crawler):
    """
    Docstring
    """
    def __init__(self):
        super().__init__()
        self.genres = self.__get_boxofficemojo_genres__()


    def __get_boxofficemojo_genres__(self, url='https://www.boxofficemojo.com/genres/'):
        self.driver.get(url)

        genres = self.driver.find_elements_by_xpath(GENRE_XPATH['genre'])
        genres = [genre.get_attribute('href')[47:-4] for genre in genres]

        return genres


    def get_all_movie_of_genre(self, genre):    
        """
        Docstring
        """
        num_elements = 100
        first_elem = '-'

        links = []
        studio_list = []
        i = 1
        try:
            while num_elements == 100:
                self.driver.get(GENRE%(i, genre))

                elems = self.driver.find_elements_by_xpath(GENRE_XPATH['movie'])[1:]
                movie_ids = [e.get_attribute('href')[41:-4] for e in elems]
                
                elems = self.driver.find_elements_by_xpath(GENRE_XPATH['studio'])[1:]
                studios = [e.get_attribute('href')[51:-4] for e in elems]
                
                if movie_ids[0] == first_elem:
                    break
                first_elem = movie_ids[0]


                links += movie_ids
                studio_list += studios

                num_elements = len(movie_ids)
                i += 1
                
            return (genre, links, studio_list)
        except:
            print('Error:', genre)
            return None


    def get_all_movies(self, delay=60):
        """
        Docstring
        """
        movies = []
        i = 1
        len_genres = len(self.genres)

        for genre in self.genres:
            movies.append(self.get_all_movie_of_genre(genre))
            print('%d/%d:'%(i, len_genres), genre)
            time.sleep(delay)
            i += 1

        return movies
