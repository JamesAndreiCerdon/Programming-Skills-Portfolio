"""Chapter 4 Exercise 3: Alien Colors #3
Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.

• If the alien is green, print a message that the player earned 5 points.

• If the alien is yellow, print a message that the player earned 10 points.

• If the alien is red, print a message that the player earned 15 points.

• Write three versions of this program, making sure each message is printed for the appropriate color alien."""

#alien_color is a variable set to "red".

#The first if statement, if alien_color is equal to "green", print "You just earned 5 points!"

#The next one, if alien_color is equal to "yellow", print "You just earned 10 points!"

#The last one, otherwise, print "You just earned 15 points!"

#So this code will display these messages depending on what alien_color is equals to


alien_color = 'red'

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")