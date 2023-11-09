# we will create a list for sandwiches
sandwich_orders = ["shawarma", "zinger", "twister", "Grilled Chicken", "tikka"]

#we will  Empty list to store finished sandwiches
finished_sandwiches = []

# now we will Make sandwiches from the orders
while sandwich_orders:
    current_order = sandwich_orders.pop(0)
    print(f" Your {current_order} sandwich.is ready to be collected")
    finished_sandwiches.append(current_order)

# now we will printn the finished sandwiches
print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
