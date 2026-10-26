# Intentionally buggy example. Do not use for real calculations.
def average(numbers):
    total = sum(numbers)
    return total / len(numbers)  # crashes when numbers is empty

print(average([]))
