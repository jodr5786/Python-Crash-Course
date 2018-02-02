current_users = ['jim', 'Sally', 'tom', 'beth', 'Eric']
new_users = ['greg', 'sally', 'Tom', 'deanna', 'josh']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("Sorry, " + new_user + ", this username has already been used. Please choose a new username." )
    else:
        print("This username, " + new_user + ", is available!")