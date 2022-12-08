import pytest
from a import solve


def test_example_1():
    assert (
        solve(
            """A Y
B X
C Z"""
        )
        == 15
    )


if __name__ == "__main__":
    pytest.main([__file__])
