number = input("Give me a number, and I'll tell you if it's a multiple of 10: ")

number = int(number)

if number % 10 == 0:
    print("\n" + str(number) + " is a multiple of 10!")
else:
    print("\n" + str(number) + " isn't a multiple of 10.")