# Ask the shopper a few questions, then print a neat receipt.

# Ask for input
name = input("Your name: ")
item = input("Item: ")
price = float(input("Price: "))
quantity = int(input("Quantity: "))

# Format name and item
customer_name = name.title()
item_name = item.upper()

# Item code from first 3 letters
item_code = item[:3].upper()

# Calculate total
total = price * quantity

# Calculate Rs 500 notes and remaining amount
notes_500 = int(total // 500)
left_amount = total % 500

# Check if total is over 1000
over_1000 = total > 1000

# Print receipt
print("------ DASHAIN RECEIPT ------")
print(f"Customer : {customer_name}")
print(f"Item     : {item_name} (code: {item_code})")
print(f"Total    : Rs {total:.2f}")
print(f"500 notes: {notes_500}, left Rs {left_amount:.2f}")
print(f"Over 1000? {over_1000}")
print(f"Price type: {type(price)}")


# output

# Your name: abhishek lamsal
# Item: icecream
# Price: 450
# Quantity: 7
# ------ DASHAIN RECEIPT ------
# Customer : Abhishek Lamsal
# Item     : ICECREAM (code: ICE)
# Total    : Rs 3150.00
# 500 notes: 6, left Rs 150.00
# Over 1000? True
# Price type: <class 'float'>