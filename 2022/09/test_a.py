import pytest
from a import solve


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
        == 13
    )


if __name__ == "__main__":
    pytest.main([__file__])
