import pytest
from a import solve


def test_example_1():
    assert solve("""109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99""") == None


def test_example_2():
    assert solve("""1102,34915192,34915192,7,4,7,99,0""") == None


def test_example_3():
    assert solve("""104,1125899906842624,99""") == None


if __name__ == "__main__":
    pytest.main([__file__])
