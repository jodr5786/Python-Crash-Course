sandwich_orders = ['turkey', 'pastrami', 'ham', 'pastrami', 'italian', 'pastrami', 'cheese steak']
finished_sandwiches = []

print("I'm sorry, the deli has run out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\n")
while sandwich_orders:
   current_sandwich = sandwich_orders.pop()
   print("I'm working on your " + current_sandwich + " sandwich!")
   finished_sandwiches.append(current_sandwich)

print("\n")
for finished_sandwich in finished_sandwiches:
    print("I made a " + finished_sandwich + " sandwich!")