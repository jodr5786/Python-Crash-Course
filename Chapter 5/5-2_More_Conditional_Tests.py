# Tests for equality and inequality with strings
fish = 'cobia'

print("Is fish == 'cobia'? I predict True.")
print(fish == 'cobia')

car = 'ford'

print("Is car a mazda? I predict False.")
print(car == 'mazda')

# Tests using the lower() function
place = 'Orlando'

print("Is the place == 'orlando'? Predict True.")
print(place.lower() == 'orlando')

place = 'Japan'

print("Is the place == 'Japan'? Predict False.")
print(place.lower() == 'Japan')

# Numberical tests involving equality and inequality, greater than
# and less than, greater than or equal to, and less than or equal to
age_0 = 10
age_1 = 11
age_2 = 12
print("Is " + str(age_1) + " between " + str(age_0) + " and " + str(age_2) + "?")
print(age_1 > age_0 and age_1 < age_2)

age_0 = 5
age_1 = 10
age_2 = 1
print("Is " + str(age_0) + " greater than " + str(age_1) + " or less than " + str(age_2) + "?")
print(age_0 > age_1 or age_0 < age_2)

age_0 = 10
age_1 = 13
print("Is " + str(age_0) + " equal to " + str(age_1) + "?")
print(age_0 == age_1)

age_0 = 10
age_1 = 13
print("Is " + str(age_0) + " not equal to " + str(age_1) + "?")
print(age_0 != age_1)

age_0 = 10
age_1 = 13
print("Is " + str(age_0) + " greater than " + str(age_1) + "?")
print(age_0 > age_1)

age_0 = 10
age_1 = 13
print("Is " + str(age_0) + " less than " + str(age_1) + "?")
print(age_0 < age_1)

# Test whether an item is in a list
thing = 'thing_2'
list_of_things = ['thing_0','thing_1','thing_2','thing_3']
if thing in list_of_things:
    print(thing + " is in the 'list_of_things'.")
else:
    print(thing + " is NOT in the 'list_of_things'.")