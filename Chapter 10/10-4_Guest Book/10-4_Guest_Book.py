filename = 'guest_book.txt'

with open(filename, 'a') as f:
    while True:
        name = input("What is your name? (Type 'q' or 'quit' to quit.)\n")
        if name == 'q':
            break 
        elif name == 'quit':
            break 
        else:
            print("Greetings, " + name.title() + "!\n")
            f.write(name + "\n")