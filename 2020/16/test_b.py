import pytest
from b import solve


def test_example_1():
    assert (
        solve(
            """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9"""
        )
        == None
    )


if __name__ == "__main__":
    pytest.main([__file__])
