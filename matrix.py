# Write a function that uses zip() to transpose a matrix.
def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed = transpose_matrix(matrix)
print(transposed)
