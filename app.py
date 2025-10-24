print('Raiyeem :)')
x = 1
xx = 222
slicing_string = 'raiyeem needs to finish'

print(slicing_string[:])  # this prints the whole thing

# here [] does the slicing where first one is starting and where to end but not inclusing the last one
print(slicing_string[0:7])

cat_one = 'lalu'
cat_two = 'abu'
cat_three = 'bahadur'

message = (
    f"***  My first cat was {cat_one} \nMy second cat was {cat_two}\nMy last one was {cat_three}\n Trick question which cat was my favorite the length of the name is {len(cat_three)}  ***")

print(message.strip())
# any valid expression can be added in between {} when f string is used so {2+2} will show 4

print(cat_three.upper())

print(message.find("baha"))
print(message.find("Trick"))

print(message[63:])

print("abu" not in message)

# how to show complex number?
x = 1 +2j
print(abs(x) + x)
