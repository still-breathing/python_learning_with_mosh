# learning functions
# The can be two types of functions,
# One performs a task and the other returns a value

# Example of a function that performs a task
def greet_user(first_name, last_name): # These are parameters
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")

# Example of a function that returns a value


def square(number):
    return number * number


# Calling the function that performs a task
print("\nExample of a function that performs a task")
greet_user("Raiyeem", "Farhan") # These are arguments

# Calling the function that returns a value

print("\nExample of a function that returns a value")
result = square(5)
print(f"The square of 5 is {result}")
