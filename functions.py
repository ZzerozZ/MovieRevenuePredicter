from lib import *


def get_id(link):
  """
  Get id of movies/person from url
  
  _____
  Params:
    - link: an url to movie/person detail
    
  _____
  Note:
    Return '-' if input link is incorrect
  """
  try:
    return re.findall(r'id=(.*?).htm', link)[0]
  except:
    return '-'
  

def money_str2float(s):
  """
  Convert money string to float
  
  _____
  Params:
    - s: money string like: "$123" or "$3 million"
    
  _____
  Notes:
    Return None if input is 'N/A' or '-'
  """
  if s == '-' or s == 'N/A':
    return None
  if 'million' in s:
    return float(sub(r'[^\d.]', '', s)) * 1e6
  else:
    return float(sub(r'[^\d.]', '', s))
  
  
def parse_datetime(dt, patent='%B %d, %Y'):
  """
  Convert time string to datetime datatype
  
  _____
  Params:
    - dt: datetime string
    - patent: format of time-string, default: '%B %d, %Y'
    
  _____
  Notes:
    Return None if input time is 'N/A' or '-'
  """
  try:
    return datetime.strptime(dt, patent)
  except:
    return None
  
  
def time_str2mins(t):
  """
  Convert runtime string to number of minute
  
  _____
  Params:
    - t: timedelta like '1 hours 15 mins'
    
  _____
  Notes:
    Return None if input is 'N/A'
  """
  if t == 'N/A':
    return None
  tmp = re.findall(r'[\d]+', t)
  if len(tmp) == 1:
    return int(tmp[0])
  else:
    return int(tmp[0]) * 60 + int(tmp[1])

def get_season(month):
    """
    Get season by month
    
    _____
    Params: 
        - month: month in range 1 to 12
    """
    if month in [12,1,2]:
        return 0
    if month in [3,4,5]:
        return 1
    if month in [6,7,8]:
        return 2
    if month in [9,10,11]:
        return 3
    
def get_movie_season(name):
    """
    Get season of movies
    
    _____
    Params:
        - name: movie id
    """
    try:
        if name[-2].isalpha():
            1 / int(name[-1])
            return int(name[-1])
    except:
        return 1
    return 1


def gr_by(df, key='year', value='revenue', method='mean'):
    """
    Groupby function
    """
    return df.groupby(key).agg({value:method}).reset_index()

def date2str(_date):
    """
    Convert datetime.datetime value to date string
    
    _____
    Params:
        - _date: datetime.datetime value
    
    _____
    Example:
        Date(2018,6,17) ---> '2018-06-17'
    """
    return str(_date.day) + '/' + str(_date.month) + '/' +str(_date.year)

def str2date(s):
    """
    Convert string like 6/30/18 to datetime.datetime type like Date(2018,06,30)
    
    _____
    Params:
        - s: date string
        
    _____
    Notes:
        - input must have a year string!
    """
    date_str = s.split('/')
    try:
        if len(date_str) == 3:
            year = 2000 + int(date_str[-1])
            if year > 2018: year -= 100

            month = int(date_str[0])
            day = int(date_str[1])
        else:
            year = int(re.findall(r'[\d]+', s)[0])
            month = 6
            day = 1
        
        return date(year,month,day)
    except:
        return None

def get_person_info(person_json, to_date):
    """
    Get informations of person
    
    _____
    Params:
        - person_json: raw data of movies that this person joined
        - to_date: datatype is datetime.datetime.Date
        
    _____
    Notes:
    If no necessary information exist, this function will be returning a None vector
    """
    stats = ['avg', 'max', 'min', 'med', 'std']
    person_feats = ['num_film', 'years'] + ['gross_' + stat for stat in stats] + \
                ['gross_last3_' + stat for stat in stats] + \
                ['gross_last5_' + stat for stat in stats] + \
                ['gross_top3_' + stat for stat in stats]  +  \
                                                            \
                ['opening_' + stat for stat in stats]       + \
                ['opening_last3_' + stat for stat in stats] + \
                ['opening_last5_' + stat for stat in stats] + \
                ['opening_top3_' + stat for stat in stats]

    tmp = pd.DataFrame(person_json)
    
    # Remove bad data:
    tmp = tmp[tmp['lifetimeGross'] != '/a']
    tmp = tmp[tmp['opening'] != '/a']
    tmp = tmp[tmp['date'] != 'N/A']
    tmp['date'] = tmp['date'].apply(lambda x: str(str2date(x)))
    
    # Remove future movies:
    tmp = tmp[tmp['date'] < to_date]
    
    if tmp.empty:
        return [None]* len(person_feats)
    
    # Cast some columns to float:
    tmp.lifetimeGross = tmp.lifetimeGross.astype('float')
    tmp.opening = tmp.opening.astype('float')
    
    # Get neccessary informations:
    num_film = tmp.shape[0]
    years = 1 + int(tmp.date.values[0][:4]) - int(tmp.date.values[-1][:4])
    try:
        top3 = tmp.sort_values('lifetimeGross', ascending=False).lifetimeGross.values[2]
    except:
        top3 = tmp.lifetimeGross.min()
    
    gross = []
    opening = []
    for df in [tmp, tmp.head(3), tmp.head(5), tmp[tmp.lifetimeGross >= top3]]:
        gross += [df.lifetimeGross.values.mean(), df.lifetimeGross.values.max(),\
                df.lifetimeGross.values.min(), np.median(df.lifetimeGross.values),\
                np.std(df.lifetimeGross.values)]
        opening += [df.opening.values.mean(), df.opening.values.max(),\
                df.opening.values.min(), np.median(df.opening.values),\
                np.std(df.opening.values)]
        
    return [num_film, years] + gross + opening


def get_studio_info(studio, df_studio, to_date):
    """
    Get informations of studio
    
    _____
    Params:
        - studio: target studio, string
        - df_studio: DataFrame contains all studios
        - to_date: datatype is datetime.datetime.Date
        
    _____
    Notes:
    If no necessary information exist, this function will be returning a None vector
    """
    tmp = df_studio[df_studio['studio'] == studio]
    tmp.date = tmp.date.apply(lambda x: str(x))
    tmp = tmp[tmp['date'] < to_date]
    
    stats = ['avg', 'max', 'min', 'med', 'std']
    studio_feats = ['num_film', 'years'] + ['gross_' + stat for stat in stats] + \
                ['gross_last3_' + stat for stat in stats] + \
                ['gross_last5_' + stat for stat in stats] + \
                ['gross_top3_' + stat for stat in stats]  +  \
                                                            \
                ['opening_' + stat for stat in stats]       + \
                ['opening_last3_' + stat for stat in stats] + \
                ['opening_last5_' + stat for stat in stats] + \
                ['opening_top3_' + stat for stat in stats]
    
    # Remove bad data:
    tmp = tmp[tmp['lifetimeGross'] != '/a']
    tmp = tmp[tmp['opening'] != '/a']
    tmp = tmp[tmp['date'] != 'N/A']

    if tmp.empty:
        return [None]* len(studio_feats)
    
    # Cast some columns to float:
    tmp.lifetimeGross = tmp.lifetimeGross.astype('float')
    tmp.opening = tmp.opening.astype('float')
    tmp = tmp.sort_values('date', ascending=False)
    
    # Get neccessary informations:
    num_film = tmp.shape[0]
    years = 1 + int(tmp.date.values[0][:4]) - int(tmp.date.values[-1][:4])
    try:
        top3 = tmp.sort_values('lifetimeGross', ascending=False).lifetimeGross.values[2]
    except:
        top3 = tmp.lifetimeGross.min()
    
    gross = []
    opening = []
    for df in [tmp, tmp.head(3), tmp.head(5), tmp[tmp.lifetimeGross >= top3]]:
        gross += [df.lifetimeGross.values.mean(), df.lifetimeGross.values.max(),\
                df.lifetimeGross.values.min(), np.median(df.lifetimeGross.values),\
                np.std(df.lifetimeGross.values)]
        opening += [df.opening.values.mean(), df.opening.values.max(),\
                df.opening.values.min(), np.median(df.opening.values),\
                np.std(df.opening.values)]
        
    return [num_film, years] + gross + opening