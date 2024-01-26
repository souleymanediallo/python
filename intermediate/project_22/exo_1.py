def get_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum, maximum

lengths = [79, 77, 55, 23, 56, 90, 29]
minimum, maximum = get_stats(lengths)
print(f"Min: {minimum}, Max: {maximum}")
