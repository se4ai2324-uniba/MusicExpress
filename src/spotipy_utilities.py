"""Script containing methods utilizing Spotipy APIs"""

import conf


def uri_finder(artist):
    """Method that returns an Artist's URI given its name"""
    artist_code = conf.SP.search(q='artist:' + artist, type='artist', limit=1)

    if artist_code['artists']['items']:
        artist_uri = artist_code['artists']['items'][0]['uri']
    else:
        print('Artist not found.')

    return artist_uri


def get_artist_genre_by_name(artist_name):
    """Method that returns an Artist's Genre given its name"""
    artist_uri = uri_finder(artist_name)
    artist = conf.SP.artist(artist_uri)
    genre = artist['genres']
    return ', '.join(genre)


def get_artist_genre_by_uri(artist_uri):
    """Method that returns an Artist's Genre given its URI"""
    artist = uri_finder('Sleep Token')
    artist = conf.SP.artist(artist_uri)
    genre = artist['genres']
    return ', '.join(genre)


def get_playlist_name(playlist_id):
    """Method that returns the name of a given Playlist"""
    playlist = conf.SP.playlist(playlist_id)
    return playlist['name']


def clear_playlist_name(tmp_name):
    """Methodo that removes the char "|" in the file name"""
    if '|' in tmp_name:
        return tmp_name.replace("|", "")
    return tmp_name


def track_ids_from_playlist(user, playlist_id):
    """Method that returns the IDs of every track in a given Playlist"""
    track_ids = []
    offset = 0
    limit = 100
    check_len = True

    while check_len:
        playlist = conf.SP.user_playlist_tracks(user, playlist_id,
                                                limit=limit, offset=offset)

        for elem in playlist['items']:
            track = elem['track']
            track_ids.append(track['id'])
            if len(track_ids) == 15:
                check_len = False
                break

        offset += limit
        if len(playlist['items']) < limit:
            break

    return track_ids


def get_track_features(track_id):
    """Method that returns the features of every track in a given Playlist"""
    track_details = conf.SP.track(track_id)
    track_features = conf.SP.audio_features(track_id)

    # Track Info
    name = track_details['name']
    artist = track_details['artists'][0]['name']

    # Track Features
    energy = track_features[0]['energy']
    liveness = track_features[0]['liveness']
    loudness = track_features[0]['loudness']

    track_info = [name, artist, energy, liveness, loudness]

    return track_info


def get_track_preview(track_name, artist_name):
    """Method that returns the link to the preview of the track"""
    query = f"track:{track_name} artist:{artist_name}"
    results = conf.SP.search(q=query, type='track')

    for track in results['tracks']['items']:
        if track['name'].lower() == track_name.lower():
            artists = [artist['name'].lower() for artist in track['artists']]
            if artist_name.lower() in artists:
                track_id = track['id']
                track_info = conf.SP.track(track_id)
                preview_url = track_info['preview_url']
                return preview_url

    return None


def get_playlist_id(playlist_name):
    """Method to retrieve playlist id given its name"""
    results = conf.SP.search(q=playlist_name, type='playlist', limit=1)
    if results['playlists']['items']:
        playlist_id = results['playlists']['items'][0]['id']
        print(f"Playlist ID: {playlist_id}")
    else:
        playlist_id = None
        print(f"No playlist found with the name '{playlist_name}'")

    return playlist_id
