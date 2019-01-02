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
  ### Python scripts
  - **lib.py**: common library
  - **xpath.py**: *xpath* strings
  - **Run_crawl.ipynb**: Run crawler
  ### Classes
  - **Chrome_Crawler**: a google chrome driver
  - **Genre_Crawler**: *Chrome_Crawler*'s child, use to crawl list of movie id
  - **Movie_Crawler**: *Chrome_Crawler*'s child, use to crawl informations of movie
  - **...**
  ### Text files
  - **movies.txt**: list of movie's url
  - **exception.txt**: list of failed-crawl url


## Crawler
____________________________________
As you see, in this project, we used *selenium* to collect data. You can use any tool else also, but find an element by **xpath** is more easier than try to make things right with *beautifulsoup* or *scrapy* as well.

An example, with each movie, we need to collect 13 features, it's just 13 lines with selenium but with beautifulsoup, 13 lines help you collect about 5 features.

## Regression model
____________________________________

### Features (64):

#### 1. From raw data:

##### a. Raw features (4):
- **budget**: budget money
- **genre**: movie's genre
- **mppa_rating**: MPAA rating
- **runtime**: long time of movie

##### b. Parse from rawdata (7):
- **month**: release month
- **season**: Season in year
- **movie_season**: season in movie serie
- **num_actor**: number of crawled-actor in this movie
- **num_composer**: number of crawled-composer in this movie
- **num_producer**: number of crawled-producer in this movie
- **num_writer**: number of crawled-writer in this movie

#### 2. From studio + actor/producer/...:

##### a. Studio stats (7):
- **num_film**: number of above movies
- **years**: #year from first movie
- **min**: min revenue of above movies
- **max**: max revenue of above movies
- **std**: standard revenue of above movies
- **mean**: avg. revenue of above movies
- **med**: median revenue of above movies

##### b. People stats (42):
- **num_film**: number of above movies
- **years**: #year from first movie
- 5 stats features of each information (5*8):
	- **gross**: gross revenue
	- **gross_last3**: gross revenue of last 3 movies
	- **gross_last5**: gross revenue of last 5 movies
	- **gross_top3**: gross revenue of top 3 movies (sorted by revenue)
	
	- **opening**: opening revenue
	- **opening_last3**: opening revenue of last 3 movies
	- **opening_last5**: opening revenue of last 5 movies
	- **opening_top3**: opening revenue of top 3 movies (sorted by revenue)
