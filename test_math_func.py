import math_func
import pytest


# @pytest.mark.skip(reason="Skip for test")
@pytest.mark.parametrize('num1, num2, result',
                         [
                             (7, 3, 10),
                             ('Hello', ' World', 'Hello World'),
                             (10.5, 25.5, 36.0)
                         ])
def test_add(num1, num2, result):
    assert math_func.add(num1, num2) == result


@pytest.mark.parametrize('arg1, arg2, result',
                         [
                             (5, 5, 25),
                             (5, 2, 10),
                             (7, 0, 0)
                         ])
def test_product(arg1, arg2, result):
    assert math_func.product(arg1, arg2) == result
