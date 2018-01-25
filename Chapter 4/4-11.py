# My Pizzas, Your Pizzas

my_pizzas = ['pepperoni', 'works', 'buffalo']

my_pizzas.append('deep dish')

friend_pizzas = my_pizzas[:]

friend_pizzas.append('pineapple')

print("My favorite pizzas are:")
for my_pizza in my_pizzas:
    print("- " + my_pizza)

print("\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print("- " + friend_pizza)

