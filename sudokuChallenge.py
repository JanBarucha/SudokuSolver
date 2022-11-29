sudoku = '004006079000000602056092300078061030509000406020540890007410920105000000840600100'


def horizontal_split(sudoku_input_as_test):
    h_list = list()
    group_list_per_three_rows = list()

    for x in range(0, len(sudoku_input_as_test), 9):
        h_list.append([int(y) for y in sudoku_input_as_test[x: x + 9]])

    group_list_per_three_rows.append(h_list[0:3])
    group_list_per_three_rows.append(h_list[3:6])
    group_list_per_three_rows.append(h_list[6:9])
    return group_list_per_three_rows


def vertical_split(sudoku_input_as_test):
    v_list = list()
    group_list_per_three_columns = list()

    for y in range(9):
        v_list.append(
            sudoku_input_as_test[y] +
            sudoku_input_as_test[y + 9] +
            sudoku_input_as_test[y + 18] +
            sudoku_input_as_test[y + 27] +
            sudoku_input_as_test[y + 36] +
            sudoku_input_as_test[y + 45] +
            sudoku_input_as_test[y + 54] +
            sudoku_input_as_test[y + 63] +
            sudoku_input_as_test[y + 72]
        )

    for i, x in enumerate(v_list):
        v_list[i] = [int(z) for z in x]

    group_list_per_three_columns.append(v_list[0:3])
    group_list_per_three_columns.append(v_list[3:6])
    group_list_per_three_columns.append(v_list[6:9])
    return group_list_per_three_columns


"""
box_creator creates 3x3 squares as list. As input it is sudoku string input. 
"""


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
    available_box_numbers = set()
    location_empty_digits = list()

    for i, num in enumerate(box):
        for k, num_k in enumerate(num):
            available_box_numbers.add(int(box[i][k]))
            if int(box[i][k]) == 0:
                location_empty_digits.append((i, k))

    available_box_numbers = [x for x in range(1, 10) if x not in available_box_numbers]

    return location_empty_digits, available_box_numbers


def box_checker(box, horizontal_numbs, vertical_numbs, flag, location_box):
    location_empty_digits = check_what_number_can_be_in_box(box)

    # Key : str, val : [tuple()]
    values_to_insert_in_box = dict()

    for i in location_empty_digits[1]:
        # k (x,y)
        i = str(i)
        values_to_insert_in_box[i] = []
        for k in location_empty_digits[0]:

            if i not in vertical_numbs[k[1]] and i not in horizontal_numbs[k[0]]:
                values_to_insert_in_box[i].append((k[1], k[0]))

    for key, value in values_to_insert_in_box.items():

        if len(value) == 1:
            flag = True
            box[value[0][1]][value[0][0]] = key

            update_horizontal_vertical(horizontal_numbs, vertical_numbs, value[0][0], value[0][1], key,
                                       location_box)

    return box, flag


def update_horizontal_vertical(horizontal, vertical, x, y, value, location_box):
    if location_box == 0:
        horizontal[y][x] = value
        vertical[x][y] = value
    elif location_box == 1:
        horizontal[y][x + 3] = value
        vertical[x][y] = value
    elif location_box == 2:
        horizontal[y][x + 6] = value
        vertical[x][y] = value
    elif location_box == 3:
        horizontal[y][x] = value
        vertical[x][y + 3] = value
    elif location_box == 4:
        horizontal[y][x + 3] = value
        vertical[x][y + 3] = value
    elif location_box == 5:
        horizontal[y][x + 6] = value
        vertical[x][y + 3] = value
    elif location_box == 6:
        horizontal[y][x] = value
        vertical[x][y + 6] = value
    elif location_box == 7:
        horizontal[y][x + 3] = value
        vertical[x][y + 6] = value
    elif location_box == 8:
        horizontal[y][x + 6] = value
        vertical[x][y + 6] = value


def sudoku_solver(sudoku):
    horizont_values = horizontal_split(sudoku)
    vertical_values = vertical_split(sudoku)

    for i, k in enumerate(horizont_values):
        for z, w in enumerate(k):
            horizont_values[i][z] = [str(elem) for elem in w]

    for i, k in enumerate(vertical_values):
        for z, w in enumerate(k):
            vertical_values[i][z] = [str(elem) for elem in w]

    box_values = box_creator(sudoku)
    box_values_in_matrix = box_creator_to_matrix(box_values)
    print(box_values_in_matrix)

    flag = True
    while flag:

        flag = False

        for i, box in enumerate(box_values_in_matrix):

            if i < 3:
                flag = box_checker(box, horizont_values[0], vertical_values[i], flag, i)[1]

            elif i < 6:
                flag = box_checker(box, horizont_values[1], vertical_values[i % 3], flag, i)[1]

            elif i < 9:
                flag = box_checker(box, horizont_values[2], vertical_values[i % 6], flag, i)[1]

    return box_values_in_matrix


print(sudoku_solver(sudoku))
