sudoku = '004006079000000602056092300078061030509000406020540890007410920105000000840600100'


def horizont_splieter(sudoku):
    h_list = list()
    group_list_per_three_rows = list()

    for x in range(0, len(sudoku), 9):
        h_list.append([int(y) for y in sudoku[x: x + 9]])

    group_list_per_three_rows.append(h_list[0:3])
    group_list_per_three_rows.append(h_list[3:6])
    group_list_per_three_rows.append(h_list[6:9])
    return group_list_per_three_rows


def vertical_spliter(sudoku):
    v_list = list()
    gooup_list_per_three_columns = list()

    for y in range(9):
        v_list.append(
            sudoku[y] +
            sudoku[y + 9] +
            sudoku[y + 18] +
            sudoku[y + 27] +
            sudoku[y + 36] +
            sudoku[y + 45] +
            sudoku[y + 54] +
            sudoku[y + 63] +
            sudoku[y + 72]
        )

    for i, x in enumerate(v_list):
        v_list[i] = [int(z) for z in x]

    gooup_list_per_three_columns.append(v_list[0:3])
    gooup_list_per_three_columns.append(v_list[3:6])
    gooup_list_per_three_columns.append(v_list[6:9])
    return v_list


print(vertical_spliter(sudoku))


def box_creator(s):
    box_list_set = list()

    for b in range(0, 81, 27):
        box_list_set.append(
            [s[0 + b], s[1 + b], s[2 + b],
             s[9 + b], s[10 + b], s[11 + b],
             s[18 + b], s[19 + b], s[20 + b]])
        box_list_set.append(
            [s[3 + b], s[4 + b], s[5 + b], s[12 + b], s[13 + b], s[14 + b], s[21 + b], s[22 + b], s[23 + b]])
        box_list_set.append(
            [s[6 + b], s[7 + b], s[8 + b], s[15 + b], s[16 + b], s[17 + b], s[24 + b], s[25 + b], s[26 + b]])

    return box_list_set


"""
Example output from box_creator() : 
[['0', '0', '4', '0', '0', '0', '0', '5', '6'],
 ['0', '0', '6', '0', '0', '0', '0', '9', '2'], 
 ['0', '7', '9', '6', '0', '2', '3', '0', '0'], 
 ['0', '7', '8', '5', '0', '9', '0', '2', '0'], 
 ['0', '6', '1', '0', '0', '0', '5', '4', '0'], 
 ['0', '3', '0', '4', '0', '6', '8', '9', '0'], 
 ['0', '0', '7', '1', '0', '5', '8', '4', '0'], 
 ['4', '1', '0', '0', '0', '0', '6', '0', '0'], 
 ['9', '2', '0', '0', '0', '0', '1', '0', '0']] 

"""


def box_creator_to_matrix(box_list_set):
    converted_box = []
    for per_box in box_list_set:
        i = 0
        box_matrix_x = []

        for x in range(3):
            box_matrix_y = list()
            for y in range(3):
                box_matrix_y.append(per_box[i])
                i += 1
            box_matrix_x.append(box_matrix_y)

        converted_box.append(box_matrix_x)
    """
    Format converted box [box in sudoku][y column in box][x column in box]
    """
    return converted_box


"""
example of data structure vertical_numbs and horizontal_numbs
[
    [1,0,3,4,5,2,0,0,0],
    [1,0,3,4,5,2,0,0,0],
    [1,0,3,4,5,2,0,0,0]
]
"""


def check_what_number_can_be(x, y, vertical_numbs, horizontal_numbs):
    avaliable_numbs_x = [xyz for xyz in range(1, 10) if xyz not in vertical_numbs[x]]
    avaliable_numbs_y = [xyz for xyz in range(1, 10) if xyz not in horizontal_numbs[y]]

    return [avaliable_numbs_x, avaliable_numbs_y]


"""data structure of box 
[
    [1,4,0],
    [2,9,0],
    [0,0,0]
]
"""


def check_what_number_can_be_in_box(box):
    avaliable_box_numbers = set()
    location_empty_digits = dict()

    for i, num in enumerate(box):
        for k, num_k in enumerate(num):
            avaliable_box_numbers.add(box[i][k])
            if box[i][k] == 0:
                location_empty_digits[(i, k)] = 0

    avaliable_box_numbers = [x for x in range(1, 10) if x not in avaliable_box_numbers]

    return location_empty_digits, avaliable_box_numbers


def box_checker(box, horizontal_numbs, vertical_numbs):
    location_empty_digits = check_what_number_can_be_in_box(box)

    # Key : str, val : [tuple()]
    values_to_insert_in_box = dict()

    for i in location_empty_digits[1]:
        # k (x,y)
        values_to_insert_in_box[str(i)] = []
        for k in location_empty_digits[0]:

            if i not in vertical_numbs[k[1]] and i not in horizontal_numbs[k[0]]:
                values_to_insert_in_box[str(i)].append((k[0], k[1]))

    for key, value in values_to_insert_in_box.items():
        if (len(value) == 1):
            box[value[0][0]][value[0][1]] = int(key)

    return box


def sudoku_solver(sudoku):
    horizont_values = horizont_splieter(sudoku)
    vertical_values = vertical_spliter(sudoku)

    box_values = box_creator(sudoku)
    box_values_in_matrix = box_creator_to_matrix(box_values)

    # for box in box_values_in_matrix:

    pass
