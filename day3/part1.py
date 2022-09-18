from collections import Counter


def calculate_power_consumption(diagnostics: list[str]) -> int:
    """Calculates the power consumption of the submarine.

    Args:
        diagnostics (list[str]): list of diagnostic readings

    Returns:
        int: the power consumption of the submarine
    """
    gamma_rate = calculate_gamma_rate(diagnostics)
    epsilon_rate = calculate_epsilon_rate(gamma_rate)
    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def calculate_gamma_rate(diagnostics: list[str]) -> str:
    """Calculates the gamma rate.

    Args:
        diagnostics (list[str]): list of diagnostic readings

    Returns:
        str: gamma rate
    """
    gamma_rate = ""
    diagnostics_length = len(diagnostics[0])
    for i in range(diagnostics_length):
        counts = Counter(map(lambda x: x[i], diagnostics))
        most_common = counts.most_common()[0][0]
        gamma_rate += most_common

    return gamma_rate


def calculate_epsilon_rate(gamma_rate: str) -> str:
    """Calculates the epsilon rate.

    Args:
        gamma_rate (str): gamma rate

    Returns:
        str: epsilon rate
    """
    return gamma_rate.translate(str.maketrans("10", "01"))


with open("./testcase.txt", "r") as test_file:
    lines = test_file.readlines()
    test_data = [line.strip() for line in lines]

result = calculate_power_consumption(test_data)
print(result)
