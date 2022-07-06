from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

url = "https://www.billboard.com/charts/hot-100/"

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

billboard = f"{url}{date}"

CLIENT_ID = "client_ID"
CLIENT_SECRET = "client_secret"

response = requests.get(billboard)
top100 = response.text

soup = BeautifulSoup(top100, "html.parser")
songs = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
list = [song.getText() for song in songs]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com/callback/",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist on spotify. Skipped")

# print(song_uris)

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)


sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist["id"], tracks=song_uris)
