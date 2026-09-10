numbers = [1, 2, 3, 2, 4, 1, 5]

duplicates = []

for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print("Duplicate elements:", duplicates)