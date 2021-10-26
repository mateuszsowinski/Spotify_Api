from libraries import *

albumsTab = []


def search_artist(artist):
    search_artist = spotipy.search(q='artist:' + artist, type='artist')
    items = search_artist['artists']['items']
    if len(items) > 0:
        artist = items[0]
        artist_id = artist['id']
    return artist_id


def search_albums(artist_id):
    search_album = spotipy.artist_albums(artist_id, album_type='album')
    albums = search_album['items']
    while search_album['next']:
        search_album = spotipy.next(search_album)
        albums.extend(search_album['items'])
    for album in albums:
        albumsTab.append(album['name'])
    return albumsTab
