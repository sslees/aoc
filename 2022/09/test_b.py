import pytest
from b import solve


def test_example_1():
    assert (
        solve(
            """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""
        )
        == 1
    )


def test_example_2():
    assert (
        solve(
            """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""
        )
        == 36
    )


if __name__ == "__main__":
    pytest.main([__file__])
