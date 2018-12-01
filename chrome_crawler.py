#!/opt/anaconda2/envs/ py35
# -*- coding: utf-8 -*-
"""
Created on Wed Dec.01 2018

@author: nghiadt 
"""

from xpath import *


GENRE = 'https://www.boxofficemojo.com/genres/chart/?view=main&pagenum=%d&id=%s.htm'


class Chrome_Crawler():
    """
    Docstring
    """
    def __init__(self):
        _chrome_option = webdriver.ChromeOptions()
        _chrome_option.add_argument("headless")
        self.chrome_option = _chrome_option
        self.driver = webdriver.Chrome(chrome_options=self.chrome_option)


    def restart_crawler(self, delay_time=0):
        """
        Restart chrome driver

        Params
        -----------
            delay_time: time delay from close to re-lauch driver, default 0
        """
        self.close()
        time.sleep(delay_time)            
        self.driver = webdriver.Chrome(chrome_options=self.chrome_option)
    
    def close(self):
        """
        Close chrome driver
        """
        self.driver.close()