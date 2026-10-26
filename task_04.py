# Dashain family visits

# 1. Tuple and unpacking
trip = ("Pokhara", 3, "bus")
place, days, transport = trip

print(f"Going to {place} for {days} days by {transport}")

# 2. Sets
sita = {"hajurba", "kaka", "fupu", "mama"}
ram = {"hajurba", "kaka", "maiju"}

print(f"Houses Sita Visited: {sorted(sita)}")
print(f"Houses Ram Visited: {sorted(ram)}")

# 3. Set operations
print(f"Both: {sorted(sita & ram)}")
print(f"Everyone: {sorted(sita | ram)}")
print(f"Only Sita: {sorted(sita - ram)}")

# 4. Unique guests
guests = ["ram", "hari", "ram", "sita", "hari"]
unique_guests = set(guests)

print(f"Guests: {guests}")
print(f"Unique guests: {len(unique_guests)}")

# 5. Dictionary operations
tika_money = {"hajurba": 500, "kaka": 200}

tika_money["mama"] = 1000

tika_money["mama"] = 1100

tika_money.update({"fupu": 300})
print(f"Tika money: {tika_money}")

# 6. get() and pop()
print(f"Maiju gave: {tika_money.get('maiju', 0)}")

removed = tika_money.pop("kaka")
print(f"Removed kaka: {removed}")

print(f"Tika money: {tika_money}")

# 7. Dictionary, keys, total
print(f"{tika_money}")
print(f"People: {list(tika_money.keys())}")
print(f"Total: {sum(tika_money.values())}")

# 8. Dictionary inside dictionary
places = {"trip": {"city": "Kathmandu", "days": 5, "transport": "plane"}}

print(f"{places['trip']['city']}")


# output

# Going to Pokhara for 3 days by bus
# Houses Sita Visited: ['fupu', 'hajurba', 'kaka', 'mama']
# Houses Ram Visited: ['hajurba', 'kaka', 'maiju']
# Both: ['hajurba', 'kaka']
# Everyone: ['fupu', 'hajurba', 'kaka', 'maiju', 'mama']
# Only Sita: ['fupu', 'mama']
# Guests: ['ram', 'hari', 'ram', 'sita', 'hari']
# Unique guests: 3
# Tika money: {'hajurba': 500, 'kaka': 200, 'mama': 1100, 'fupu': 300}
# Maiju gave: 0
# Removed kaka: 200
# Tika money: {'hajurba': 500, 'mama': 1100, 'fupu': 300}
# {'hajurba': 500, 'mama': 1100, 'fupu': 300}
# People: ['hajurba', 'mama', 'fupu']
# Total: 1900
# Kathmandu