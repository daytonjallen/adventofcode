def count_depth_increases(depths: list[int]) -> int:
    """Counts the number of times a depth measurement increases.

    Args:
        depths (List[int]): depth measurements

    Returns:
        int: the number of times a depth measurement increases
    """
    if len(depths) <= 1:
        return 0

    numberOfIncreases = 0
    lastDepth = depths[0]

    for depth in depths[1:]:
        if depth > lastDepth:
            numberOfIncreases += 1
        lastDepth = depth
    return numberOfIncreases


with open("./testcase.txt", "r") as test_file:
    lines = test_file.readlines()
    test_data = [int(line.strip()) for line in lines]

result = count_depth_increases(test_data)
print(result)
