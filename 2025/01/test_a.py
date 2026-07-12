import pytest
from a import solve


def test_example_1():
    assert (
        solve(
            """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""
        )
        # == 3
        == 6
    )


'''
def test_example_2():
    assert solve("""example2""") == None


def test_example_3():
    assert solve("""example3""") == None
'''

if __name__ == "__main__":
    pytest.main([__file__])
