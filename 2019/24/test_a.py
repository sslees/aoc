import pytest
from a import solve


def test_example_1():
    assert (
        solve(
            """....#
#..#.
#..##
..#..
#...."""
        )
        == 2_129_920
    )


if __name__ == "__main__":
    pytest.main([__file__])
