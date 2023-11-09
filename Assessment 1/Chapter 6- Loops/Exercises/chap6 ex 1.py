pizza_toppings = ''
while pizza_toppings.lower() != 'quit': #if the user enter quit it will exit the loop
    pizza_toppings = input("Enter toppings for your pizza or enter quit to finish: ")
    if pizza_toppings.lower() != 'quit':
        print(f"I'll add {pizza_toppings} to your pizza.")
