favorite_numbers = {
    'sam': [5, 10],
    'larry': [22, 37],
    'greg': [13, 21],
    'elen': [12, 45],
    'tim': [54, 56],
}

for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + "'s favorite numbers are: ")
    for number in numbers:
        print("- " + str(number))

