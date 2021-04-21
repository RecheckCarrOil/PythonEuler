import pytest

from problem_1 import *


@pytest.mark.parametrize("input_value, result",
                         [(0, False), (2, False), (3, True), (9, True), (31, False), (3000, True)])
def test_is_multiple_of_3(input_value, result):
    assert is_multiple_of_3(input_value) == result


@pytest.mark.parametrize("input_value, result",
                         [(0, False), (2, False), (5, True), (9, False), (54, False), (555, True)])
def test_is_multiple_of_5(input_value, result):
    assert is_multiple_of_5(input_value) == result


@pytest.mark.parametrize("start_num, end_num, result", [(1, 10, 23), (3, 4, 3), (1, 20, 78), (1, 1000, 233168)])
def test_sum_multiples_in_range(start_num, end_num, result):
    assert sum_of_multiples_of_3_or_5(start_num, end_num) == result
