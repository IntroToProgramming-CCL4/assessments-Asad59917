# we will create  dictionaries for different pets and their owner
pet1 = {'animal': 'puppy', 'owner': 'shahab'}
pet2 = {'animal': 'cat', 'owner': 'tayyab'}
pet3 = {'animal': 'hamster', 'owner': 'mohsin'}
pet4 = {'animal': 'bull dog', 'owner': 'Asad'}
# Now we will sort our dictionary into a list called pets
pets = [pet1, pet2, pet3,pet4]

# now we will loop through the list printing information about pets and their owner
for pet in pets:
    print(f"Pet: {pet['animal']}")
    print(f"Owner: {pet['owner']}\n")
    