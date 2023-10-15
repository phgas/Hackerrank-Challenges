def divisibleSumPairs(n: int, k: int, arr: list) -> int:
    """
    """

    valid_pair_count = 0

    # Time complexity: O(n^2), where n is the number of elements in the input list arr
    for start_index in range(0, n):
        # Ensure start_index < end_index to avoid counting the same pair twice
        for end_index in range(start_index + 1, n):
            if (arr[start_index] + arr[end_index]) % k == 0:
                valid_pair_count += 1

    return valid_pair_count


n = 6
arr = [1, 3, 2, 6, 1, 2]
k = 3
print(divisibleSumPairs(n, k, arr))
