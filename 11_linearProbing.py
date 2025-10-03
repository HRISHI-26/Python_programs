arr = [23, 45, 42, 35, 12]
hash_table = {}


def hashfunction(num):
    return num % 34


keys = []


def insert(num):
    index = hashfunction(num)
    while index in keys:
        index += 1
    keys.append(index)
    hash_table[index] = num


for num in arr:
    insert(num)

print(f"Hash Table: {hash_table}")
