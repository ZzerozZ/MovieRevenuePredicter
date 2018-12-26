#!/opt/anaconda2/envs/ py35
# -*- coding: utf-8 -*-
"""
Created on Wed Nov.28 2018

@author: nghiadt 
"""

from lib import *



MOVIE_XPATH = {
    'name'        :'/html[1]/body[1]/div[1]/div[3]/div[2]/table[2]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/font[1]/b',
    'domestic'    :'/html[1]/body[1]/div[1]/div[3]/div[2]/table[2]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/table[1]/tbody[1]/tr[1]/td[1]/center[1]/table[1]/tbody[1]/tr[1]/td[1]/font[1]/b[1]',
    'revenue'     :'/html[1]/body[1]/div[1]/div[3]/div[2]/table[2]/tbody[1]/tr[1]/td[1]/table[2]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[2]/table[1]/tbody[1]/tr[4]/td[2]/b[1]',
    'release_date':'/html[1]/body[1]/div[1]/div[3]/div[2]/table[2]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/table[1]/tbody[1]/tr[1]/td[1]/center[1]/table[1]/tbody[1]/tr[2]/td[2]/b[1]/nobr[1]/a[1]',
    'genre'       :'/html[1]/body[1]/div[1]/div[3]/div[2]/table[2]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/table[1]/tbody[1]/tr[1]/td[1]/center[1]/table[1]/tbody[1]/tr[3]/td[1]/b[1]',
    'runtime'     :'/html[1]/body[1]/div[1]/div[3]/div[2]/table[2]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/table[1]/tbody[1]/tr[1]/td[1]/center[1]/table[1]/tbody[1]/tr[3]/td[2]/b[1]',
    'mpaa_rating' :'/html[1]/body[1]/div[1]/div[3]/div[2]/table[2]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/table[1]/tbody[1]/tr[1]/td[1]/center[1]/table[1]/tbody[1]/tr[4]/td[1]/b[1]',
    'budget'      :'/html[1]/body[1]/div[1]/div[3]/div[2]/table[2]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/table[1]/tbody[1]/tr[1]/td[1]/center[1]/table[1]/tbody[1]/tr[4]/td[2]/b[1]',
    'director'    :'/html[1]/body[1]/div[1]/div[3]/div[2]/table[2]/tbody[1]/tr[1]/td[1]/table[2]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[2]/font[1]/a',
    'writer'      :'/html[1]/body[1]/div[1]/div[3]/div[2]/table[2]/tbody[1]/tr[1]/td[1]/table[2]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[2]/font/a',
    'actor'       :'/html[1]/body[1]/div[1]/div[3]/div[2]/table[2]/tbody[1]/tr[1]/td[1]/table[2]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[2]/table[1]/tbody[1]/tr[3]/td[2]/font[1]/a',
    'producer'    :'/html[1]/body[1]/div[1]/div[3]/div[2]/table[2]/tbody[1]/tr[1]/td[1]/table[2]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[2]/table[1]/tbody[1]/tr[4]/td[2]/font[1]/a',
    'composer'    :'/html[1]/body[1]/div[1]/div[3]/div[2]/table[2]/tbody[1]/tr[1]/td[1]/table[2]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[2]/table[1]/tbody[1]/tr[5]/td[2]/font[1]',
    'lastseen'  :'/html[1]/body[1]/div[1]/div[3]/div[2]/table[2]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/table[1]/tbody[1]/tr[1]/td[1]/center[1]/table[1]/tbody[1]/tr[1]/td[1]/font[1]/font[1]'
}

GENRE_XPATH = {
    'movie' :'/html[1]/body[1]/div[1]/div[3]/div[2]/h2[1]/table[2]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr/td[2]/font[1]/a[1]',
    'studio': '/html[1]/body[1]/div[1]/div[3]/div[2]/h2[1]/table[2]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr/td[3]/font[1]/a[1]',
    'genre' : '/html[1]/body[1]/div[1]/div[3]/div[2]/table[2]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr/td[1]/font[1]/b[1]/a'
}

PERSON_XPATH = {
    'name':'/html[1]/body[1]/div[1]/div[3]/div[2]/table[2]/tbody[1]/tr[1]/td[1]/h1[1]',
    'movie': {
        'date'          :'/html[1]/body[1]/div[1]/div[3]/div[2]/table[2]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr/td[1]/font[1]',
        'title'         :'/html[1]/body[1]/div[1]/div[3]/div[2]/table[2]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr/td[2]/font[1]/a[1]',
        'studio'        :'/html[1]/body[1]/div[1]/div[3]/div[2]/table[2]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr/td[3]/font[1]/a[1]',
        'lifetimeGross' :'/html[1]/body[1]/div[1]/div[3]/div[2]/table[2]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr/td[4]/font[1]',
        'opening'       :'/html[1]/body[1]/div[1]/div[3]/div[2]/table[2]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr/td[6]/font[1]'
    },
    'average':'/html[1]/body[1]/div[1]/div[3]/div[2]/table[2]/tbody[1]/tr[1]/td[1]/font[2]/b[1]'
}