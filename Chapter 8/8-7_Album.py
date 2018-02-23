def make_album(artist_name, album_title, number_tracks=''):
    """Return a dictionary of album information."""
    album_dict = {
        'artist': artist_name, 
        'title': album_title,
        }
    if number_tracks:
        album_dict['tracks'] = number_tracks
    return album_dict

album = make_album('eagles', 'hell freezes over', 12)
print(album)

album = make_album('metallica', 'master of puppets', 15)
print(album)

album = make_album('billy joel', 'allentown', 11)
print(album)
