import pytest
from b import solve


def test1():
    assert (
        solve(
            """forward 5
down 5
forward 8
up 3
down 8
forward 2
"""
        )
        == 900
    )


if __name__ == "__main__":
    pytest.main([__file__])
