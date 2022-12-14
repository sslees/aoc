import pytest
from a import solve


def test_example_1():
    assert (
        solve(
            """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""
        )
        == 24
    )


if __name__ == "__main__":
    pytest.main([__file__])
