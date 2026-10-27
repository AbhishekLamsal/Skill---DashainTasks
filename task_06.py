# Dashain countdown and savings jar

# Part A

for day in range(1, 16):
    if day == 7:
        print(f"Day {day}: Fulpati!")
        continue

    if day == 10:
        print(f"Day {day}: Vijaya Dashami, tika day!")
        break

    print(f"Day {day}")

# Part B

balance = 0

while True:
    choice = input("\n1 Add  2 Spend  3 Balance  4 Quit: ")

    if choice == "1":
        amount = int(input("Amount: "))
        balance += amount

    elif choice == "2":
        amount = int(input("Amount: "))

        if amount > balance:
            print("Not enough money!")
            continue

        balance -= amount

    elif choice == "3":
        print(f"Balance: Rs {balance}")

    elif choice == "4":
        print("Bye! Happy Dashain.")
        break

    else:
        print("Wrong choice, try again.")


# output

# Day 1
# Day 2
# Day 3
# Day 4
# Day 5
# Day 6
# Day 7: Fulpati!
# Day 8
# Day 9
# Day 10: Vijaya Dashami, tika day!

# 1 Add  2 Spend  3 Balance  4 Quit: 1
# Amount: 1200

# 1 Add  2 Spend  3 Balance  4 Quit: 2
# Amount: 1500
# Not enough money!

# 1 Add  2 Spend  3 Balance  4 Quit: 2
# Amount: 550

# 1 Add  2 Spend  3 Balance  4 Quit: 3
# Balance: Rs 650

# 1 Add  2 Spend  3 Balance  4 Quit: 4
# Bye! Happy Dashain.