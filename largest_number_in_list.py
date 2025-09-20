print("Largest number in a list")

numbers = [3, 6, 2, 8, 4, 10, 12, 7]
largest = numbers[0]  # assume the first number is the largest initially
for number in numbers:
    if number > largest:
        largest = number
print(f"The largest number in the list {numbers} is: \n{largest}")
print("\nEND\n")
