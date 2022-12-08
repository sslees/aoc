import pytest
from a import solve


def test_example_1():
    assert (
        solve(
            """30373
25512
65332
33549
35390"""
        )
        == 21
    )


if __name__ == "__main__":
    pytest.main([__file__])
