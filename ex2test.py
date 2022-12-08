#! /usr/bin/env python3

from os import listdir


def main():
    for year in listdir():
        if year.startswith("20"):
            for day in listdir(year):
                p = year + "/" + day
                fs = [f for f in listdir(p) if f.endswith(".txt") and f != "input.txt"]
                if not all(f.endswith("b.txt") for f in fs):
                    test_a = open(p + "/test_a.py", "w")
                    test_a.write("import pytest\nfrom a import solve\n\n\n")
                else:
                    test_a = None
                if not all(f.endswith("a.txt") for f in fs):
                    test_b = open(p + "/test_b.py", "w")
                    test_b.write("import pytest\nfrom b import solve\n\n\n")
                else:
                    test_b = None
                ia = 1
                ib = 1
                for f in sorted(fs):
                    if not f.endswith("b.txt"):
                        with open(p + "/" + f) as e:
                            test_a.write(
                                f"def test_example_{ia}():\n    assert solve("
                                f'"""{e.read().strip()}""") == None\n\n\n'
                            )
                            ia += 1
                            print("rm", p + "/" + f)
                    if not f.endswith("a.txt"):
                        with open(p + "/" + f) as e:
                            test_b.write(
                                f"def test_example_{ib}():\n    assert solve("
                                f'"""{e.read().strip()}""") == None\n\n\n'
                            )
                            ib += 1
                            print("rm", p + "/" + f)
                end = 'if __name__ == "__main__":\n    pytest.main([__file__])\n'
                if test_a:
                    test_a.write(end)
                    test_a.close()
                if test_b:
                    test_b.write(end)
                    test_b.close()


if __name__ == "__main__":
    main()
