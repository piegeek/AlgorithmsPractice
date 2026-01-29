import sys
import copy

def zimbabwe():
    c, test_cases = parse_input()
    for e, m in test_cases:
        solve_zimbabwe(e, m)



# 1 2 3 4 2 5 

# What this solution differs from the book's solution
def solve_zimbabwe(e, m):
  # Brute force; too slow
  perms = []
  get_perms(e, perms)

  # Filter out permutations; smaller than e
  possible = []

  for perm in perms:
    price = int(''.join(perm))
    if price < e:
      possible.append(price)

  count = 0

  for price in possible:
    if price % m == 0:
      count += 1

  print(count)


def get_perms(e, perms):
  letters = list(str(e))
  N = len(letters)

  # 각 숫자(0~9)가 몇 개 있는지 카운트
  count = [0] * 10
  for ch in letters:
    count[int(ch)] += 1

  stack = []

  # 첫 자리 숫자 <= 원래 첫 자리 숫자인 경우만 탐색 (Pruning)
  first_digit = int(letters[0])
  for digit in range(0, first_digit + 1):
    if count[digit] > 0:
      dfs(digit, count, stack, N, perms, letters)


def dfs(digit, count, stack, N, perms, letters):
  # 해당 숫자 사용
  count[digit] -= 1
  stack.append(str(digit))

  # Pruning: 현재까지 만든 수가 원래 수의 prefix보다 크면 중단
  if int(''.join(stack)) > int(''.join(letters[:len(stack)])):
    # Backtracking
    count[digit] += 1
    stack.pop()
    return

  if len(stack) == N:
    perms.append(stack[:])  # 복사본 저장
    # Backtracking
    count[digit] += 1
    stack.pop()
    return

  # 다음 자리에 올 수 있는 숫자들 탐색 (0~9 순서대로)
  for next_digit in range(0, 10):
    if count[next_digit] > 0:
      dfs(next_digit, count, stack, N, perms, letters)

  # Backtracking
  count[digit] += 1
  stack.pop()


def parse_input():
    input = sys.stdin.readline

    # Number of test cases (c ≤ 50)
    c = int(input().strip())
    test_cases = []

    for _ in range(c):
        # Two natural numbers e and m
        # e: 1 ≤ e ≤ 10^14
        # m: 2 ≤ m ≤ 20
        e, m = map(int, input().split())
        test_cases.append((e, m))

    return c, test_cases


# Example usage
if __name__ == "__main__":
  zimbabwe()