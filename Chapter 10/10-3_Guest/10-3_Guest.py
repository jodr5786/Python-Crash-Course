filename = 'guest.txt'

with open(filename, 'a') as f:
    name = input("What is your name? \n")
    f.write(name + "\n")