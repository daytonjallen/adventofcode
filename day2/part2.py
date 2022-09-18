from typing import List, Tuple


def calculatePosition(commands: List[Tuple[str, int]]) -> int:
    """Calculates submarines final position

    Args:
        commands (List[Tuple[str, int]]): command and value tuple

    Returns:
        int: final position
    """
    horizontalPosition = 0
    depthPosition = 0
    aim = 0

    for command, value in commands:
        if command == "forward":
            horizontalPosition += value
            depthPosition += aim * value
        elif command == "down":
            aim += value
        else:
            aim -= value

    return horizontalPosition * depthPosition


with open("./testcase.txt", "r") as test_file:
    lines = test_file.readlines()
    test_data = [
        (command, int(value))
        for (command, value) in (line.split(" ") for line in lines)
    ]

result = calculatePosition(test_data)
print(result)
