import pprint

from decouple import config

import requests

from db import save_many

# vars
YT_API_KEY = config('YT_API_KEY')

current_videos = []

endpoints = {
  'playlist': 'https://youtube.googleapis.com/youtube/v3/playlistItems?part=id,snippet',
  'channel': 'https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails'
}

def get_all_uploads_playlist_id(channel_id):
  params = {
    'key': YT_API_KEY,
    'id': channel_id,
  }
  res = requests.get(url=endpoints['channel'], params=params)

  res = res.json()

  pl_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']

  return pl_id

def get_all_videos_ids(playlist_id, nextPageToken = None):
  global current_videos
  
  params = {
    "key": YT_API_KEY,
    "playlistId": playlist_id,
    'maxResults': 50,
    'pageToken': nextPageToken
  }

  res = requests.get(url=endpoints['playlist'], params = params)

  res = res.json()

  current_videos.extend(res['items'])

  if len(current_videos) < res['pageInfo']['totalResults']:
    return get_all_videos_ids(playlist_id, res['nextPageToken'])
  else:
    temp_videos = []

    for vid in current_videos:
      temp_videos.append({
        'publishedAt': vid['snippet']['publishedAt'],
        'videoId': vid['snippet']['resourceId']['videoId'],
        'owner': vid['snippet']['videoOwnerChannelTitle']
      })
    
    current_videos = []
    
    return temp_videos

def get_video_details(video_id):
  print('get video details')

def save_videos(channel_id):
  uploads = get_all_uploads_playlist_id(channel_id)
  vids = get_all_videos_ids(uploads)

  save_many(vids)