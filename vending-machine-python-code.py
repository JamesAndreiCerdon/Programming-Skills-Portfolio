# Define the items in the vending machine
items = {
    "A1": {"name": "Apple Juice", "price": 2.5, "stock": 10},
    "A2": {"name": "Water", "price": 1, "stock": 15},
    "B1": {"name": "Biscuits", "price": 2, "stock": 8},
    "B2": {"name": "Gummy Bears", "price": 3, "stock": 5},
    "C1": {"name": "Popcorn", "price": 10, "stock": 15},
    "C2": {"name": "Melon Milk", "price": 4.5, "stock": 15},
    "D1": {"name": "Pepsi", "price": 4, "stock": 15},
    "D2": {"name": "Doritos Nacho Cheese", "price": 8, "stock": 15},
    "E1": {"name": "Chips Ahoy Cookies", "price": 5, "stock": 15},
    "E2": {"name": "Starbucks Frappuccino bottle Caramel", "price": 12, "stock": 15}
}

# Define a function to display the menu of items
def display_items():
    print("Welcome to the vending machine!")
    print("Here are the items available:")
    for code, item in items.items():
        print(f"{code}: {item['name']} - {item['price']} AED - {item['stock']} left")

# Define a function to get the user's selection
def get_selection():
    while True:
        code = input("Enter the code of the item you want or 'cancel' to cancel: ")
        if code == "cancel":
            return None
        if code in items:
            item = items[code]
            if item["stock"] > 0:
                return item
            else:
                print("Item out of stock.")
        else:
            print("Invalid code.")

# Define a function to get the user's payment
def get_payment(price):
    while True:
        try:
            payment = float(input(f"Enter {price} AED to purchase: "))
            if payment >= price:
                return payment
            else:
                print(f"Insufficient payment. Please enter at least {price} AED.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Define a function to calculate the change
def calculate_change(price, payment):
    change = payment - price
    if change > 0:
        print(f"Here is your change: {change} AED.")
    elif change == 0:
        print("No change due.")
    return change

# Define a function to run the vending machine
def run_vending_machine():
    display_items()
    item = get_selection()
    if item is None:
        return
    price = item["price"]
    payment = get_payment(price)
    change = calculate_change(price, payment)
    print(f"Here is your {item['name']}. Thank you for your purchase!")
    print(f"Your balance is {payment - price} AED.")

# Run the vending machine
run_vending_machine()
