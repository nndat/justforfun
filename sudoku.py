import numpy as np


data = """
        9 1 7 | 2 5 4 | 0 0 0
        4 0 2 | 0 8 0 | 0 0 0
        6 5 0 | 0 0 3 | 4 0 0
        0 0 3 | 0 9 0 | 2 5 6 
        5 0 0 | 7 0 0 | 3 0 9 
        2 0 0 | 0 0 0 | 0 7 1 
        0 2 0 | 5 3 0 | 7 6 0
        3 7 0 | 1 6 0 | 0 9 8 
        0 0 0 | 0 0 0 | 0 3 0
        """


def print_board(board):
    for i, row in enumerate(board):
        for j, number in enumerate(row):
            print(f'{number: <2}', end='')
            if j == 2  or j == 5:
                print('| ', end='')
        print()
        if i == 2 or i == 5:
            print('-'*21)


# read input from text like above
def to_array(data):
    board = []
    data = data.strip().splitlines()

    for row in data:
        row = row.replace('x', '0')
        row = row.replace('|', '')
        row = row.split()
        row = [int(n) for n in row]
        board.append(row)

    return board


# read input from stdin
def input_board():
    print('Nhap du lieu tung dong theo mau: >>> 345003100')
    board = [None for _ in range(9)]
    r = 0
    while r < 9:
        row = input(f'Row {r+1}:')
        row = row.strip()
        if len(row) == 9:
            row = [int(c) for c in row]
        else:
            row = [int(c) for c in row.split()]
        if len(row) != 9:
            print(f'Loi du lieu. Nhap lai dong {r+1}')
            continue
        board[r] = row
        r += 1
    return board



def is_solved(board):
    return (0 not in board)


def check_number(r, c, num, board):
    r1, r2 = (0, 3) if r < 3 else (3, 6) if r < 6 else (6, 9)
    c1, c2 = (0, 3) if c < 3 else (3, 6) if c < 6 else (6, 9)
    return (num not in board[r]) and (num not in board[:, c]) and (num not in board[r1:r2, c1:c2])


def get_choices(r, c, board):
    choices = []
    for num in range(1, 10):
        if check_number(r, c, num, board):
            choices.append(num)

    return choices


def find_min_options(board):
    # tim vi tri co so lua chon nho nhat
    # tra ve vi tri (r, c) va nhung lua chon cho vi tri do: options
    # (0, 1, [1, 3, 4])..
    min_options = 9
    result = [None, None, []]

    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                options = get_choices(r, c, board)
                if len(options) == 1:
                    return r, c, options
                if len(options) < min_options:
                    min_options = len(options)
                    result = (r, c, options)
    return result


def solve(board):
    if is_solved(board):
        return True

    r, c, options = find_min_options(board)
    for num in options:
        board[r][c] = num
        if solve(board):
            return True
        board[r][c]= 0
    return False
        

if __name__ == '__main__':
    #board = np.array(input_board())
    board = np.array(to_array(data))
    print_board(board)
    if solve(board):
        print('Solved')
        print_board(board)
    else:
        print("Can't solve it!")
