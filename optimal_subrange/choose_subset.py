from typing import List
import operator

def choose_subset(numbers: List[int] , k: int, sorted: bool = True) -> List[int]:
    """Chooses k elements from the input list of positive numbers, maximising scatter."""

    # Edge cases
    n = len(numbers)
    if k >= n:
        return numbers
    elif k < 0:
        return []

    # Sort input array if it isn't already
    if not sorted:
        numbers.sort()

    # Allocate the dynamic programming (dp) table and parent pointers (pp)
    dp = [[-1 for _ in range(n)] for _ in range(k)]
    pp = [[-1 for _ in range(n)] for _ in range(k)]

    # Edge case, because choosing two points from a sorted list is always the extreme
    for j in range(1, n):
        dp[1][j] = numbers[j] - numbers[0]
        pp[1][j] = 0
    
    # Fill in rest of the DP table
    for i in range(2, k):
        for j  in range(i, n):
            candidates = []
            for l in range(0, j):
                candidates.append(min(dp[i-1][l], numbers[j] - numbers[l]))
            pp[i][j], dp[i][j] = max(enumerate(candidates), key=operator.itemgetter(1))

    # Backtrace the DP table to choose the k optimal points
    result = [numbers[-1]]
    j = n-1
    for i in range(k-1, 0, -1):
        result.append(numbers[pp[i][j]])
        j = pp[i][j]
    result.reverse()
    
    return result
