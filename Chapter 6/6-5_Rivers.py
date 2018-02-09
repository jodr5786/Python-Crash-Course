rivers = {
    'nile': 'egypt',
    'mississippi': 'America',
    'rio grande': 'America',
}

for river, country in rivers.items():
    print("The " + river.title() + " runs through " + country.title() + ".")

print("\nThe following rivers are in this data set:")
for river in rivers.keys():
    print(river.title())

print("\nThe following countries are in this data set:")
for country in rivers.values():
    print(country.title())
