def greet(first_name="john", last_name="doe"): #default parameter values
    print(f"Hello, {first_name} {last_name}!")

greet("raiyeem") #adding user values
greet() #using default values

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
greet(first_name) #using user input values

# learning: if default values are used and only one agrument is provided, the other parameter takes the default value.
#here the greet(first_name) is adding the user input value to first_name parameter and last_name takes the default value "doe".

greet(first_name,last_name)