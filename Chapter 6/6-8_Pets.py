pets = []

pet = {
    'animal': 'dog',
    'name': 'griffin',
    'owner': 'josh',
}
pets.append(pet)

pet = {
    'animal': 'dog',
    'name': 'maverick',
    'owner': 'deanna',
}
pets.append(pet)

pet = {
    'animal': 'cat',
    'name': 'luna',
    'owner': 'deanna',
}
pets.append(pet)

for pet in pets:
    animal = pet['animal']
    name = pet['name'].title()
    owner = pet['owner'].title()
    print("\n")
    print(name + " is a " + animal + " owned by " + owner + ".")
