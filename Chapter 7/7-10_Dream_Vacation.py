dream_vacation = {}

polling_active = True 

while polling_active:
    name = input("\nWhat is your name? ")
    place = input("If you could visit one place in the world, where would it be? ")

    dream_vacation[name] = place

    repeat = input("Would you like to let another person take the poll? (yes/no) ")
    if repeat == 'no':
        polling_active = False

for name, place in dream_vacation.items():
    print(name.title() + "'s dream vacation is to " + place.title() + ".")