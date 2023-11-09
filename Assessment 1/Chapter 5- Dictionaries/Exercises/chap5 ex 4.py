rivers = {
    'Nile': 'Egypt',
    'Mississippi': 'United states',
    'Yangtze': 'China'
}

#now we will print a sentence about each river
for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

# now we will Print the name of each river
print("\nRivers:")
for river in rivers:
    print(river)

#now we will Print the name of each country
print("\nCountries:")
for country in rivers.values():
    print(country)
