poll_takers = {'josh', 'aaron', 'sarah', 'phil'}

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for person, language in favorite_languages.items():
    print(person.title()+ "'s favorite language is " + language.title() + ".")

print("\n")

for poll_taker in poll_takers:
    if poll_taker not in favorite_languages.keys():
        print(poll_taker.title() + ", please take the poll.")
    else:
        print(poll_taker.title() + ", thank you for taking the poll!")