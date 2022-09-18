def calculate_winning_score(called_numbers: list[str], boards: list[list[str]]) -> int:
    """Calculates the winning score.

    Args:
        called_numbers (list[str]): called numbers
        boards (list[list[str]]): board data

    Returns:
        int: winning score
    """
    for called_number in called_numbers:
        for i, board in enumerate(boards):
            if {called_number} in board:
                return calculate_board_score(called_number, board)
            else:
                boards[i] = [row - {called_number} for row in board]


def create_boards(board_data):
    boards = []
    for board in board_data:
        rows = [[int(i) for i in row.split()] for row in board.split("\n")]
        boards.append([set(row) for row in rows])
        boards.append([set(col) for col in zip(*rows)])
    return boards


def calculate_board_score(number_called: int, board: list[int]):
    """Calculates board score.

    Args:
        number_called (int): called number
        board (list[int]): board

    Returns:
        _type_: board score
    """
    return (sum(sum(group) for group in board) - number_called) * number_called


with open("./testcase.txt", "r") as test_file:
    called_numbers, *boards = test_file.read().split("\n\n")
    called_numbers = map(int, called_numbers.strip().split(","))
    boards = create_boards(boards)
result = calculate_winning_score(called_numbers, boards)
print(result)
