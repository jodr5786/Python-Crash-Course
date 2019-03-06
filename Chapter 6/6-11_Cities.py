cities = {
    'orlando': {
        'country': 'united states',
        'population': '277,173',
        'fact': 'middle of Florida',
    },
    'savannah': {
        'country': 'united states',
        'population': '146,763',
        'fact': 'Civil War statues in parks',
    },
    'st. augustine': {
    'country': 'united states',
    'population': '14,280',
    'fact': 'old',
    },
}

for city, city_info in cities.items():
    print("\n" + city.title() + " Facts:")
    print("\tCountry: " + city_info['country'].title())
    print("\tPopulation: " + city_info['population'].title())
    print("\tfact: " + city_info['fact'].title())