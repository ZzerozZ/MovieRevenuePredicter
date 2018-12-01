# Movie Revenue Predicter

### Predict revenue of the movie

Final project of Data Science class

Members:
  - 1512345: Duong Trong Nghia
  - 1552008: Hoa Minh Luan

## Summary
____________________________________
In this project, we try to use a regression model to predict revenue of movie with its information.

We use python-selenium to collect data from [boxofficemojo](https://www.boxofficemojo.com/)'s reports and use these data as input data. 

Our predict model will be comming soon.


## Project architecture
____________________________________
  ### Python scripts:
  - **lib.py**: common library
  - **xpath.py**: *xpath* strings
  - **Run_crawl.ipynb**: Run crawler
  ### Classes
  - **Chrome_Crawler**: a google chrome driver
  - **Genre_Crawler**: *Chrome_Crawler*'s child, use to crawl list of movie id
  - **Movie_Crawler**: *Chrome_Crawler*'s child, use to crawl informations of movie
  - **...**
  ### Text files:
  - **movies.txt**: list of movie's url
  - **exception.txt**: list of failed-crawl url


## Crawler
____________________________________
As you see, in this project, we used *selenium* to collect data. You also use any tool else, but find an element by **xpath** is more easier than try to make things right with *beautifulsoup* or *scrapy* as well.

An example, with each movie, we need to collect 13 features, it's just 13 lines with selenium but with beautifulsoup, 13 lines help you collect about 5 features.

## Regression model
____________________________________


