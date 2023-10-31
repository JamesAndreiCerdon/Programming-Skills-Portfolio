"""Chapter 4 Exercise 5: Pets 
Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the

owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about

each pet"""


# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = {
    'animal type': 'pythonidae',
    'name': 'Adam',
    'owner': 'Mike',
    'weight': 43,
    'eats': 'birds',
}
pets.append(pet)

pet = {
    'animal type': 'chicken',
    'name': 'Steven',
    'owner': 'Louise',
    'weight': 2,
    'eats': 'seeds',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'Jason',
    'owner': 'Liam',
    'weight': 37,
    'eats': 'Dog food',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))
