def duplicates(numbers):
    # O(n^2)
    for num1 in range(len(numbers)):
        for num2 in range(num1 + 1, len(numbers)):
            if numbers[num1] == numbers[num2]:
                print(f"{numbers[num1]} is a duplicate")
                break
    print("...The End...")


numbers = [3, 6, 2, 4, 3, 6, 8, 9]
duplicates(numbers)
