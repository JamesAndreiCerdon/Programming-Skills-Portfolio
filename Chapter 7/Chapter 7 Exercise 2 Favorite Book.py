"""Exercise 2: Favorite Book 
Write a function called favorite_book() that accepts one parameter, title. The function should print a message, such as One of my

favorite books is Alice in Wonderland. Call the function, making sure to include a book title as an argument in the function call."""

#this function is called "favorite_book". Like before, it has no parameters, and within it is a print statement, with the variable title being added to the string "is one of my favorite books."
#When you type in "favorite_book('The Great Gatsby')", the function runs, and prints to the console, 
#"The Abstract Wild is one of my favorite books." It basically only has two steps to it: get a book title and a print statement. 
#Nothing is really getting stored or referenced here.

def favorite_book(title):
    """Display a message about someone's favorite book."""
    print(title + " is one of my favorite books.")

favorite_book('The Great Gatsby')