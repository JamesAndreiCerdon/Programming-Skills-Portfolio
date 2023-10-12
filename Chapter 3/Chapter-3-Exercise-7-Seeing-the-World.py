"""Chapter Exercise 7: Seeing the world 
Think of at least five places in the world you’d like to visit. • Store the locations in a list. Make sure the list is not in alphabetical order.

• Print your list in its original order. Don’t worry about printing the list neatly,just print it as a raw Python list.

• Use sorted() to print your list in alphabetical order without modifying the actual list.

• Show that your list is still in its original order by printing it.

• Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.

• Show that your list is still in its original order by printing it again.

• Use reverse() to change the order of your list. Print the list to show that its order has changed.

• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.

• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.

• Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed."""


# store the locations in a list
locations = ['Paris, france', 'Kobe', 'Shibuya', 'Akihabara', 'Osaka Castle']

# print list in original order
print("Original order:")
print(locations)

# print list in sorted Alphabetical locations
print("\nAlphabetical:")
print(sorted(locations))

# print list with \n original order
print("\nOriginal order:")
print(locations)

# print list with \n reverse sorted alphabetical order without changing the order of the original order
print("\nReverse alphabetical:")
print(sorted(locations, reverse=True))

# print list with \n original order 
print("\nOriginal order:")
print(locations)

# print list with \n reversed
print("\nReversed:")
locations.reverse()
print(locations)

# print list with \n original order 
print("\nOriginal order:")
locations.reverse()
print(locations)

# print list with \n Alphabetical and sort
print("\nAlphabetical")
locations.sort()
print(locations)

# print list with \n Reverse alphabetical and sort
print("\nReverse alphabetical")
locations.sort(reverse=True)
print(locations)

