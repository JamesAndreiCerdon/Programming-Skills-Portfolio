"""Chapter 2 Exercise 5: USB Shopper
A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. 
They are £6 each.

Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.

You will to use the arithmetic operators to complete this exercise."""


USBsticks=float(input("price of USB sticks: "))
Money=float(input("current balance: "))

# / for division
amount=int(Money/USBsticks)
print("you can buy",amount,"pieces of this USB sticks")

# * for mulitply and - for subtract
remaining=float(Money-USBsticks*amount)
print("you have",remaining,"remaining pounds left.")

