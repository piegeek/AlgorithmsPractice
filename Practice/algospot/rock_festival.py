def parse_input():
	C = int(input())

	N_L = []
	prices = []

	for i in range(C):
		N_L.append(remove_empty_str_and_intify(input().split(' ')))

		prices.append(remove_empty_str_and_intify(input().split(' ')))

	return C, N_L, prices

def remove_empty_str_and_intify(lst):
	out = []

	for item in lst:
		if item != '':
			out.append(int(item))

	return out

def rock_festival():
	C, N_L, prices = parse_input()

	for x in range(C):
		N = N_L[x][0]
		L = N_L[x][1]
		price = prices[x]

		min_avg_price = float('inf')

		for i in range(L, N+1):
			for j in range(0, N-i):
				min_avg_price = min(min_avg_price, sum(price[j:j+i]) / i)

		print(min_avg_price)


if __name__ == '__main__':
	rock_festival()