def birthday(s: list, d: int, m: int) -> int:
    """
    This function takes a list of integers representing chocolate squares in segments,
    a birthday day, and a birthday month as input. It calculates and returns the number
    of ways to give a gift consisting of a contiguous segment of chocolate squares with
    a total sum equal to the birthday day and a length equal to the birthday month.

    :param s: A list of segments (integers).
    :param d: Birthday day (integer).
    :param m: Birthday month (integer).
    :return: The number of valid gift possibilities (integer).
    """

    possibilities_counter = 0

    # Time complexity: O(n), where n equals to the number of elements in the input list s
    for end_index in range(m, len(s) + 1):
        sub_segment = s[end_index - m:end_index]
        if sum(sub_segment) == d and len(sub_segment) == m:
            possibilities_counter += 1

    return possibilities_counter


if __name__ == "__main__":
    s = [2, 2, 1, 3, 2]
    d = 4
    m = 2
    print(birthday(s, d, m))
