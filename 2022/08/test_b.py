import pytest
from b import solve


def test_example_1():
    assert (
        solve(
            """30373
25512
65332
33549
35390"""
        )
        == 8
    )


if __name__ == "__main__":
    pytest.main([__file__])
