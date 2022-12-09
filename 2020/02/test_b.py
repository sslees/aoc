import pytest
from b import solve


def test_example_1():
    assert (
        solve(
            """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""
        )
        == None
    )


if __name__ == "__main__":
    pytest.main([__file__])
