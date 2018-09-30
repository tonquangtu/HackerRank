# Sudoku filler
# Application to fill sudoku board

# Input: a sudoku board hasn't filled
# Output: a sudoku baord filled


from datetime import datetime


def set_bit_map(bit_map, i, j, number):
    sub_board_pos = int(i / 3) * 3 + int(j / 3)
    bit_map[0][number] |= 1 << i
    bit_map[1][number] |= 1 << j
    bit_map[2][number] |= 1 << sub_board_pos


def clear_bit_map(bit_map, i, j, number):
    sub_board_pos = int(i / 3) * 3 + int(j / 3)
    bit_map[0][number] ^= 1 << i
    bit_map[1][number] ^= 1 << j
    bit_map[2][number] ^= 1 << sub_board_pos


def sudoku_filler(s_board, bit_map, i, j):
    while s_board[i][j] > 0:
        j += 1
        if j == 9:
            j = 0
            i += 1
            if i == 9:
                return True

    for k in range(1, 10):
        sub_board_pos = int(i/3) * 3 + int(j/3)
        k_seted = (bit_map[0][k] & 1 << i) | (bit_map[1][k] & 1 << j) | (bit_map[2][k] & 1 << sub_board_pos)

        if not k_seted:
            s_board[i][j] = k
            set_bit_map(bit_map, i, j, k)
            if sudoku_filler(s_board, bit_map, i, j):
                return True
            s_board[i][j] = 0
            clear_bit_map(bit_map, i, j, k)

    return False


# It for fill sudoku game
# Version 1: Using bit map for get set of suitable candidate for one empty
# I using a multi array size 3*9 for marked the appear of each number in each row, each column and each sub matrix
def solve_sudoku(s_board):
    bit_map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for i in range(3)]

    for i in range(9):
        for j in range(9):
            if s_board[i][j] > 0:
                set_bit_map(bit_map, i, j, s_board[i][j])

    return sudoku_filler(s_board, bit_map, 0, 0)


def show_sudoku_board(s_board):
    for i in range(9):
        for j in range(9):
            print(s_board[i][j], end=' ')
        print('')


# This function for check sudoku is corrected ?
def check_correct_sudoku(s_board):
    for i in range(9):
        mark_row = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        mark_cell = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        mark_sub = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        for j in range(9):
            if mark_row[s_board[i][j]] or mark_cell[s_board[j][i]]:
                return False

            sb_r = int(j / 3) + int(i / 3) * 3
            sb_c = int(j % 3) + int(i % 3) * 3
            if mark_sub[s_board[sb_r][sb_c]]:
                return False

            mark_row[s_board[i][j]] = 1
            mark_cell[s_board[j][i]] = 1
            mark_sub[s_board[sb_r][sb_c]] = 1

    return True


def test():
    s_board = [[0, 0, 0, 0, 6, 8, 1, 0, 0],
               [0, 6, 2, 0, 0, 0, 0, 0, 3],
               [0, 9, 0, 7, 0, 4, 8, 0, 0],
               [6, 0, 8, 0, 0, 0, 7, 0, 5],
               [0, 5, 0, 6, 0, 0, 0, 4, 0],
               [0, 0, 4, 1, 8, 0, 0, 9, 0],
               [2, 0, 0, 4, 0, 9, 0, 0, 7],
               [5, 1, 0, 0, 7, 6, 0, 0, 0],
               [7, 0, 0, 0, 0, 0, 9, 6, 0]]

    print('This is previous sudoku board, before run algorithm for fill')
    show_sudoku_board(s_board)
    print('-----------------------------------------------------')
    start = datetime.now()
    filled = solve_sudoku(s_board)
    end = datetime.now()
    # Check algorithm right or wrong
    is_correct = check_correct_sudoku(s_board)
    print('This result is right: ', is_correct)
    print('This board can fill: ', filled)
    show_sudoku_board(s_board)
    print('Time run algorithm: ', (end - start).microseconds)


test()
