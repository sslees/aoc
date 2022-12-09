import pytest
from b import solve


def test_example_1():
    assert (
        solve(
            """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN"""
        )
        == 4
    )


if __name__ == "__main__":
    pytest.main([__file__])
