from collections import Counter


def calculate_life_support_rating(diagnostics: list[str]) -> int:
    """Calculates the life support rating of the submarine.

    Args:
        diagnostics (list[str]): list of diagnostic readings

    Returns:
        int: the life support rating of the submarine
    """
    o2_generator_rating = calculate_oxygen_generator_rating(diagnostics)
    co2_scrubber_rating = calculate_co2_scrubber_rating(diagnostics)
    return int(o2_generator_rating, 2) * int(co2_scrubber_rating, 2)


def calculate_oxygen_generator_rating(diagnostics: list[str]) -> str:
    """Calculates the oxygen generator rating.

    Args:
        diagnostics (list[str]): list of diagnostic readings

    Returns:
        str: oxygen generator rating
    """
    rating = ""
    diagnostics_length = len(diagnostics[0])
    o2_rating = list(diagnostics)
    for i in range(diagnostics_length):
        counts = Counter(map(lambda x: x[i], o2_rating))
        most_common_counter = counts.most_common()
        if (
            len(most_common_counter) > 1
            and most_common_counter[0][1] == most_common_counter[1][1]
        ):
            most_common = "1"
        else:
            most_common = most_common_counter[0][0]
        o2_rating = list(filter(lambda x: x[i] == most_common, o2_rating))
        rating += most_common
    return rating


def calculate_co2_scrubber_rating(diagnostics: list[str]) -> str:
    """Calculates the co2 scrubber rating.

    Args:
        diagnostics (list[str]): list of diagnostic readings

    Returns:
        str: co2 scrubber rating
    """
    rating = ""
    diagnostics_length = len(diagnostics[0])
    o2_rating = list(diagnostics)
    for i in range(diagnostics_length):
        counts = Counter(map(lambda x: x[i], o2_rating))
        most_common_counter = counts.most_common()
        if (
            len(most_common_counter) > 1
            and most_common_counter[0][1] == most_common_counter[1][1]
        ):
            most_common = "0"
        else:
            most_common = most_common_counter[-1][0]
        o2_rating = list(filter(lambda x: x[i] == most_common, o2_rating))
        rating += most_common
    return rating


with open("./testcase.txt", "r") as test_file:
    lines = test_file.readlines()
    test_data = [line.strip() for line in lines]

result = calculate_life_support_rating(test_data)
print(result)
