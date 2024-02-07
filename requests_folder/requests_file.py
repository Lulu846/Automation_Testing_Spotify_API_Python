import requests

from requests_folder.environment import token


def get_artist(artist_id=""):
    response = ""
    header = {'Authorization': token}
    response = requests.get(f'https://api.spotify.com/v1/artists/{artist_id}',headers = header)
    return response

def get_top_tracks(artist_id,country):
    header = {'Authorization': token}
    response = requests.get(f'https://api.spotify.com/v1/artists/{artist_id}/top-tracks?market={country}', headers = header)
    return response

def get_available_markets(country):
    header = {'Authorization': token}
    response = requests.get(f'https://api.spotify.com/v1/markets?markets={country}', headers = header)
    return response

def get_play_list(playlist_id):
    header = {'Authorization': token}
    response = requests.get(f'https://api.spotify.com/v1/playlists/{playlist_id}', headers = header)
    return response

def put_play_list(playlist_id,name="",collaborative="",privacy="",description=""):
    header = {'Authorization': token}
    data = {
        "name": name,
        "collaborative": collaborative,
        "public": privacy,
        "description": description
    }
    response = requests.put(f'https://api.spotify.com/v1/playlists/{playlist_id}', json=data, headers = header)
    return response

def post_play_list(user_id, name, collaborative="",privacy="",description=""):
    header = {'Authorization': token}
    data = {
        "name": name,
        "collaborative": collaborative,
        "public": privacy,
        "description": description
    }
    response = requests.post(f'https://api.spotify.com/v1/users/{user_id}/playlists', json=data, headers=header)
    return response

def post_play_list_id_tracks(playlist_id, trackid, position=""):
    header = {'Authorization': token}
    data = {
        "uris": [
            trackid
        ],
        "position": position,
    }
    response = requests.post(f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks', json=data, headers=header)
    return response

def post_create_playlist(user_id, name ="", description ="", privacy =""):
    header = {'Authorization': token}
    data = {
        "name": name,
        "description": description,
        "public": privacy
    }
    response = requests.post(f'https://api.spotify.com/v1/users/{user_id}/playlists', json=data, headers=header)
    return response








