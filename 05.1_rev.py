text = input("Enter the string: ")
reverse = ""

for char in text:
    reverse = char + reverse

print("Reversed string:", reverse)