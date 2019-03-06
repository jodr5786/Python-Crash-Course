class Restaurant():
    """Restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant_name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describes the restaurant."""
        print(self.restaurant_name + " is the name of the restaurant; the cusine is " + self.cuisine_type + ".")

    def open_restaurant(self):
        """Message that the restaurant is open."""
        print(self.restaurant_name + " is open!")
    

restaurant_a = Restaurant('pizza palace', 'pizza')
restaurant_b = Restaurant('mona lisa', 'italian')
restaurant_c = Restaurant('bar harbor', 'seafood')

restaurant_a.describe_restaurant()
restaurant_b.describe_restaurant()
restaurant_c.describe_restaurant()