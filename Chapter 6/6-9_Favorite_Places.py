favorite_places = {
    'josh': ['north carolina', 'bahamas', 'savannah'],
    'deanna': ['savannah', 'michigan'],
    'grayson': ['home', 'outside'],
}

for name, places in favorite_places.items():
    print("\n" + name.title() + "'s favorite places are:")
    for place in places:
        print("- " + place.title()) 