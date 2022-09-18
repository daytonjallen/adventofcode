def calculate_position(commands: list[tuple[str, int]]) -> int:
    """Calculates submarines final position

    Args:
        commands (List[Tuple[str, int]]): command and value tuple

    Returns:
        int: final position
    """
    horizontalPosition = 0
    depthPosition = 0

    for command, value in commands:
        if command == "forward":
            horizontalPosition += value
        elif command == "down":
            depthPosition += value
        else:
            depthPosition -= value

    return horizontalPosition * depthPosition


with open("./testcase.txt", "r") as test_file:
    lines = test_file.readlines()
    test_data = [
        (command, int(value))
        for (command, value) in (line.strip().split(" ") for line in lines)
    ]

result = calculate_position(test_data)
print(result)
