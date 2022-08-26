import json

youtube_playlist=json.load(open('youtube-playlist-item.json'))

#print the keys within the dict
#print(youtube_playlist.keys())

# Get the content of the items.
# print(youtube_playlist['items'][0]['etag'])

# print(youtube_playlist['items'][0]['contentDetails'])

for playlist_item in youtube_playlist['items']:
    print(playlist_item['kind'])
    print(playlist_item['contentDetails']['videoId'])