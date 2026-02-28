def greedy(N, M, positions):
    positives = sorted([x for x in positions if x > 0], reverse=True)
    negatives = sorted([abs(x) for x in positions if x < 0], reverse=True)

    max_dist = max(max(positives, default=0),
                   max(negatives, default=0))

    total = 0

    for side in [positives, negatives]:
        for i in range(0, len(side), M):
            total += 2 * side[i]

    return total - max_dist