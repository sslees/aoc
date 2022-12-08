import pytest
from b import solve


def test_example_1():
    assert (
        solve(
            """199
200
208
210
200
207
240
269
260
263
"""
        )
        == 5
    )


if __name__ == "__main__":
    pytest.main([__file__])
