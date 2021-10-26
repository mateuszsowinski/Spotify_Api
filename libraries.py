import json
import sys
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import config

if len(sys.argv) == 4:
    artist = str(sys.argv[1])
    fileFormat = str(sys.argv[2])
    fileName = str(sys.argv[3])
else:
    artist = str(sys.argv[1])
    fileFormat = str(sys.argv[2])

clientId = config.CLIENT_ID
secretId = config.SECRET_ID

client_credentials_manager = SpotifyClientCredentials(client_id=clientId, client_secret=secretId)
spotipy = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


