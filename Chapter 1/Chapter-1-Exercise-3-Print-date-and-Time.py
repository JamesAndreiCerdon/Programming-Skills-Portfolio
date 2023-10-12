"""Chapter 1 Exercise 3: Print date and Time
Write a Python program to display the current date and time."""

# datetime object containing current date and time
import datetime 
now = datetime.datetime.now()

# print the date time like this dd/mm/yy H:M:S 
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

