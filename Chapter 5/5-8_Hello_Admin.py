usernames = ['admin', 'user1', 'user2', 'user3', 'user4']

for username in usernames:
    if username == 'admin':
        print("Hellow admin, would you like to see a status report?")
    else:
        print("Hello " + username + ", thank you for logging in again.")