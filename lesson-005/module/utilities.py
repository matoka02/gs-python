def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def find_max(numbers):
    if not numbers:
        return None
    return max(numbers)