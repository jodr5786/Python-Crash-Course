class Restaurant():
    """Restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant_name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describes the restaurant."""
        print(self.restaurant_name + " is the name of the restaurant; the cusine is " + self.cuisine_type + ".")

    def open_restaurant(self):
        """Message that the restaurant is open."""
        print(self.restaurant_name + " is open!")
    
    def set_number_served(self, served):
        """Sets the number of customers that have been served."""
        self.number_served = served
        print("Number served: " + str(self.number_served))

    def increment_number_served(self, served):
        """Increments number served."""
        self.number_served += served
        print("Number served in day: " + str(self.number_served))
    
class IceCreamStand(Restaurant):
    """Models icecream stand restaurant."""

    def __init__(self, restaurant_name, cuisine_type='ice cream'):
         super().__init__(restaurant_name, cuisine_type)
         self.flavors = []
    
    def display_flavors(self):
        print("\nWe have the following flavors of ice cream available: ")
        for flavor in self.flavors:
            print("- " + flavor.title())


icey_stand = IceCreamStand('Icey Stand')
icey_stand.flavors = ['vanilla', 'chocolate', 'strawberry']
icey_stand.describe_restaurant()
icey_stand.display_flavors()