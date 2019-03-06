from user import User

class Admin(User):
    """Class describing an Admin user profile."""

    def __init__(self, first_name, last_name, username, email_address):
        super().__init__(first_name, last_name, username, email_address)
        self.privileges = Privileges()

class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges
    
    def show_privileges(self):
        print("\nThe user's privileges are: ")
        if self.privileges:
            for privilege in self.privileges:
                print("- " + privilege)
        else:
            print("This user has no privileges.")