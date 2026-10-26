def average(numbers):
    """Return the arithmetic mean, or None if no values were supplied."""
    values = list(numbers)
    if not values:
        return None
    return sum(values) / len(values)


if __name__ == "__main__":
    samples = [4, 8, 12]
    result = average(samples)
    print("Average:", result if result is not None else "No values supplied")
