sandwich_orders = ['turkey', 'ham', 'italian', 'cheese steak']
finished_sandwiches = []

while sandwich_orders:
   finished_sandwich = sandwich_orders.pop()

   print("\nI just made your " + finished_sandwich + " sandwich!")

   finished_sandwiches.append(finished_sandwich)
