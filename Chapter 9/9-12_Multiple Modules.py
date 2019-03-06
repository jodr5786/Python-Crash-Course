from admin import Admin

josh_user_profile = Admin('josh', 'rawlins', 'joshdrawlins', 'joshdrawlins@gmail.com')

josh_user_profile.describe_user()

josh_user_profile.privileges.privileges = [
    'create',
    'modify',
    'delete'
]

josh_user_profile.privileges.show_privileges()