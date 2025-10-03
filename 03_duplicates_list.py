def duplicates_list(numbers):
    duplicate = []

    # O(n^2)
    for num1 in range(len(numbers)):
        for num2 in range(num1 + 1, len(numbers)):
            if numbers[num1] == numbers[num2]:
                duplicate.append(numbers[num1])
                break

    # O(n)
    for num in duplicate:
        print(num)


numbers = [3, 6, 2, 4, 3, 6, 8, 9]
duplicates_list(numbers)
