def make_pizza(size, *toppings):
    """Summarize the pizza we're about to make."""
    print("Making a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)