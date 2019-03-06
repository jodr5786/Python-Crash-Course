def make_sandwich(*toppings):
    """Summarizes a sandwich being made."""
    print("Making a sandwich with the following toppings:")
    for topping in toppings:
        print("- " + topping)