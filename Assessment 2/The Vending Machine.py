import os

item01 = {'Code': '001', 'Name': 'Pepsi    ', 'Price': 8.00, 'Category': 'Cold Drinks'}
item02 = {'Code': '002', 'Name': 'Marinda  ', 'Price': 7.00, 'Category': 'Cold Drinks'}
item03 = {'Code': '003', 'Name': 'Coca cola', 'Price': 8.50, 'Category': 'Cold Drinks'}
item04 = {'Code': '004', 'Name': 'Kitkat   ', 'Price': 5.25, 'Category': 'Chocolate'}
item05 = {'Code': '005', 'Name': 'Dairy milk','Price': 4.50, 'Category': 'Chocolate'}
item06 = {'Code': '006', 'Name': 'Coca cola', 'Price': 9.00, 'Category': 'Cold Drinks'}
item07 = {'Code': '007', 'Name': 'Lays    ',  'Price': 5.00, 'Category': 'Chips'}
item08 = {'Code': '008', 'Name': 'Kurkury   ','Price': 5.00, 'Category': 'Chips'}
item09 = {'Code': '009', 'Name': 'Latte     ','Price': 10.00, 'Category': 'Hot Drinks'}
item10 = {'Code': '010', 'Name': 'Spanish latte','Price': 15.00, 'Category': 'Hot Drinks'}
item11 = {'Code': '011', 'Name': 'Mocha        ','Price': 12.75, 'Category': 'Hot Drinks'}
item12 = {'Code': '012', 'Name': 'Americano','Price': 11.25, 'Category': 'Hot Drinks'}
item13 = {'Code': '013', 'Name': 'Hot Chocolate','Price': 19.00, 'Category': 'Hot Drinks'}   # product list which will be displayed
menu = [item01, item02, item03, item04, item05, item06, item07, item08,item09,item10,item11,item12,item13]
user_order = [] # this will save user orders


def total_order_cost(order): # this function will calculate the sum of the order
    total_amount = sum(item['Price'] for item in order)
    return total_amount
    

def print_menu():  # to displpay the item list in organized way
    print("=" * 30)
    print("Welcome to Vending Machine")
    print("=" * 30)
    print(f"CODE\tITEM\t\tPrice\t")
    for item in menu:
        print(f"{item['Code']}\t{item['Name']}\t{item['Price']}")
    print("=" * 30)

def add_another_Item(): # This function is for adding another item to the user order
    print("=" * 30)
    print("Select another item")
    print("=" * 30)
    print(f"CODE\tITEM\t\tPrice\t")
    for item in menu:
        print(f"{item['Code']}\t{item['Name']}\t{item['Price']}")
    print("=" * 30)

def clear_screen(): # this function will keep the output more clean
    os.system('clear' if os.name == 'posix' else 'cls')


def get_user_choice(): #will allow user to make choices 
    while True:
        choice = input("Enter 'M' to go back to the menu, 'A' to add another item, 'C' to CheckOut, or 'Q' to quit: ").upper()
        if choice in ['M', 'A','C', 'Q']:
            return choice
        else:
            print("Invalid choice. Please enter 'M', 'A','C', or 'Q.")

def add_item_to_order(item): # once the user select an item thiss function will add that itam to the user 
    user_order.append(item)
    print("Item added to your order!")



def User_order_Display(): # it will display user cart/order list in organized way
    print("=" * 30)
    print("\tYour Order")
    print("=" * 30)
    print(f"CODE\tITEM\t\tPrice\t")
    for item in user_order:
        print(f"{item['Code']}\t{item['Name']}\t{item['Price']}")
    print("=" * 30)
    

def user_recipt(): # this will give user choice if they want reciept or no
    while True:
        choice = input(f"Would You like to take recipt\t if YES enter 'Y' If NO enter 'N': ").upper()
        if choice in ['Y', 'N']:
            return choice
        else:
            print("Invalid choice. Please enter 'Y', 'N'")


def User_order_recipt(): # if the user chooses to take reciept then this function will display reciept in organized way
    print("=" * 30)
    print("\tYour recipt")
    print("=" * 30)
    print(f"CODE\tITEM\t\tPrice\t")
    for item in user_order:
        print(f"{item['Code']}\t{item['Name']}\t{item['Price']}")
    print("=" * 30)
    print(f"Total cost \t\t${total_amount:.2f}")
    print("=" * 30)
    print(f"Your Change\t\t${Change_return:.2f}")
    print("=" * 30)
    print("Thank You for your purchase\n\thave a good day")
    print("=" * 30)


# Main loop execution
print_menu() 

while True:
    # ask the user to enter code they want to buy and if they dont want they q to quit
    ask_user_input = input("Enter the item code number from 001 to 013 or enter 'Q' to quit: ").upper()
    clear_screen()
    # if user chooses quit this will end the execution
    if ask_user_input == "Q":

        print("Have a good day")
        break
    else:
        # this will check if the code entered mataches with any of the code in the list then it will add that item to user order
        found = False
        for item in menu:
            if ask_user_input == item['Code']:
                print(f"Item: {item['Name']}\tPrice: {item['Price']}")
                found = True
                add_item_to_order(item)
                clear_screen()
                User_order_Display()
                break
        # if no item is found with the code entered then it will ask to enter code again        
        if not found:
            print("=" * 30)
            print("Invalid input.\nPlease enter a valid item code")
            print_menu()
            continue  
        # this will execute the user next action
        user_choice = get_user_choice()

        if user_choice == 'M':
            print_menu()
        elif user_choice == 'A':
            clear_screen()
            add_another_Item()
            pass
       
        elif user_choice == 'C': 
            # this will proceed to checkout           
            clear_screen()
            User_order_Display()
            total_amount = total_order_cost(user_order)
            print(f"Total cost\t\t${total_amount:.2f}")
            print("=" * 30)
            money_input = float(input("Enter the amount of money: $")) 
            clear_screen()
            # this will make sure that the inserted money is enough to buy the item or items in the user order
            if money_input < total_amount:
                print("Insufficient amount, Please enter sufficient amount")\
                # if not enough that it will ask user again
                while money_input< total_amount:
                    money_input = float(input("Enter the amount of money: $")) 
                    clear_screen()
                
            # this will return the change to user if have any
            Change_return = money_input - total_amount
            print(f"Your Change: ${Change_return:.2f}")
            # it will give choice to the user if they want to take reciept ot no
            recipt_for_user=user_recipt()

            if recipt_for_user == 'Y':
                clear_screen()
                User_order_recipt()

            elif recipt_for_user == 'N':
                clear_screen()
                print("Thank You for your purchase,\nhave a good day")
            break

        # if the user chooses to quit this will end the execution
        elif user_choice == 'Q':   
            clear_screen
            print("Have a good day") 
            break




