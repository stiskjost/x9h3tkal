import calculator
import math as math
import pytest


@pytest.mark.parametrize(
    "arg, expected", [[(1,2), 3], [(-1,1), 0], [(3, -5), -2]]
)
def test_add_exercise_1(arg, expected):
    calculated = calculator.add(arg[0], arg[1])
    assert calculated == expected

@pytest.mark.parametrize(
    "arg, expected", [[(0.1, 0.2), 0.3], [(-0.5, -1.5), -2.0], [(0.3, -0.5), -0.2]]
)
def test_add2_exercise_2(arg, expected):
    tol = 10**(-8)
    calculated = calculator.add(arg[0], arg[1])
    assert abs(expected-calculated) < tol

@pytest.mark.parametrize(
    "arg, expected", [[("Hello ", "world"), "Hello world"], [("gH1sx7", "Rt12fk9"), "gH1sx7Rt12fk9"], [("Leonhard ", "Euler"), "Leonhard Euler"]]
)
def test_add_string_exercise_3(arg, expected):
    calculated = calculator.add(arg[0], arg[1])
    assert expected == calculated

@pytest.mark.parametrize(
    "arg, expected", [(5, math.factorial(5)), (7, math.factorial(7)), (4, math.factorial(4))]
)
def test_factorial_exercise_4(arg, expected):
    calculated = calculator.factorial(arg)
    assert expected == calculated

@pytest.mark.parametrize(
    "arg, expected", [(5, math.sin(5)), (math.pi, math.sin(math.pi)), (0, math.sin(0))]
)
def test_sin_exercise_4(arg, expected):
    tol = 10**(-8)
    calculated = calculator.sin(arg, 50)
    assert abs(expected-calculated) < tol

@pytest.mark.parametrize(
    "arg, expected", [[(615, 999), 0.615615615615], [(1, 2), 0.5], [(6, -8), -0.75]]
)
def test_divide_exercise_4(arg, expected):
    tol = 10**(-8)
    calculated = calculator.divide(arg[0], arg[1])
    assert abs(expected-calculated) < tol

@pytest.mark.parametrize(
    "arg, expected", [(6.1353256, 7), (3.14159265, 4), (-7.2, -7)]
)
def test_ceil_exercise_4(arg, expected):
    calculated = calculator.ceil(arg)
    assert expected == calculated

@pytest.mark.parametrize(
    "arg, expected", [(99999999999, 9), (17, 8), (86432, 5) ]
)
def test_digitalRoot_exercise_4(arg, expected):
    calculated = calculator.digitalRoot(arg)
    assert expected == calculated

@pytest.mark.parametrize(
    "arg", [(1, "Hello"), ("One", 2), ("Number", 9)]
)
def test_add_string_with_float_raises_TypeError_exercise_5(arg):
    with pytest.raises(TypeError):
        calculator.add(arg[0], arg[1])

@pytest.mark.parametrize(
    "arg", [1, 5, 0]
)
def test_divide_by_zero_raises_ZeroDivisionError_exercise_5(arg):
    with pytest.raises(ZeroDivisionError):
        calculator.divide(arg, 0)

#
