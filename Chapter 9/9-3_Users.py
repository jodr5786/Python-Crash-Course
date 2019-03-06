class User():
    """Class describing user profiles."""

    def __init__(self, first_name, last_name, username, email_address):
        """Initialize attributes."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email_address = email_address

    def describe_user(self):
        """Prints a summary of the user information."""
        print("The user information is: ")
        print("\n - First name: " + self.first_name)
        print("\n - Last name: " + self.last_name)
        print("\n - Username: " + self.username)
        print("\n - Email address: " + self.email_address)    

    def greet_user(self):
        """Greets the user."""
        print("Hello, " + self.first_name + " " + self.last_name + "!")


josh = User('josh','rawlins','jodr5786','joshdrawlins@gmail.com')
deanna = User('deanna','rawlins','deannamarie','deannamarietitlton@gmail.com')

josh.describe_user()
josh.greet_user()

deanna.describe_user()
deanna.greet_user()