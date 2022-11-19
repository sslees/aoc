import pytest
from a import solve


def test1():
    assert (
        solve(
            """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""
        )
        == 198
    )


if __name__ == "__main__":
    pytest.main([__file__])
