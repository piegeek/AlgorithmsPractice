def dfs_dp(idx, visited, mod, less, sorted_e, original_e, m, cache):
    n = len(sorted_e)
    mask = 0
    for i in range(n):
        if visited[i]:
            mask |= (1 << i)

    if (mask, mod, less) in cache:
        return cache[(mask, mod, less)]

    # Base case: all digits used
    if idx == n:
        return 1 if less and mod == 0 else 0

    count = 0

    for i in range(n):
        if visited[i]:
            continue

        # Duplicate skip
        if i > 0 and sorted_e[i] == sorted_e[i-1] and not visited[i-1]:
            continue

        digit = int(sorted_e[i])

        # Tight constraint
        if not less and digit > int(original_e[idx]):
            continue

        new_less = less or (digit < int(original_e[idx]))
        new_mod = (mod * 10 + digit) % m

        visited[i] = True
        count += dfs_dp(
            idx + 1,
            visited,
            new_mod,
            new_less,
            sorted_e,
            original_e,
            m,
            cache
        )
        visited[i] = False

    cache[(mask, mod, less)] = count
    return count
