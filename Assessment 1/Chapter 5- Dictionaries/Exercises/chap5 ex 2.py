# first we will create a dictionary for the words we learned i python 

Words_learned={
    'Break':'It allows you to exit a loop when an external condition is met.',
    'continue':'It is used to end the current iteration in a for loop (or a while loop), and continues to the next iteration.',
    'import':'It is used to make code in one module available in another',
    'lambda':'It is used for defining the anonymous function.',
    'return':'This statement is used to end the execution of the function call and “returns” the result (value of the expression following the return keyword) to the caller.'
}

# we will use (for) loop to retrieve key-value pairs form dictionary.

for words, meaning in Words_learned.items():
    print(f"{words}:\n{meaning}\n")


