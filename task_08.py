# Flexible momo shop

# Menu items and their prices
menu = [
    ("buff momo", 180),
    ("veg momo", 150),
    ("chicken momo", 220),
    ("tea", 40)
]

# Calculate the total bill with an optional discount
def total_bill(*prices, discount=0):
    return sum(prices) - discount


print(f"{total_bill(100, 120, 170)}")
print(f"{total_bill(100, 120, 170, discount=40)}")

cart = [100, 120, 180]
print(f"{total_bill(*cart)}")


# Print customer order details
def make_order(customer, *items, **extras):
    print(f"Order for {customer}:")

    for item in items:
        print(f"  - {item}")

    for key, value in extras.items():
        print(f"  {key}: {value}")


make_order(
    "Sita",
    "buff momo",
    "jhol momo",
    spicy="yes",
    table=4
)

# Sort menu
sort = sorted(menu, key=lambda item: item[1])
print(f"sorted menu: {sort}")

# Find the most expensive item
costliest = max(menu, key=lambda item: item[1])
print(f"Costliest: {costliest}")

# Add a 10% service charge to each price
service_prices = list(map(lambda item: int(item[1] * 1.1), menu))
print(f"With 10% service: {service_prices}")

# Keep only items costing less than Rs 200
under_200 = list(filter(lambda item: item[1] < 200, menu))
print(f"Under 200: {under_200}")

# output

# 90
# 350
# 400
# Order for Sita:
#   - buff momo
#   - jhol momo
#   spicy: yes
#   table: 4
# sorted menu: [('tea', 40), ('veg momo', 150), ('buff momo', 180), ('chicken momo', 220)]
# Costliest: ('chicken momo', 220)
# With 10% service: [198, 165, 242, 44]
# Under 200: [('buff momo', 180), ('veg momo', 150), ('tea', 40)]