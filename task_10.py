# Safe Dashain food shop

# Menu dictionary with item prices
menu = {
    "momo": 180,
    "chowmein": 150,
    "sel roti": 30,
    "tea": 40
}

cart = []


# Get and validate quantity
def ask_quantity():
    quantity = int(input("Quantity: "))

    if quantity <= 0:
        raise ValueError("Quantity must be more than 0")

    return quantity


# Print the final bill
def print_bill(cart):
    total = 0

    for item, quantity, price in cart:
        amount = quantity * price
        total += amount
        print(f"{item} x{quantity} = Rs {amount}")

    print(f"Total: Rs {total}")


while True:
    item = input("Item (or done): ").strip().lower()

    if item == "done":
        break

    try:
        price = menu[item]
        quantity = ask_quantity()

    except KeyError:
        print(f"Sorry, no {item} on the menu.")

    except ValueError as e:
        print(f"Wrong quantity: {e}")

    else:
        cart.append((item, quantity, price))
        print(f"Added {quantity} x {item}")

    finally:
        print("-" * 20)


print_bill(cart)


# output

# Item (or done): momo
# Quantity: 4
# Added 4 x momo
# --------------------
# Item (or done): tea
# Quantity: 7
# Added 7 x tea
# --------------------
# Item (or done): coffee
# Sorry, no coffee on the menu.
# --------------------
# Item (or done): done
# momo x4 = Rs 720
# tea x7 = Rs 280
# Total: Rs 1000