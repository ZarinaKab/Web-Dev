import re

n, m = map(int, input().split())
matrix = []
for i in range(n):
    matrix.append(input())

# Combine the characters in the matrix into a single string, reading down the columns
message = ""
for j in range(m):
    for i in range(n):
        message += matrix[i][j]

# Use regular expressions to remove any non-alphanumeric characters between two alphanumeric characters
decoded_message = re.sub(r"(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])", " ", message)

print(decoded_message)
