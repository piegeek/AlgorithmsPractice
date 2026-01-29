import sys
import math

# Had help implementing this
def roots():
    C, test_cases = parse_input()

    for n, coeffs in test_cases:
        print(solve_roots(n, coeffs))

def solve_roots(n, coeffs):
	if n <= 2:
		return solve_roots_naive(n, coeffs)

	f_prime = dy_dx(n, coeffs)

	local_minmaxes = solve_roots(n-1, f_prime)

	local_minmaxes = [-26] + local_minmaxes + [26]

	print(local_minmaxes)

	ret = []

	for i in range(len(local_minmaxes)-1):
		x1, x2 = local_minmaxes[i], local_minmaxes[i+1]
		y1, y2 = f(x1, n, coeffs), f(x2, n, coeffs)

		if y1 * y2 > 0:
			continue
		elif (y1 > y2):
			x1, x2 = x2, x1
			y1, y2 = y2, y1

		for it in range(100+1):
			mx = (x1 + x2) / 2
			my = f(mx, n, coeffs)

			if y1 * my > 0:
				y1 = my
				x1 = mx
			else:
				y2 = my
				x2 = mx

		ret.append((x1 + x2) / 2)

	ret = sorted(ret)

	return ret

def solve_roots_naive(n, coeffs):
	if n == 1:
		return [(-1) * (coeffs[1] / coeffs[0])]

	if n == 2:
		a, b, c = coeffs
		return sorted([
			(-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a),
			(-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
		])

def dy_dx(n, coeffs):
	f_prime = []

	for i in range(0, n):
		f_prime.append(coeffs[i] * (n-i))

	return f_prime

def f(x, n, coeffs):
	y = 0

	for i in range(n+1):
		y += coeffs[i] * (x ** (n - i))

	return y

def parse_input():
    input = sys.stdin.readline

    # Number of test cases
    C = int(input().strip())
    test_cases = []

    for _ in range(C):
        # Degree of the polynomial
        n = int(input().strip())

        # Coefficients from highest degree to constant term
        coeffs = list(map(float, input().split()))
        assert len(coeffs) == n + 1

        test_cases.append((n, coeffs))

    return C, test_cases


# Example usage
if __name__ == "__main__":
	roots()