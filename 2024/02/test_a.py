import pytest
from a import solve


def test_example_1():
    assert (
        solve(
            """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
        )
        == 2
    )


if __name__ == "__main__":
    pytest.main([__file__])
