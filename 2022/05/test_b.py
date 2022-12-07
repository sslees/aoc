import pytest
from b import solve


def test1():
    assert (
        solve(
            """    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""
        )
        == "MCD"
    )


if __name__ == "__main__":
    pytest.main([__file__])
