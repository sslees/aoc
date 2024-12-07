import pytest
from a import solve


def test_example_1():
    assert (
        solve(
            """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
        )
        == 161
    )


if __name__ == "__main__":
    pytest.main([__file__])
