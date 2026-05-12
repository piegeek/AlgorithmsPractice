# Read matrix
grid = [list(map(int, input().split())) for _ in range(n)]

# Read list of strings
grid = [input().strip() for _ in range(n)]

# Read characters
chars = list(input().strip())

# Read tuple list
pairs = [tuple(map(int, input().split())) for _ in range(n)]

# Output space-separated
print(*arr)

# YES / NO
print("YES")
print("NO")