def breakingRecords(scores: list) -> list:
    """
    This function takes a list of scores as input and returns a list that indicates the number of times a new record
    for the highest score and the lowest score was broken.

    :param scores: A list of scores.
    :return: A list with two integers: [Number of times the highest record was broken, Number of times the lowest record was broken].
    """

    min_score = scores[0]
    max_score = scores[0]
    records = [0, 0]

    # Time complexity: O(n), where n is the number of elements in scores
    for score in scores:
        if score < min_score:
            records[1] += 1
            min_score = score
        elif score > max_score:
            records[0] += 1
            max_score = score

    return records


scores = [12, 24, 10, 24]
print(breakingRecords(scores))
