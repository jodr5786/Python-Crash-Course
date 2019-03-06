from privileges import Admin

josh_profile = Admin('josh', 'rawlins', 'joshdrawlins', 'joshdrawlins@gmail.com')

josh_profile.describe_user()

josh_profile.privileges.privileges = [
    'create user',
    'create groups',
    'edit files and folders'
]

josh_profile.privileges.show_privileges()