numbers = [10,5,25,3,8]

maximum = numbers[0]
minimum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

    if num < minimum:
        minimum = num

print("Maximum:", maximum)
print("Minimum:", minimum)