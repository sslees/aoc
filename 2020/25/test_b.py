import pytest
from b import solve


def test_example_1():
    assert (
        solve(
            """5764801
17807724"""
        )
        == None
    )


if __name__ == "__main__":
    pytest.main([__file__])
