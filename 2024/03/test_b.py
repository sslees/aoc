import pytest
from b import solve


def test_example_1():
    assert (
        solve(
            """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
        )
        == 48
    )


if __name__ == "__main__":
    pytest.main([__file__])
