"""Script containing methods utilizing Spotipy APIs"""

import conf


# Method that returns an Artist's URI given its name
def uri_finder(artist):

    artist_code = conf.SP.search(q='artist:' + artist, type='artist', limit=1)

    if artist_code['artists']['items']:
        artist_URI = artist_code['artists']['items'][0]['uri']
    else:
        print('Artist not found.')

    return artist_URI


# Method that returns an Artist's Genre given its name
def get_artist_genre_by_name(artistName):

    artist_URI = uri_finder(artistName)
    artist = conf.SP.artist(artist_URI)
    genre = artist['genres']
    return ', '.join(genre)


# Method that returns an Artist's Genre given its URI
def get_artist_genre_by_URI(artist_URI):

    artist = uri_finder('Sleep Token')
    artist = conf.SP.artist(artist_URI)
    genre = artist['genres']
    return ', '.join(genre)


# Method that returns all the Albums of a given Artist
def album_finder(artist, artist_URI):

    albums_data = conf.SP.artist_albums(artist_URI, album_type='album')
    albums = albums_data['items']

    while albums_data['next']:
        albums_data = conf.SP.next(albums_data)
        albums.extend(albums_data['items'])

    print(f"These are all {artist} \'s albums found on Spotify:")
    for x in range(len(albums)):
        print(str(x) + "° Album: " + albums[x]['name'])


# Method that returns the top 10 songs of a given Artist
def top_songs(artist, artist_URI, target_country):

    top_tracks = conf.SP.artist_top_tracks(artist_URI, country=target_country)

    top_ten_tracks = top_tracks['tracks'][:10]

    print(f"These are {artist} \'s top {len(top_ten_tracks)} songs in {target_country} found on Spotify:")

    for x in range(len(top_ten_tracks)):
        print(str(x+1) + "° Track: " + top_ten_tracks[x]['name'])
        print(str(x+1) + "° Audio: " + top_ten_tracks[x]['preview_url'] + "\n")


# Method that returns the name of a given Playlist
def get_playlist_name(playlist_id):
    playlist = conf.SP.playlist(playlist_id)
    return playlist['name']


# Methodo that removes the char "|" in the file name
def clear_playlist_name(tmp_name):
    if '|' in tmp_name:
        return tmp_name.replace("|", "")
    return tmp_name


# Method that returns the IDs of every track in a given Playlist
def track_IDs_from_playlist(user, playlist_ID):
    track_IDs = []
    offset = 0
    limit = 100

    while True:
        playlist = conf.SP.user_playlist_tracks(user, playlist_ID,
                                                limit=limit, offset=offset)

        for elem in playlist['items']:
            track = elem['track']
            track_IDs.append(track['id'])

        offset += limit
        if len(playlist['items']) < limit:
            break

    return track_IDs


# Method that returns the features of every track in a given Playlist
def get_track_features(trackID):

    track_details = conf.SP.track(trackID)
    track_features = conf.SP.audio_features(trackID)

    # Track Info
    name = track_details['name']

    # Track Features
    energy = track_features[0]['energy']
    liveness = track_features[0]['liveness']
    loudness = track_features[0]['loudness']

    track_info = [name, energy, liveness, loudness]

    return track_info


# Method that returns the link to the preview of the track
def getTrackPreview(trackName, artistName):

    query = f"track:{trackName} artist:{artistName}"
    results = conf.SP.search(q=query, type='track')

    for track in results['tracks']['items']:
        if track['name'].lower() == trackName.lower():
            artists = [artist['name'].lower() for artist in track['artists']]
            if artistName.lower() in artists:
                track_id = track['id']
                track_info = conf.SP.track(track_id)
                preview_url = track_info['preview_url']
                return preview_url

    return None
