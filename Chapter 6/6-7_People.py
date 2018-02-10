person1_info = {
    'first_name': 'deanna',
    'last_name': 'rawlins',
    'age': 34,
    'city': 'mount dora',
}

person2_info = {
    'first_name': 'josh',
    'last_name': 'rawlins',
    'age': 31,
    'city': 'mount dora',
}

person3_info = {
    'first_name': 'grayson',
    'last_name': 'rawlins',
    'age': 1,
    'city': 'mount dora',
}

people = [person1_info, person2_info, person3_info]

for person in people:
    print("\n")
    print("First name is " + person['first_name'].title() + ".")
    print("Last name is " + person['last_name'].title() + ".")
    print("Age is " + str(person['age']) + ".")
    print("City is " + person['city'].title() + ".")