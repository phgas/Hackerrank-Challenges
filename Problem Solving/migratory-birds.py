def migratoryBirds(arr: list) -> int:
    """
    Determines the most frequently occurring bird type from the list.
    In case of a tie, returns the smallest bird type number.

    :param arr: A list of segments (integers).
    :return: The lowest type id of the most frequently sighted birds (integer).
    """
    bird_counts = [0] * len(arr)

    # Time complexity: O(n), where n equals to the number of elements in the input list arr
    for bird in arr:
        bird_counts[bird] += 1

    return bird_counts.index(max(bird_counts))


if __name__ == "__main__":
    arr = [1, 4, 4, 4, 5, 3]
    print(migratoryBirds(arr))
