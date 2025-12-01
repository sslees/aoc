import pytest
from a import solve


def test_example_1():
    assert (
        solve(
            """AAAA
BBCD
BBCC
EEEC"""
        )
        == 140
    )


def test_example_2():
    assert (
        solve(
            """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO"""
        )
        == 772
    )


def test_example_3():
    assert (
        solve(
            """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""
        )
        == 1930
    )


if __name__ == "__main__":
    pytest.main([__file__])
