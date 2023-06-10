from aocd import data

numbers = [x for x in data.splitlines()[0].split(',')]
boards = data.split('\n\n')[1:]
boards = [x.split() for x in boards]

def print_board(board):
    idx = 0
    for _ in range(5):
        print(board[idx : idx + 5])
        idx += 5
    print()

def check_board(board):
    marked_indices = [i for i, val in enumerate(board) if val == 'X']

    if len(marked_indices) < 5:
        return False
    
    winning_indices = [
        [0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9],
        [10, 11, 12, 13, 14],
        [15, 16, 17, 18, 19],
        [20, 21, 22, 23, 24],
        [0, 5, 10, 15, 20],
        [1, 6, 11, 16, 21],
        [2, 7, 12, 17, 22],
        [3, 8, 13, 18, 23],
        [4, 9, 14, 19, 24]
    ]

    for seq in winning_indices:
        win = True
        for idx in seq:
            if idx not in marked_indices:
                win = False

        if win:
            return True

    return False

def calc_score(board):
    return sum([int(num) for num in board if num != 'X'])

def part1():
    winners = [False] * len(boards)
    p1 = None

    for drawn in numbers:
        for i in range(len(boards)):
            boards[i] = ['X' if x == drawn else x for x in boards[i]]
            if check_board(boards[i]):
                if not p1:
                    p1 = f'part 1: {calc_score(boards[i]) * int(drawn)}'

                if winners[i] == False:
                    winners[i] = True

                    if False not in winners:
                        print(p1)
                        print(f'part 2: {calc_score(boards[i]) * int(drawn)}')

part1()