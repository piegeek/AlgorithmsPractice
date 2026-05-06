def heap_insert(heap, num):
	heap.append(num)

	heap[0], heap[-1] = heap[-1], heap[0]

	for i in range(len(heap)):
		# TODO: When i == 0; 2*i == 0, 2*i+1 == 1 -> Done

		if i == 0 and len(heap) == 1:
			break
		elif i == 0 and len(heap) == 2:
			if heap[0] < heap[1]:
				heap[0], heap[1] = heap[1], heap[0]
			else:
				break
		elif i == 0 and len(heap) >= 3:
			if heap[0] > heap[1] and heap[0] > heap[2]:
				continue
			elif heap[0] < heap[1] and heap[0] > heap[2]:
				heap[0], heap[1] = heap[1], heap[0]
			elif heap[0] > heap[1] and heap[0] < heap[2]:
				heap[0], heap[2] = heap[2], heap[0]
			else:
				if heap[1] < heap[2]:
					heap[0], heap[2] = heap[2], heap[0]
				else:
					heap[0], heap[1] = heap[1], heap[0]
			continue

		if 2*i+1 < len(heap):
			if heap[i] > heap[2*i] and heap[i] > heap[2*i+1]:
				pass
			elif heap[i] < heap[2*i] and heap[i] > heap[2*i+1]:
				heap[i], heap[2*i] = heap[2*i], heap[i]
			elif heap[i] > heap[2*i] and heap[i] < heap[2*i+1]:
				heap[i], heap[2*i+1] = heap[2*i+1], heap[i]
			else:
				if heap[2*i] > heap[2*i+1]:
					heap[i], heap[2*i] = heap[2*i], heap[i]
				else:
					heap[i], heap[2*i+1] = heap[2*i+1], heap[i]
		elif 2*i < len(heap):
			if heap[i] > heap[2*i]:
				pass
			else:
				heap[i], heap[2*i] = heap[2*i], heap[i]
		else:
			pass

	print(heap)

def make_heap(num):
	if num < 1:
		return []

	heap = make_heap(num - 1)
	
	heap_insert(heap, num)

	return heap



def main():
	n = int(input())

	heap = make_heap(n)

	heap_strfied = [ str(item) for item in heap ]

	ans = " ".join(heap_strfied)

	# print(ans)

if __name__ == "__main__":
	main()