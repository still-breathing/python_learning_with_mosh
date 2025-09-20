print(" this is 2D list \n ")
matrix = [
    [1, 2, 3],  # row 0 --> matrix[0]
    [4, 5, 6],  # row 1 --> matrix[1]
    [7, 8, 9]   # row 2 --> matrix[2                                    
]   
print(matrix)
print(f"accessing the first row {matrix[0]}")
print(f"accessing the first element of first row {matrix[0][0]}")
print(f"accessing the second element of first row {matrix[0][1]}")
print(f"accessing the third element of first row {matrix[0][2]}")
print(f"accessing the second element of second row {matrix[1][1]}")
print(f"accessing the third element of third row {matrix[2][2]}")
print("\n iterating over 2D list \n")

for row,columns in matrix:
    for item in row:
        print(item)
print("\n END \n")