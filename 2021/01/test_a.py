from a import solve
import pytest


def test1():
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
        == 7
    )


if __name__ == "__main__":
    pytest.main([__file__])
