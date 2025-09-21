numbers = [1, 2, 3, 4, 3, 2, 1,7,4,13,14]

uniquie_numbers = []

for number in numbers:
    if number not in uniquie_numbers: # if number is not already in the list then append it
        uniquie_numbers.append(number)

print(uniquie_numbers)