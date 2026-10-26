# Ping (swing) ticket counter
# Decide who can ride the big Dashain ping, and how much they pay.

# 1. Input
name = input("Name: ").strip().title()
age = int(input("Age: "))
height = int(input("Height (cm): "))
coupon = input("Coupon code: ").strip().lower()

# 2. Check empty name
if name == "":
    print("Please enter your name.")

# 3. Safety check
elif age < 5 or height < 110:
    print(f"Sorry {name}, the big ping is not safe for you.")

else:
    # 4. Ticket price
    if age >= 60:
        price = 0
    elif age < 12:
        price = 50
    else:
        price = 100

    # 5. Coupon discount
    if coupon in ["dashain", "tihar"] and price > 0:
        price -= 20
        print("Coupon used! Rs 20 off.")

    print(f"{name}, your ping ticket is Rs {price}.")


# output

# Name: ram prasad
# Age: 45
# Height (cm): 170
# Coupon code: 
# Ram Prasad, your ping ticket is Rs 100.

# Name: gita kumari
# Age: 11
# Height (cm): 120
# Coupon code: dashain
# Coupon used! Rs 20 off.
# Gita Kumari, your ping ticket is Rs 30.

# Name: aama
# Age: 63
# Height (cm): 146
# Coupon code: tihar
# Aama, your ping ticket is Rs 0.