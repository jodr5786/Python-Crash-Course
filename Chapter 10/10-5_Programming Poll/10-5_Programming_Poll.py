filename = 'responses.txt'


responses = []
while True:
    response = input("Why do you like programming? ")
    responses.append(response)

    additional_reponses = input("Would you like to let others respond? (Type 'y' to continue.) ")

    if additional_reponses != 'y':
        break 

with open(filename, 'a') as f:
    for response in responses:
        f.write(response + "\n")
