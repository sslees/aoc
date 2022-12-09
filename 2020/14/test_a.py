import pytest
from a import solve


def test_example_1():
    assert (
        solve(
            """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""
        )
        == None
    )


if __name__ == "__main__":
    pytest.main([__file__])
