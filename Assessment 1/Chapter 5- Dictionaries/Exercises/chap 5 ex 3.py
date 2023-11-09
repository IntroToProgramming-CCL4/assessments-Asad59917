# we will create a Words_Learned with programming terms and their meanings
Words_Learned = {
    'Variable': 'A container for storing data values.',
    'Function': 'A block of organized, reusable code that is used to perform a single, related action.',
    'Loop': 'A control structure that repeats a block of code until a specified condition is met.',
    'List': 'A collection of items that are ordered and mutable.',
    'Conditional Statement': 'A statement that performs different actions depending on whether a condition is true or false.',
    'Dictionary': 'A collection of data that is unordered, changeable, and indexed. It has keys and values.',
    'Algorithm': 'A set of well-defined rules or steps to solve a specific problem.',
    'String': 'A sequence of characters, used for text representation in programming.',
    'Boolean': 'A data type that can be either True or False.',
    'Recursion': 'A technique in which a function calls itself in its own definition.'
}

# Print it 
for term, definition in Words_Learned.items():
    print(f"{term}:\n{definition}\n")
