import pytest

from task_3_generator.main import range_

test_cases = [
    (1, 100),
    (5, 80, 3),
    (7, 40, 6),
    (500, 900, 15),
    (-6, 40, -6),
    (-45, 40, 6),
    (120, 200, -6),
    (5, -70, 6),
    (1, 4, 2),
    (5, 40, -6),
    (6, 6),
]


@pytest.mark.parametrize("params", test_cases)
def test_range_(params: tuple):
    assert tuple(range_(*params)) == tuple(range(*params))
