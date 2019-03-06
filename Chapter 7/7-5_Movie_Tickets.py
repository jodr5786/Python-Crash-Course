prompt = "\nHow old are you?"
prompt+= "\nEnter 'quit' to exit: "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)
    
    if age < 3:
        print(" Your ticket is free!")
    elif age >= 3 and age <= 12:
        print(" Your ticket is $10.")
    elif age > 12:
        print(" Your ticket is $15.")