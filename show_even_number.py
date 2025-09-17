def is_even(num):
    """Return True if num is even."""
    return num % 2 == 0


def number_shower(numbers):
    """Print each number in the list."""
    for i in numbers:
        print(i)
    # return numbers not needed


# Method 1 - using for loop
print("Method 1 - using logical loops")
count = 0
for i in range(1, 11):
    if is_even(i):
        print(i)
        count += 1
print(f"We have {count} even numbers")
print("*" * 10)

# Method 2 - list comprehension
print("Method 2 - list comprehension")
even_numbers = [i for i in range(1, 11) if is_even(i)]
number_shower(even_numbers)
print(f"We have total {len(even_numbers)} even numbers {even_numbers}")
print("*" * 10)

# Method 3 - using filter function
print("Method 3 using filter function")
even_numbers = list(filter(is_even, range(1, 11)))
number_shower(even_numbers)
print(f"We have total {len(even_numbers)} even numbers {even_numbers}")

odd_numbers = list(filter(lambda x: not is_even(x), range(1, 11)))
number_shower(odd_numbers)
print(f"We have total {len(odd_numbers)} odd numbers {odd_numbers}")
print("*" * 10)
