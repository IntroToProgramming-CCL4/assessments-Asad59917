def make_shirt(size="Large", message="I love python"):
    print(f"I need {size} sized shirt with {message} message")

# first we gonnaa call the the function using positional arguments
make_shirt()

# we will print it with medium size

make_shirt(size='medium')

# now we will the function using keyword arguments
make_shirt( size="XXL",message="Lost")