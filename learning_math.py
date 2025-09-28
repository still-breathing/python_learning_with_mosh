#!/usr/bin/python3

sum = 0
fruit = "apple"
item = "bag"

def summing_string(s):
    total = 0
    for i in s:
        total += ord(i)
    return total
def printer(args):
    print(f"The sun of the ASCII values in {args} is {summing_string(args)}")


for i in fruit:
    print(i)

# for i in fruit:
#     print(i)
#     print(ord(i))
#     sum += ord(i)

printer(fruit)

printer(item)
#print(f"The sum of the ASCII values in {fruit} is {summing_string(fruit)}")

#print(f"The sum of the ASCII values in {item} is {summing_string(item)}")

#print(f"The sum of the ASCII values in {fruit} is {sum}")