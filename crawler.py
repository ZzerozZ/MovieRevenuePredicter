#!/opt/anaconda2/envs/ py35
# -*- coding: utf-8 -*-
"""
Created on Wed Nov.28 2018

@author: nghiadt 
"""


from conf import *


def get_movie_info(driver, url, num_actor=-1):   
    """
    Get informations of movie

    Parameters
    ----------
        - driver: a webdriver
        - url: url of movie info in boxofficemojo.com
        - num_actor: number of maximum actor to get,
                     default: -1 (get all)

    Returns
    -------
    Dictionary of movie info
    Format:  {'name':'',
         'revenue':'',
         'release_date':'',
         'genre':'',
         'runtime':'',
         'mpaa_rating':'',
         'budget':'',
         'director':'',
         'writer':'',
         'actor':'',
        }
    """

    movie = {'name':'',
         'revenue':'',
         'release_date':'',
         'genre':'',
         'runtime':'',
         'mpaa_rating':'',
         'budget':'',
         'director':'',
         'writer':'',
         'actor':'',
        }
    # Get URL:
    driver.get(url)

    # Get movie info:
    movie['name'] = driver.find_element_by_xpath(XPATHS['name']).text.replace('\n', ' ')
    movie['revenue'] = driver.find_element_by_xpath(XPATHS['revenue']).text
    movie['release_date'] = driver.find_element_by_xpath(XPATHS['release_date']).text
    movie['genre'] = driver.find_element_by_xpath(XPATHS['genre']).text
    movie['runtime'] = driver.find_element_by_xpath(XPATHS['runtime']).text
    movie['mpaa_rating'] = driver.find_element_by_xpath(XPATHS['mpaa_rating']).text
    movie['budget'] = driver.find_element_by_xpath(XPATHS['budget']).text
    
    movie['director'] = [e.get_attribute('href') for e in driver.find_elements_by_xpath(XPATHS['director'])]
    movie['writer'] = [e.get_attribute('href') for e in driver.find_elements_by_xpath(XPATHS['writer'])]
    movie['actor'] = [e.get_attribute('href') for e in driver.find_elements_by_xpath(XPATHS['actor'])]

    # Filter actors:
    if num_actor > 0 and len(movie['actor']) > num_actor:
        movie['actor'] = movie['actor'][:5]

    # Return movie information:
    return movie



if __name__ == '__main__':
    print ('Start crawling...')
    driver = webdriver.Chrome()

    movies = pd.read_csv('movie.txt', header=None).values.ravel()

    round = 1

    for movie in movies:
        try:
            movie_info = get_movie_info(driver, movie, num_actor=5)
            with open('Data/%s.dict'%movie[41:-4], 'w') as f:
                f.write(str(movie_info))

            time.sleep(np.random.randint(1,4))

            # Reset driver:
            if round % 100 == 0:
                driver.close()
                del driver
                time.sleep(60)            
                driver = webdriver.Chrome()

            round += 1
        except:
            with open('exceptions.txt', 'a+') as f_except:
                f_except.write(movie + '\n')

    print ('Done')
