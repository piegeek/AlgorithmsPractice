import sys
import math

def pass486():
    c, test_cases = parse_input()

    for n, lo, hi in test_cases:
        solve_pass486(n, lo, hi)

def solve_pass486(n, lo, hi):
	# O(hi-lo) * O(i) => O(x^2): Too slow
	
	# count = 0

	# for i in range(lo, hi+1):
	# 	if has_n_divisors(i, n):
	# 		count += 1

	# print(count)
	# return count

	# Still too slow
	count = 0

	primes_cache = {}
	is_prime_cache = {}

	for i in range(lo, hi+1):
		if factor_count(i, primes_cache, is_prime_cache) == n:
			count += 1

	print(count)
	return count

def factor_count(integer, primes_cache, is_prime_cache):
	primes = get_primes_under(integer, primes_cache, is_prime_cache)
	exponents = [ 0 for _ in range(len(primes)) ]

	# print(primes)

	number = integer

	for i in range(len(primes)):
		exponent_count = 0
		while number % primes[i] == 0:
			number /= primes[i]
			exponent_count += 1

		exponents[i] = exponent_count
	
	num_of_factors = 1

	for i in range(len(primes)):
		if exponents[i] > 0:
			num_of_factors *= (exponents[i] + 1)

	return num_of_factors

def get_primes_under(integer, primes_cache, is_prime_cache):
	if integer in primes_cache: return primes_cache[integer]

	primes = []
	for i in range(2, integer):
		if is_prime(i, is_prime_cache):
			primes.append(i)

	if is_prime(integer, is_prime_cache) and integer not in primes:
		primes.append(integer)

	primes_cache[integer] = primes
	return primes

def is_prime(i, is_prime_cache):
	if i < 2: return False
	if i == 2: return True

	if i in is_prime_cache: return is_prime_cache[i]

	# for j in range(2, i):
	# 	if i % j == 0:
	# 		is_prime_cache[i] = False
	# 		return False
	
	# Optimized version
	if (i % 2) == 0: return False

	for div in range(3, int(math.sqrt(i))+1, 2):
		if i % div == 0: 
			is_prime_cache[i] = False
			return False

	is_prime_cache[i] = True
	return True

def has_n_divisors(i, n):
	count = 0

	for x in range(1, i+1):
		if count > n: return False

		if i % x == 0:
			count += 1

	return count == n

def parse_input():
    input = sys.stdin.readline

    # Number of test cases
    c = int(input().strip())
    test_cases = []

    for _ in range(c):
        # Read n, lo, hi
        n, lo, hi = map(int, input().split())
        test_cases.append((n, lo, hi))

    return c, test_cases


# Example usage
if __name__ == "__main__":
	pass486()