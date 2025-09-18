prices = [10, 20, 30]

sum = 0
for price in prices:  # just to clear the concept here the first price is kind of variable it can be anything
    sum += price  # just for that example price is used

print("Example of iterating over a list, summing up the values")
print(f"\nThe prices are {prices}")
print(f"\nThe total price is {sum}")

print("\nExample of nested loops")
for x in range(4):  # outer loop
    for y in range(3):  # inner loop
        print(f"({x}, {y})")

# Task show the letter F in the console using nested loops
print("\nShowing the letter F using nested loops")
for x in range(7):
    for y in range(5):
        # found out the first condition controls the "x" shown in console

        # TODO: modify the conditions to get the desired output find out how to make the F thicker
        if (y < 2) or (x == 0 and y < 4) or (x == 3 and y < 4):
            print("X", end="")
        else:
            print(" ", end="")
    print()  # to move to the next line after each row
