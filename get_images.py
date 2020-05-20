import requests
CONFIG_PATTERN = 'http://api.themoviedb.org/3/configuration?api_key={key}'
KEY = 'd03c254e45681731fe6c68a466818160'

"""
    'sizes' should be sorted in ascending order, so
        max_size = sizes[-1]
    should get the largest size as well.        
"""

IMG_PATTERN = 'http://api.themoviedb.org/3/movie/{imdbid}/images?api_key={key}' 
r = requests.get(IMG_PATTERN.format(key=KEY,imdbid='tt0095016'))
api_response = r.json()
img = api_response['backdrops'][0]['file_path']
print(img)
base_url = 'https://image.tmdb.org/t/p/'
max_size = 'w300'
rel_path = 'mc7MubOLcIw3MDvnuQFrO9psfCa.jpg'
url = 'http://d3gtl9l2a4fn1j.cloudfront.net/t/p/original/mc7MubOLcIw3MDvnuQFrO9psfCa.jpg'
url = base_url + max_size + img
print(url)