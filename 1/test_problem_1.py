import pytest

from problem_1 import *


@pytest.mark.parametrize("intInput, result", [(0, False), (2, False), (3, True), (9, True), (31, False)])
def test_is_multiple_of_3(intInput, result):
    assert is_multiple_of_3(intInput) == result
