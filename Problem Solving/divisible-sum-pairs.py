def divisibleSumPairs(n: int, k: int, arr: list) -> int:
    """
    This function takes an integer n, an integer k, and a list of integers arr as input.
    It calculates and returns the number of pairs (i, j) where i < j, and (arr[i] + arr[j]) is divisible by k.

    :param n: The number of elements in the array arr.
    :param k: The divisor for checking divisibility.
    :param arr: A list of integers.
    :return: The count of valid pairs (integers).
    """

    valid_pair_count = 0

    # Time complexity: O(n^2), where n equals to the number of elements in the input list arr
    for start_index in range(0, n):
        # Ensure start_index < end_index to avoid counting the same pair twice
        for end_index in range(start_index + 1, n):
            if (arr[start_index] + arr[end_index]) % k == 0:
                valid_pair_count += 1

    return valid_pair_count


if __name__ == "__main__":
    n = 6
    arr = [1, 3, 2, 6, 1, 2]
    k = 3
    print(divisibleSumPairs(n, k, arr))
