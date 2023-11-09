def make_shirt(size, message):
    print(f"I need {size} sized shirt with {message}")

# first we gonnaa call the the function using positional arguments
make_shirt("XL", "LOST")

# now we will the function using keyword arguments
make_shirt(size="XXXL", message="Lost")