import pprint

from decouple import config

import requests

# vars
YT_API_KEY = config('YT_API_KEY')

endpoints = {
  'playlist': 'https://youtube.googleapis.com/youtube/v3/playlistItems?part=id,snippet',
}

def get_all_uploads_playlist_id(channel_id):
  print('get all uploads playlist id')

def get_all_videos_ids(playlist_id):
  print('get all videos ids')

def get_video_details(video_id):
  print('get video details')

### 
params = {
  "key": YT_API_KEY,
  "playlistId": 'UU-b3c7kxa5vU-bnmaROgvog',
  'maxResults': 50
}

res = requests.get(url = url, params = params)

res = res.json()

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(res)