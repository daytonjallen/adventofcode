def count_triple_depth_increases(depths: list[int], window_size: int) -> int:
    """Counts the number of times a sliding window of depth measurements increase.

    Args:
        depths (List[int]): depth measurements
        window_size (int): size of the sliding window

    Returns:
        int: the number of times a sliding window of depth measurements increase
    """
    if len(depths) <= window_size:
        return 0

    numberOfIncreases = 0

    for i in range(window_size, len(depths)):
        if depths[i - window_size] < depths[i]:
            numberOfIncreases += 1
    return numberOfIncreases


with open("./testcase.txt", "r") as test_file:
    lines = test_file.readlines()
    test_data = [int(line.strip()) for line in lines]

result = count_triple_depth_increases(test_data, 3)
print(result)
