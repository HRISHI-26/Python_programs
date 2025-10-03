arr = [12, 34, 23, 45, 25]
hash_table = {}


def hashfunction(num):
    return num % 34


keys = []


def insert(num):
    index = hashfunction(num)
    while index in keys:
        index *= index
    keys.append(index)
    hash_table[index] = num


for num in arr:
    insert(num)
print(f"Hash Table: {hash_table}")
