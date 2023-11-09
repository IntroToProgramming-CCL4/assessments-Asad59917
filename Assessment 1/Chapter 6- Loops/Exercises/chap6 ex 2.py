while True:
    enter_age = input("Please enter your age or enter quit to exit: ")

    if enter_age.lower() == 'quit':
        break  # for exiting the loop if the user inputs quit

    age = int(enter_age)

    if age < 3:              #if the is equal to 3 or less then 3 then the ticket will bw free 
        print("Your ticket is free.")
    elif 3 <= age <= 12:     #if the age will be more then 12 or equal to 12 the the ticket will be  10$
        print("The cost of your ticket is $10.")
    else:          #if the age will be more then 15 or equal to 15 the the ticket will be  15$
        print("The cost of your ticket is $15.")
