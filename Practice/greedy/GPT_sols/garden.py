def greedy(N, flowers):
    # Convert dates first if needed
    # flowers.sort(key=lambda x: (x[0], x[1]))

    idx = 0
    count = 0
    end_time = 3.01

    while end_time <= 11.30:
        max_end = end_time

        while idx < N and flowers[idx][0] <= end_time:
            max_end = max(max_end, flowers[idx][1])
            idx += 1

        # Cannot extend coverage
        if max_end == end_time:
            return 0

        end_time = max_end
        count += 1

    return count