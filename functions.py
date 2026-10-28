"""
Function - A block of code that performs a specific task.
"""

def average(list_of_numbers):
    """
    This function takes a list of numbers and returns the average.
    """
    total = sum(list_of_numbers)
    return total / len(list_of_numbers)

def apply_discount(price, discount=10):
    """
    This function takes a price and a discount percentage and returns the discounted price.
    """
    return price - (price * discount / 100)


marks = [90, 80, 70, 60, 50]
print(f"Average: {average(marks)}")
print(f"Discounted Price: {apply_discount(100, 20)}")
print(f"Discounted Price (default discount): {apply_discount(100)}")