#!/opt/anaconda2/envs/ py35
# -*- coding: utf-8 -*-
"""
Created on Wed Nov.28 2018

@author: nghiadt 
"""


from xpath import *

CHROME_OPTION = webdriver.ChromeOptions()
CHROME_OPTION.add_argument("headless")

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
            'producer':''
        }
    """

    movie = {'name':'',
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
        }
    # Get URL:
    driver.get(url)

    # Get movie info:
    movie['name']         = driver.find_element_by_xpath(MOVIE_XPATH['name']).text.replace('\n', ' ')
    movie['domestic']     = driver.find_element_by_xpath(MOVIE_XPATH['domestic']).text
    movie['revenue']      = driver.find_element_by_xpath(MOVIE_XPATH['revenue']).text
    movie['release_date'] = driver.find_element_by_xpath(MOVIE_XPATH['release_date']).text
    movie['genre']        = driver.find_element_by_xpath(MOVIE_XPATH['genre']).text
    movie['runtime']      = driver.find_element_by_xpath(MOVIE_XPATH['runtime']).text
    movie['mpaa_rating']  = driver.find_element_by_xpath(MOVIE_XPATH['mpaa_rating']).text
    movie['budget']       = driver.find_element_by_xpath(MOVIE_XPATH['budget']).text
    movie['composer']     = driver.find_element_by_xpath(MOVIE_XPATH['director']).get_attribute('href')
    
    movie['director']     = [e.get_attribute('href') for e in driver.find_elements_by_xpath(MOVIE_XPATH['director'])]
    movie['writer']       = [e.get_attribute('href') for e in driver.find_elements_by_xpath(MOVIE_XPATH['writer'])]
    movie['actor']        = [e.get_attribute('href') for e in driver.find_elements_by_xpath(MOVIE_XPATH['actor'])]
    movie['producer']     = [e.get_attribute('href') for e in driver.find_elements_by_xpath(MOVIE_XPATH['producer'])]

    # Filter actors:
    if num_actor > 0 and len(movie['actor']) > num_actor:
        movie['actor'] = movie['actor'][:num_actor]

    # Return movie information:
    return movie



if __name__ == '__main__':
    print ('Start crawling...')
    driver = webdriver.Chrome(chrome_options=CHROME_OPTION)

    movies = pd.read_csv('movie.txt', header=None).values.ravel()

    _round = 1

    for movie in movies:
        try:
            movie_info = get_movie_info(driver, movie, num_actor=5)
            
            with open('Data/%s.json'%movie[41:-4], 'w') as fp:
                json.dump(movie_info, fp)

            time.sleep(np.random.randint(1,4))

            # Reset driver:
            if _round % 100 == 0:
                print ("Crawling...\t%d/%d\n"%(_round, len(movies)))
                driver.close()
                del driver
                time.sleep(60)            
                driver = webdriver.Chrome(chrome_options=CHROME_OPTION)
            _round += 1
        except:
            with open('exceptions.txt', 'a+') as f_except:
                f_except.write(movie + '\n')

    driver.close()
    del driver
    print ('Done')


# Load json:
# import json

# columns = ['name', 'runtime', 'release_date', 'mpaa_rating', 'genre', 'budget', 'actor', 'composer', 'director', 'producer', 'writer', 'domestic', 'revenue']

# with open('/bigdata/dns/data-parse/output/nghiadt/DNS/data/avatar.json', 'r') as fp:
#     data = json.load(fp)
    
# df = pd.DataFrame.from_dict([data])
# df = df[columns]