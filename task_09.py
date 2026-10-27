# Banner, countdown and token machine

# Print a Dashain banner before and after a function
def dashain_banner(func):
    def wrapper(*args, **kwargs):
        print("*** Happy Dashain ***")
        func(*args, **kwargs)
        print("*********************")
    return wrapper

# Decorated greeting function
@dashain_banner
def greet(name, gift="tika"):
    print(f"{name} gets a {gift}!")

greet("Sita")
greet("Ram", "kite")

# Count down recursively until Tika day
def countdown(n):
    if n == 0:
        print("Tika day!")
        return

    print(f"{n} days left")
    countdown(n - 1)

countdown(3)

# Calculate the sum of digits recursively
def sum_digits(n):
    if n < 10:
        return n

    return n % 10 + sum_digits(n // 10)

print(f"Digit sum: {sum_digits(2026)}")

# Generate tokens forever starting from a given number
def token_machine(start):
    while True:
        yield f"T-{start}"
        start += 1

tokens = token_machine(101)

print(f"{next(tokens)} {next(tokens)} {next(tokens)}")

# Sum the squares from 1² to 5² using a generator expression
total = sum(x ** 2 for x in range(1, 6))
print(f"Sum of squares: {total}")


# output

# *** Happy Dashain ***
# Sita gets a tika!
# *********************
# *** Happy Dashain ***
# Ram gets a kite!
# *********************
# 3 days left
# 2 days left
# 1 days left
# Tika day!
# Digit sum: 10
# T-101 T-102 T-103
# Sum of squares: 55