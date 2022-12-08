import pytest
from a import solve


def test_example_1():
    assert solve("""nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6""") == None


if __name__ == "__main__":
    pytest.main([__file__])
