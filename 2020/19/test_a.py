import pytest
from a import solve


def test_example_1():
    assert (
        solve(
            """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb"""
        )
        == None
    )


if __name__ == "__main__":
    pytest.main([__file__])
