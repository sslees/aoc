import pytest
from b import solve


def test_example_1():
    assert (
        solve(
            """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
        )
        == 81
    )


if __name__ == "__main__":
    pytest.main([__file__])
