def find_column_with_largest_sum(matrix):

    if not matrix or not (matrix[0]):
        return -1

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    max_sum = float('-inf')
    max_col_index = -1

    for j in range(num_cols):
        current_col_sum = 0
        for i in range(num_rows):
            current_col_sum +=matrix[i][j]

        if current_col_sum > max_sum:
            max_sum = current_col_sum
            max_col_index = j
    return max_col_index
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result_column_index = find_column_with_largest_sum(matrix)
print(result_column_index)
