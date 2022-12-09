import pytest
from a import solve


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
K)L"""
        )
        == None
    )


if __name__ == "__main__":
    pytest.main([__file__])
