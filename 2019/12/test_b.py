import pytest
from b import solve


def test_example_1():
    assert (
        solve(
            """<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>"""
        )
        == 2_772
    )


def test_example_2():
    assert (
        solve(
            """<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>"""
        )
        == 4_686_774_924
    )


if __name__ == "__main__":
    pytest.main([__file__])
