# we will create a list for sandwiches
sandwich_orders = ["shawarma", "zinger", "twister", "Grilled Chicken", "tikka","pastrami","pastrami","pastrami"]

#we will  Empty list to store finished sandwiches
finished_sandwiches = []
print("We've run out of pastrami.")

#we will write a statment to remove pastrami from the 

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# now we will Make sandwiches from the orders
while sandwich_orders:
    current_order = sandwich_orders.pop(0)
    print(f" Your {current_order} sandwich is ready to be collected")
    finished_sandwiches.append(current_order)

# now we will printn the finished sandwiches
print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
