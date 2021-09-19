"""
in a n*n chess board there are obstacles and a queen and the queen can't move further than obstacles
given the position of the queen and (row,column) number of obstacles in form of tuple in array
i'm calculating the number of the squares the queen can walk
"""


def queensAttack(n, k, r_q, c_q, obstacles):
    # n sq board side lenght
    # k number of obstacles
    # r_q, c_q => (queen row, queen col)
    # obstacles = [[1,2], [5,5], ...] => loc obstacles

    # orthogonal
    squares_n = n - r_q
    squares_s = r_q - 1
    squares_e = n - c_q
    squares_w = c_q - 1

    # diaggonal
    squares_nw = min(squares_n, squares_w)
    squares_ne = min(squares_n, squares_e)
    squares_sw = min(squares_s, squares_w)
    squares_se = min(squares_s, squares_e)

    for row, col in obstacles:
        # share a row either east or west of obstacle
        if r_q == row:
            if c_q > col:
                if c_q - col - 1 < squares_w:
                    squares_w = c_q - col - 1
            if c_q < col:
                if col - c_q - 1 < squares_e:
                    squares_e = col - 1 - c_q

        # share a col either south or north of obstacle
        elif c_q == col:
            if r_q > row:
                if r_q - 1 - row < squares_s:
                    squares_s = r_q - 1 - row
            if r_q < row:
                if row - 1 - r_q < squares_n:
                    squares_n = row - 1 - r_q

        # north east
        elif row > r_q and col > c_q:
            if row - r_q == col - c_q:
                if row - r_q - 1 < squares_ne:
                    squares_ne = row - r_q - 1

        # north west
        elif row > r_q and col < c_q:
            if row - r_q == c_q - col:
                if row - r_q - 1 < squares_nw:
                    squares_nw = row - r_q - 1

        # south west
        elif row < r_q and col < c_q:
            if r_q - row == c_q - col:
                if r_q - row - 1 < squares_sw:
                    squares_sw = r_q - row - 1
        # south east
        elif row < r_q and col > c_q:
            if r_q - row == col - c_q:
                if r_q - row - 1 < squares_se:
                    squares_se = r_q - row - 1

    return sum([squares_n, squares_e, squares_w, squares_s, squares_nw, squares_sw, squares_ne, squares_se])
