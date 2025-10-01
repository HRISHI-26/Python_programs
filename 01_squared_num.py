def get_squared_number(numbers):
    squared_numbers = []
    for num in numbers:
        squared_numbers.append(num * num)
    return squared_numbers


numbers = [12, 15, 19, 16, 20]
print(f"Numbers: {numbers}")
print(f"Squares: {get_squared_number(numbers)}")
