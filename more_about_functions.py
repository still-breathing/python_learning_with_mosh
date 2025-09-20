def multiplier(number, multiplier = 1):
    """Multiplies a number by a multiplier.

    Args:
        number (int, float): The number to be multiplied.
        multiplier (int, float, optional): The multiplier. Defaults to 1.

    Returns:
        int, float: The result of the multiplication.
    """
    return number * multiplier

print("\nExample of a function with a default parameter")
print(f"\n5 multiplied by default multiplier is {multiplier(5)}")
print(f"\n5 multiplied by 3 is {multiplier(5, 3)}")

