import random
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# Load the client secret JSON file
creds = Credentials.from_authorized_user_info(info="path/to/client_secret.json", scopes=["https://www.googleapis.com/auth/youtube"])

composer = input("Enter the name of a composer: ")
quantity = int(input("How long would you like your playlist to be? "))

# Use the YouTube Data API to search for videos of the composer's music
youtube = build("youtube", "v3", credentials=creds)
request = youtube.search().list(part="id,snippet", q=composer, type="video")
response = request.execute()

if not response['items']:
    print(f'No videos found for {composer}')
else:
    # Select 5 random videos from the search results
    videos = random.sample(response['items'], quantity)
    video_ids = [video['id']['videoId'] for video in videos]
    
    #Create Playlist
    playlist_name = input("Enter the name of the playlist: ")
    request = youtube.playlists().insert(
        part="snippet",
        body={
            "snippet": {
                "title": playlist_name,
                "description": f"Playlist of {composer}'s random pieces"
            }
        }
    )
    response = request.execute()
    playlist_id = response['id']
    
    # Add videos to the playlist
    for video_id in video_ids:
        request = youtube.playlistItems().insert(
            part="snippet",
            body={
                "snippet": {
                    "playlistId": playlist_id,
                    "position": 0,
                    "resourceId": {
                        "kind": "youtube#video",
                        "videoId": video_id
                    }
                }
            }
        )
        request.execute()
    print(f"Playlist created with title '{playlist_name}' and id: {playlist_id}")
