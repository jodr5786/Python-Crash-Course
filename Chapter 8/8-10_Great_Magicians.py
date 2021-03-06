def show_magicians(magicians):
    """Prints a list of magician's names."""
    for magician in magicians:
        print(magician)

def make_great(magicians):
    """Adds "the Great" to the end of each magician's name."""
    great_magicians = []

    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)
    
    for great_magician in great_magicians:
        magicians.append(great_magician)

magicians = ['Harry Houdini', 'David Copperfield', 'David Blaine']
show_magicians(magicians)

print("\n")

make_great(magicians)
show_magicians(magicians)
        