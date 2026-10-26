# Kite shop stock list

# Initial list
kites = ["red", "green", "blue"]

# 1. Add yellow at end and black at start
kites.append("yellow")
kites.insert(0, "black")

# 2. Remove green and pop last kite
kites.remove("green")
sold = kites.pop()
print(f"Sold: {sold}")

# 3. Sort and print first two
kites.sort()
print(f"Stock: {kites}")
print(f"First two: {kites[:2]}")

# 4. Count and check blue
print(f"How many kites left: {len(kites)}")
print(f"Have blue? {'blue' in kites}")

# 5. Add new colors with split and add
new_kites = "pink,orange,white".split(",")
kites.extend(new_kites)

# 6. Join with |
print(f"{' | '.join(kites)}")

# 7. Real copy
copy_kites = kites.copy()
copy_kites.append("gold")
print(f"{len(kites)} {len(copy_kites)}")

# 8. Nested list
prices = [["small", 50], ["big", 150]]
print(f"Big kite price: {prices[1][1]}")


# output

# Sold: yellow
# Stock: ['black', 'blue', 'red']
# First two: ['black', 'blue']
# How many kites left: 3
# Have blue? True
# black | blue | red | pink | orange | white
# 6 7
# Big kite price: 150