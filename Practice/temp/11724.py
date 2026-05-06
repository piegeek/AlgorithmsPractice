from queue import Queue

def init(graph_lst):
	num_nodes = graph_lst[0][0]
	num_edges = graph_lst[0][1]

	return [num_nodes, num_edges]

def main(lst):
	num_nodes, num_edges = init(lst)

	q = Queue(maxsize=num_nodes)
	
	for i in range(1,num_edges + 1):
		q.put(lst[i][0])
		q.put(lst[i][1])

		