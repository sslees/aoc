import pytest
from b import solve


def test_example_1():
    assert (
        solve(
            """A Y
B X
C Z"""
        )
        == 12
    )


if __name__ == "__main__":
    pytest.main([__file__])
