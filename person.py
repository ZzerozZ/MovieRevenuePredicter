#!/opt/anaconda2/envs/ py35
# -*- coding: utf-8 -*-
"""
Created on Wed Dec.01 2018

@author: nghiadt 
"""


# PROCESSING...



from xpath import *
from chrome_crawler import Chrome_Crawler
from lib import *

# CHROME_OPTION = webdriver.ChromeOptions()
# CHROME_OPTION.add_argument("headless")

PEOPLE = 'https://www.boxofficemojo.com/people/chart/?view=%s&id=%s.htm'

class Person_Crawler(Chrome_Crawler):
    """
    Docstring
    """
    
    def __init__(self):
        super().__init__()

    def get_list_person(self):
        # Get json movie list from folder Movies
        listMovies = os.listdir('C:\\Users\Dell\Desktop\DataScience\MovieRevenuePredicter\Movies')
        listPeople = []

        for movie in listMovies:
            # Verify movie is .json file
            if (not(movie.endswith('.json'))):
                break
            
            # Create link of movie
            url = 'C:\\Users\Dell\Desktop\DataScience\MovieRevenuePredicter\Movies\\%s' % movie
            # Get movie information
            movieInfo = json.load(open(url, 'r'))
            # Get list persons from movieInfo
            listPeople += movieInfo['director'] + movieInfo['writer'] + movieInfo['actor'] + movieInfo['producer']

        # Remove duplicated values
        people = np.unique(listPeople)
        return people
    
    # def get_person_info(self, url):
        
    #     id = url.split('id=')[1][:-4]
    #     role = url.split('view=')[1].split('&')[0]
    #     name = self.driver.find_element_by_xpath(PERSON_XPATH['name']).text
    #     average = self.driver.find_element_by_xpath(PERSON_XPATH['average']).text.split('$')[1]

    #     elements = self.driver.find_elements_by_xpath(PERSON_XPATH['movie']['date'])[1:]
    #     date = [e.text for e in elements]

    #     elements = self.driver.find_elements_by_xpath(PERSON_XPATH['movie']['title'])[1:]
    #     title = [e.get_attribute('href')[41:-4] for e in elements]


    #     elements = self.driver.find_elements_by_xpath(PERSON_XPATH['movie']['studio'])[1:]
    #     studio = [e.get_attribute('href')[51:-4] for e in elements]

    #     elements = self.driver.find_elements_by_xpath(PERSON_XPATH['movie']['lifetimeGross'])[1:]
    #     lifetimeGross = [e.text[1:].replace(',','') for e in elements]

    #     elements = self.driver.find_elements_by_xpath(PERSON_XPATH['movie']['opening'])[1:]
    #     opening = [e.text[1:].replace(',','') for e in elements]

    #     movies = pd.DataFrame({
    #         'date': date,
    #         'title': title,
    #         'studio': studio,
    #         'lifetimeGross': lifetimeGross,
    #         'opening': opening
    #     }).to_dict('records')

    #     person = {
    #         'id':id,
    #         'name':name,
    #         'role':role,
    #         'average':average,
    #         'movies':movies
    #     }

    #     return person

        

