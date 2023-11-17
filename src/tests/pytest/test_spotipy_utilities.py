"""Script containing Pytest tests designed for spotipy_utilities methods"""
# pylint: disable=wrong-import-position
import sys                        # noqa:E402
sys.path.append('src')            # noqa:E402
import conf                       # noqa:E402
import spotipy_utilities as spUt  # noqa:E402
# pylint: enable=wrong-import-position


def test_artist_uri_found():
    '''Test for checking the artist's uri is properly found'''
    uri = spUt.uri_finder('Sleep Token')
    assert uri != "", "Artist not found"


def test_artist_uri_not_found():
    '''Test for checking the artist's uri is not found'''
    uri = spUt.uri_finder('abc123')
    assert uri != "", "Unexpected artist found"


def test_get_artist_genre_by_name():
    '''Test to get an artist's genre by the name'''
    genre = spUt.get_artist_genre_by_name('Sleep Token')
    assert genre != "", "Artist's genre not found"


def test_get_artist_genre_by_uri():
    '''Test to get an artist's genre by the uri'''
    uri = spUt.uri_finder('Sleep Token')
    genre = spUt.get_artist_genre_by_uri(uri)
    assert genre != "", "Artist's genre not found"


def test_get_playlist_name_by_id():
    '''Test to get a playist name by its id'''
    name = spUt.get_playlist_name(conf.PLAYLISTS[0])
    assert name != "", "Playlist name not found"


def test_clear_playlist_name():
    '''Test to get the cleaned playlist name'''
    # pylint: disable=line-too-long
    expected_name = 'Spotify\'s Most Played All-Time [Updated Weekly]  Most Streamed  Top Played  500Mil+'  # noqa:E501
    # pylint: enable=line-too-long
    name = spUt.get_playlist_name(conf.PLAYLISTS[1])
    name = spUt.clear_playlist_name(name)
    assert name == expected_name, "Playlist name not valid"


def test_track_ids_from_playlist():
    '''Test to get the tracks' id from a playlist'''
    playlist_id = "0THO1kZlbyWvlgAh8YUCSd"
    user = "ivanrinaldi_"
    # pylint: disable=line-too-long
    expected_tracks_ids = ['18lR4BzEs7e3qzc0KVkTpU', '1r1fPuhj9H4VdXr7OK6FL5', '373gDROnujxNTFa1FojYIl']  # noqa:E501
    # pylint: enable=line-too-long
    ids = spUt.track_ids_from_playlist(user, playlist_id)
    assert ids == expected_tracks_ids, "Tracks' ids do not match"


def test_get_track_features():
    '''Test to get track's features'''
    track_id = '18lR4BzEs7e3qzc0KVkTpU'
    expected_track_features = [
            "What I've Done",
            {
                # pylint: disable=line-too-long
                'external_urls': {'spotify': 'https://open.spotify.com/artist/6XyY86QOPPrYVGvF9ch6wz'},  # noqa:E501
                # pylint: enable=line-too-long
                'href': 'https://api.spotify.com/v1/artists/6XyY86QOPPrYVGvF9ch6wz',  # noqa:E501
                'id': '6XyY86QOPPrYVGvF9ch6wz',
                'name': 'Linkin Park',
                'type': 'artist',
                'uri': 'spotify:artist:6XyY86QOPPrYVGvF9ch6wz'
            },
            0.93,
            0.138,
            -5.285]
    track_features = spUt.get_track_features(track_id)
    assert track_features == expected_track_features, "Track's features do not match"  # noqa:E501


def test_get_track_preview_url():
    '''Test to get the track's preview url'''
    track_name = "What I've Done"
    artist_name = "Linkin Park"
    url = spUt.get_track_preview(track_name, artist_name)
    assert url != "", "Preview not found"
