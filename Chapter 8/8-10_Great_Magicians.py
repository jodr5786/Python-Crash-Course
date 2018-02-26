def show_magicians(names):
    """Prints a list of magician's names."""
    print("List of magician names:")
    for name in names:
        print(name.title())

def make_great():
    """Adds "the Great" to the end of each magician's name."""

magician_names = ['houdini', 'david copperfield', 'prestige']
show_magicians(magician_names)
        