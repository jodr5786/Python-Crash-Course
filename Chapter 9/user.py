class User():
    """Class describing user profiles."""

    def __init__(self, first_name, last_name, username, email_address):
        """Initialize attributes."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email_address = email_address
        self.login_attempts = 0

    def describe_user(self):
        """Prints a summary of the user information."""
        print(self.first_name + " " + self.last_name + ": ")
        print(" - First name: " + self.first_name)
        print(" - Last name: " + self.last_name)
        print(" - Username: " + self.username)
        print(" - Email address: " + self.email_address)    

    def greet_user(self):
        """Greets the user."""
        print("Hello, " + self.first_name + " " + self.last_name + "!")

    def increment_login_attemtps(self):
        """Increments login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attemtps(self):
        """Resets login attempts to 0."""
        self.login_attempts = 0