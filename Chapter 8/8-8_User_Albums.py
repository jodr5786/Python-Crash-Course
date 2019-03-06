def make_album(artist, title):
    """Return a dictionary of album information."""
    album_dict = {
        'artist': artist, 
        'title': title,
        }
    return album_dict

while True:
    print("\nPlease enter the album information:")
    print("(enter q at any time to quit)")
    
    artist = input("Artist: ")
    if artist == 'q':
        break
    
    title = input("Title: ")
    if title == 'q':
        break

    album = make_album(artist.title(), title.title())
    print(album)