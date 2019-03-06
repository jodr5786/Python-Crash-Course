prompt = "\nEnter a topping to be added to a pizza."
prompt += "\nType 'quit' to exit: "

active = True

while active:
    message = input(prompt)

    if  message == 'quit':
        break
    else:
        print("I'm adding " + message + " to your pizza!")