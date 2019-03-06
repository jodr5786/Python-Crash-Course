def describe_city(city_name, city_country='united states'):
    """Prints a city name and country."""
    print(city_name.title() + " is located in " + city_country.title() + ".")

describe_city('orlando')
describe_city('boone')
describe_city('capetown', city_country='south africa')