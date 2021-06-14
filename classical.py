import json
import urllib
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials


def get_artist(sp, artist_name, artist_uri):
    albums = sp.artist_albums(artist_uri)['items']
    album_uri = []
    withpreviews = []
    previews = []
    for album in albums:
        album_uri.append(album['uri'])

    for uri in album_uri:
        album_tracks = sp.album_tracks(uri)['items']
        for track in album_tracks:
            if (track['preview_url']):
                previews.append(track['preview_url'])
                withpreviews.append(track)

    return previews, withpreviews


def get_tracks(sp):
    artists = {
        "bach": "spotify:artist:5aIqB5nVVvmFsvSdExz408",
        "beethoven": "spotify:artist:2wOqMjp9TyABvtHdOSOTUS",
        "mozart":  "spotify:artist:4NJhFmfw43RLBLjQvxDuRS",
        "chopin": "spotify:artist:7y97mc3bZRFXzT2szRM4L4", 
        "schubert": "spotify:artist:2p0UyoPfYfI76PCStuXfOP" 
    }
    tracks_dic = {}
    preview_dic = {}

    for key in artists:
        print(key)
        previews, withpreviews = get_artist(sp, key, artists[key])
        tracks_dic[key] = withpreviews
        preview_dic[key] = previews

    with open('./tracks.json', 'w') as t:
        json.dump(tracks_dic, t)
    
    with open('./previews.json', 'w') as p:
        json.dump(preview_dic, p)


if __name__ == "__main__":
    cid = "0192382717fd44a18daf0f99ca2242d8"
    secret = "f92c001ce58b4f6c9476ac0da30a8fa7"
    #redirect_uri = config["spotify_auth"]["redirect_uri"]
    #audio_dir = config["path"]["audio"]

    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret) 
    token = client_credentials_manager.get_access_token()
    sp = spotipy.Spotify(token)
    #sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    #token = util.prompt_for_user_token(username='mahshid_aln', client_id=cid, client_secret=secret,redirect_uri=redirect_uri)
    
    get_tracks(sp)

