import pytest
from b import solve


def test_example_1():
    assert solve(""">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>""") == 1_514_285_714_288


'''
def test_example_2():
    assert solve("""example2""") == None


def test_example_3():
    assert solve("""example3""") == None
'''

if __name__ == "__main__":
    test_example_1()
    # pytest.main([__file__])
