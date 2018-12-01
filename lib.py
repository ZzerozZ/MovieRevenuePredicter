#!/opt/anaconda2/envs/ py35
# -*- coding: utf-8 -*-
"""
Created on Mon Sep.17 2018

@author: nghiadt 
"""

import os
import gc
import re
import csv
import json
import time
import pickle
# import resource
# import threading
# import itertools
# import subprocess
import numpy as np
import pandas as pd
# from os import walk
# import seaborn as sns
# import networkx as nx
# from lxml import html
# from statistics import mode
# import lightgbm as lgb
# import catboost as cbt
# import xgboost as xgb
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import multiprocessing as mp
# import urllib.request as urllib
import matplotlib.pyplot as plt
# from sklearn.metrics import confusion_matrix
# from sklearn.preprocessing import LabelEncoder
from datetime import datetime, timedelta, date, timezone


def save_obj(obj, file_path):
    """
    Save a python object to binary file in folder: ROOT + 'pyobj/' + file_name
    
    Params:
        + obj: object to save
        + file_name: name of binary file will be create
        
    Output: 1 if success, 0 if fail
    """
    try:
        file_save = open(file_path, 'wb')
        pickle.dump(obj, file_save, pickle.HIGHEST_PROTOCOL)
        file_save.close()
        return 1
    except:
        return 0


def load_obj(file_path):
    """
    Load a binary object which saved by save_obj function
    
    Params:
        + file_name: name of binary python object file
        
    Output: an object if success, None if fail
    """
    try:
        file_save = open(file_path, 'rb')
        return pickle.load(file_save)
    except:
        return None
