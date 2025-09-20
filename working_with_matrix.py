def print_matrix(matrix):
    for row in matrix:
        for item in row:
            print(f" the row is:{row} \n the item is {item}", end="\n")
        print()  # for new line after each row

print("Example of working with 2-D matrix \n ")
my_matrix = [
    [1, 2, 3],  # row 0 --> matrix[0]
    [4, 5, 6],  # row 1 --> matrix[1                        
    [7, 8, 9]   # row 2 --> matrix[2                     ]          
]
for i in my_matrix:
    print(i)

print_matrix(my_matrix)