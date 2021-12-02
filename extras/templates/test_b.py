from b import solve
import pytest


def test1():
    assert solve("""example1""") == None


# def test2():
#     assert solve("""example2""") == None


# def test3():
#     assert solve("""example3""") == None


if __name__ == "__main__":
    pytest.main([__file__])
