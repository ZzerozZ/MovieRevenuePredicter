#!/opt/anaconda2/envs/ py35
# -*- coding: utf-8 -*-
"""
Created on Wed Nov.28 2018

@author: nghiadt 
"""


from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

from lib import *

CHROME_OPTION = webdriver.ChromeOptions()
CHROME_OPTION.add_argument("headless")


XPATHS = {
         'name':'/html[1]/body[1]/div[1]/div[3]/div[2]/table[2]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/font[1]/b',
         'revenue':'/html[1]/body[1]/div[1]/div[3]/div[2]/table[2]/tbody[1]/tr[1]/td[1]/table[2]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[2]/table[1]/tbody[1]/tr[4]/td[2]/b[1]',
         'release_date':'/html[1]/body[1]/div[1]/div[3]/div[2]/table[2]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/table[1]/tbody[1]/tr[1]/td[1]/center[1]/table[1]/tbody[1]/tr[2]/td[2]/b[1]/nobr[1]/a[1]',
         'genre':'/html[1]/body[1]/div[1]/div[3]/div[2]/table[2]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/table[1]/tbody[1]/tr[1]/td[1]/center[1]/table[1]/tbody[1]/tr[3]/td[1]/b[1]',
         'runtime':'/html[1]/body[1]/div[1]/div[3]/div[2]/table[2]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/table[1]/tbody[1]/tr[1]/td[1]/center[1]/table[1]/tbody[1]/tr[3]/td[2]/b[1]',
         'mpaa_rating':'/html[1]/body[1]/div[1]/div[3]/div[2]/table[2]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/table[1]/tbody[1]/tr[1]/td[1]/center[1]/table[1]/tbody[1]/tr[4]/td[1]/b[1]',
         'budget':'/html[1]/body[1]/div[1]/div[3]/div[2]/table[2]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/table[1]/tbody[1]/tr[1]/td[1]/center[1]/table[1]/tbody[1]/tr[4]/td[2]/b[1]',
         'director':'/html[1]/body[1]/div[1]/div[3]/div[2]/table[2]/tbody[1]/tr[1]/td[1]/table[2]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[2]/font[1]/a',
         'writer':'/html[1]/body[1]/div[1]/div[3]/div[2]/table[2]/tbody[1]/tr[1]/td[1]/table[2]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[2]/font/a',
         'actor':'/html[1]/body[1]/div[1]/div[3]/div[2]/table[2]/tbody[1]/tr[1]/td[1]/table[2]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[2]/table[1]/tbody[1]/tr[3]/td[2]/a'
        }