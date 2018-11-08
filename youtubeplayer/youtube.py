'''
    Obtains data on YouTube URL
'''

import os
import requests
import json

class YouTubeClient():
    # API_KEY = os.environ.get('YOUTUBE_AUTH')
    API_KEY = 'AIzaSyAIisdrMZFK-IvdgSbAFkKYi0ARdbK0YIM'
    BASE_URL = 'https://www.googleapis.com/youtube/v3/videos?'

    @staticmethod
    def get_youtube_title(id):
        title = ''
        API_KEY = 'AIzaSyAIisdrMZFK-IvdgSbAFkKYi0ARdbK0YIM'
        BASE_URL = 'https://www.googleapis.com/youtube/v3/videos?'
        response = requests.get(f'{BASE_URL}part=snippet&id={id}&key={API_KEY}')
        if response.status_code == 200:
            print(title)
            title =  response.json()['items'][0]['snippet']['title']
        return title
