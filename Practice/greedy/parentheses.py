import sys

INF = 10 ** 9

# BOJ 1541
def parentheses():
    numbers, operators = parse_input()
    solve_parentheses(numbers, operators)

def solve_parentheses(numbers, operators):
    ret = dp(0, len(numbers) - 1, numbers, operators)

    print(ret)
    return ret

def dp(left, right, numbers, operators):
    if right - left == 1:
        operator = operators[left]
        if operator == '+':
            return numbers[left] + numbers[right]
        else:
            return numbers[left] - numbers[right]

    ret = numbers[left]
    for i in range(left+1, right+1):
        if operators[i-1] == '+':
            ret += numbers[i]
        else:
            ret -= numbers[i]

    for i in range(left + 1, right):
        operator = operators[i-1]
        if operator == '+':
            ret = min(ret, dp(left, i, numbers, operators) + dp(i+1, right, numbers, operators))
        else:
            ret = min(ret, dp(left, i, numbers, operators) - dp(i+1, right, numbers, operators))

    return ret

def parse_input():
    input = sys.stdin.readline  # fast input
    
    expression = input().strip()

    numbers = []    
    operators = []

    last_char_idx = 0

    for i in range(len(expression)):
        if expression[i] in ['-', '+']:
            operators.append(expression[i])
            numbers.append(expression[last_char_idx:i])
            last_char_idx = i + 1

    numbers.append(expression[last_char_idx:])

    numbers = list(map(int, numbers))
    
    return numbers, operators


# Example usage
if __name__ == "__main__":
    parentheses()