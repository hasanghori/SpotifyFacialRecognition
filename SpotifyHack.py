import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
import json
mood = str(input("enter your mood")) #this will equal different string variables depending on a person's mood.
genre=str(input("what's your favorite genre"))
#could be joy, anger, sorrow, or surprise
scope = 'playlist-modify-public'
username = input("enter your spotiy username")

token = SpotifyOAuth(scope=scope,username=username)
spotifyObject = spotipy.Spotify(auth_manager=token)

#create playlist
playlist_name = input("enter a playlist name")
playlist_description = "yuh"

spotifyObject.user_playlist_create(user=username,name=playlist_name,public=True,description=playlist_description)


endpoint_url = "https://api.spotify.com/v1/recommendations?"

# OUR FILTERS
limit=10

market="US"
seed_genres=genre
target_danceability=0
target_energy=0
if mood == "joy":
    target_danceability=0.9
    target_energy=0.8
elif mood == "sorrow":
    target_danceability=0.3
    target_energy=0.5
elif mood == "surprise":
    target_danceability = 0.95
    target_energy = 0.9
else:
    target_danceability = 0.7
    target_energy = 0.7



query = f'{endpoint_url}limit={limit}&market={market}&seed_genres={seed_genres}&target_danceability={target_danceability}&target_energy={target_energy}'

response =requests.get(query,
               headers={"Content-Type":"application/json",
                        "Authorization":"Bearer BQBu3pE7PuoSkxO7rMoYgBbE00zZZA55gp2diJcT1-4tSkCljY2n5Y7VcCExLlukEBr9ZqmJxYqT4-88PYHOkljrO7tlsXX_mi1eaO3xTbAPRRJhiiSangfEfp_ckX8SAb78if0RTvhc9AAYFe_k30eRHv5Pyi4QJooX9Y-HoEr2BA7-qFWzXgLTo7hYu8YaXmQpkEI"})

json_response = response.json()
uris = []
songNames = []
listUris = []
count = int(0)
for i in json_response['tracks']:
            uris.append(i)
            #print(json.dumps(uris[0], sort_keys=4, indent=4))
            #print(uris[i]['uri'])
            listUris.append(uris[count]['uri'])
            print(f"\"{i['name']}\" by {i['artists'][0]['name']}")
            count = count + 1

prePlaylist = spotifyObject.user_playlists(user=username)
playlist = prePlaylist['items'][0]['id']

spotifyObject.user_playlist_add_tracks(user=username, playlist_id=playlist, tracks= listUris)
