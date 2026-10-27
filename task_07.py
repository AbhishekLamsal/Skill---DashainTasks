# Report card

# Calculate the average marks
def get_average(marks):
    """Returns the average marks rounded to 2 decimal places."""
    return round(sum(marks) / len(marks), 2)


# Convert average marks into a grade
def get_grade(avg):
    if avg >= 80:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "Fail"

# Display a student's result summary
def report(name, marks, pass_mark=40):
    avg = get_average(marks)
    grade = get_grade(avg)

    print(f"{name}: avg {avg:.2f}, grade {grade}")
    print(f"  Best: {max(marks)} | Worst: {min(marks)}")
    print(f"  Passed all? {min(marks) >= pass_mark}")

    return avg

# Student names
names = ["Sita", "Ram", "Gita"]

# Marks obtained by each student
all_marks = [
    [85, 90, 78],
    [45, 60, 38],
    [70, 80, 65]
]

# Store averages for ranking
averages = []

# Process each student and their marks
for name, marks in zip(names, all_marks):
    avg = report(name, marks)
    averages.append(avg)

# Sort averages from highest to lowest
ranked = sorted(averages, reverse=True)

# Display rankings
for rank, avg in enumerate(ranked, start=1):
    print(f"Rank {rank}: {avg:.2f}")


# output

# Sita: avg 84.33, grade A
#   Best: 90 | Worst: 78
#   Passed all? True
# Ram: avg 47.67, grade C
#   Best: 60 | Worst: 38
#   Passed all? False
# Gita: avg 71.67, grade B
#   Best: 80 | Worst: 65
#   Passed all? True
# Rank 1: 84.33
# Rank 2: 71.67
# Rank 3: 47.67