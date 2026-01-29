def merge(list1, list2):
	lst = []

	longer_list = list1 if len(list1) > len(list2) else list2
	shorter_length = len(list1) if len(list1) < len(list2) else len(list2)

	i = 0
	j = 0

	while i < shorter_length and j < shorter_length:
		if list1[i] < list2[j]:
			lst.append(list1[i])
			i += 1
		else:
			lst.append(list2[j])
			j += 1

	lst = lst[0:shorter_length] + longer_list[shorter_length:]

	return lst

def merge_sort(nums, start, end):

	if len(nums) == 1:
		return nums

	mid_point = len(nums) // 2

	left_sorted = merge_sort(nums[0:mid_point], 0, mid_point) # Pass only nums as argument
	right_sorted = merge_sort(nums[mid_point:end], mid_point, end)

	sorted = merge(left_sorted, right_sorted)

	return sorted

def main():
	n = int(input())

	nums = []

	for i in range(n):
		nums.append(int(input()))

	nums = merge_sort(nums, 0, len(nums))

	for num in nums:
		print(num)

if __name__ == "__main__":
	main()