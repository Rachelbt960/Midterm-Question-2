# Get the price  of sale item from the user
price = float(input("Enter the price of the sale item: "))

# Get the shipping state from the user
state = input("Enter the state to which the item will be shipped: ")

# What the shipping tax is
if state == "TX" or state == "LA":
    shipping_tax = 1.25
elif state == "CA":
    shipping_tax = 3.25
else:
    shipping_tax = 0.50

# Display the shipping tax
print("The shipping tax is: $", shipping_tax)
