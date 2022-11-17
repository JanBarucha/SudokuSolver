import pytest
import sudokuChallenge


@pytest.fixture()
def sudoku_format():
    return '038 000 000 ' \
           '056 097 100' \
           '700 108 600'\
                        \
           '000 300 500 ' \
           '860 000 731 ' \
           '005 200 890 ' \
           '            ' \
           '607 903 000 ' \
           '083 005 009' \
           '000 010 300'

@pytest.fixture()
def horizontal_x_numbs():
    return [['038 000 000 '],
            ['056 097 100' ],
            ['700 108 600']]

@pytest.fixture()
def vertical_y_numbs():
    return [['007 080 064'],
            ['350 060 084'],
            ['860 005 730']]

@pytest.fixture()
def box_example():
    return [
        [0, 3, 8],
        [0, 5, 6],
        [7, 0, 0]
    ]

def test_check_what_number_can_be_in_box():
    box = [
        [0, 3, 8],
        [0, 5, 0],
        [7, 0, 0]
    ]
    result = sudokuChallenge.check_what_number_can_be_in_box(box)

    assert result == ({(0, 0): 0, (0, 1): 0, (1, 2): 0, (2, 2): 0, (2,1):0}, [1, 2, 4, 6, 9])


def test_horizont_splieter():
    result = sudokuChallenge.horizont_splieter('123456789')

    assert result == '1234567'


def test_box_checker(box_example,horizontal_x_numbs,vertical_y_numbs):
    converted_horizontal = list()
    converted_vertical = list()

    for i in horizontal_x_numbs:
        converted_horizontal.append(
            [int(x) for x in i[0].replace(' ', '')]
        )

    for i in vertical_y_numbs:
        converted_vertical.append(
            [int(x) for x in i[0].replace(' ', '')]
        )

    result = sudokuChallenge.box_checker(box_example,converted_horizontal,converted_vertical)
    assert [
        [1, 3, 8],
        [0, 5, 6],
        [7, 0, 4]
    ] == result


