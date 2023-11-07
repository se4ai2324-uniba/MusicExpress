"""Script containing methods utilizing Spotipy APIs"""

import conf


# Method that returns an Artist's URI given its name
def uriFinder(artist):

    artistCode = conf.SP.search(q='artist:' + artist, type='artist', limit=1)

    if artistCode['artists']['items']:
        artist_uri = artistCode['artists']['items'][0]['uri']
    else:
        print('Artist not found.')

    return artist_uri


# Method that returns an Artist's Genre given its name
def getArtistGenreByName(artistName):

    artistURI = uriFinder(artistName)
    artist = conf.SP.artist(artistURI)
    genre = artist['genres']
    return ', '.join(genre)


# Method that returns an Artist's Genre given its URI
def getArtistGenreByURI(artistURI):

    artist = uriFinder('Sleep Token')
    artist = conf.SP.artist(artistURI)
    genre = artist['genres']
    return ', '.join(genre)


# Method that returns all the Albums of a given Artist
def albumFinder(artist, artistURI):

    albumsData = conf.SP.artist_albums(artistURI, album_type='album')
    albums = albumsData['items']

    while albumsData['next']:
        albumsData = conf.SP.next(albumsData)
        albums.extend(albumsData['items'])

    print(f'These are all {artist} \'s albums found on Spotify:')
    for x in range(len(albums)):
        print(str(x) + "° Album: " + albums[x]['name'])


# Method that returns the top 10 songs of a given Artist
def topSongs(artist, artistURI, targetCountry):

    topTracks = conf.SP.artist_top_tracks(artistURI, country=targetCountry)

    topTenTracks = topTracks['tracks'][:10]

    print(f'These are {artist} \'s top {len(topTenTracks)} 
          songs in {targetCountry} found on Spotify:')

    for x in range(len(topTenTracks)):
        print(str(x+1) + "° Track: " + topTenTracks[x]['name'])
        print(str(x+1) + "° Audio: " + topTenTracks[x]['preview_url'] + "\n")


# Method that returns the name of a given Playlist
def getPlaylistName(playlist_id):
    playlist = conf.SP.playlist(playlist_id)
    return playlist['name']


# Methodo that removes the char "|" in the file name
def clearPlaylistName(tmpName):
    if '|' in tmpName:
        return tmpName.replace("|", "")
    return tmpName


# Method that returns the IDs of every track in a given Playlist
def trackIDsFromPlaylist(user, playlistID):
    trackIDs = []
    offset = 0
    limit = 100

    while True:
        playlist = conf.SP.user_playlist_tracks(user, playlistID,
                                                limit=limit, offset=offset)

        for elem in playlist['items']:
            track = elem['track']
            trackIDs.append(track['id'])

        offset += limit
        if len(playlist['items']) < limit:
            break

    return trackIDs


# Method that returns the features of every track in a given Playlist
def getTrackFeatures(trackID):

    trackDetails = conf.SP.track(trackID)
    trackFeatures = conf.SP.audio_features(trackID)

    # Track Info
    name = trackDetails['name']

    # Track Features
    energy = trackFeatures[0]['energy']
    liveness = trackFeatures[0]['liveness']
    loudness = trackFeatures[0]['loudness']

    trackInfo = [name, energy, liveness, loudness]

    return trackInfo


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
