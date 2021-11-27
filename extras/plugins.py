import contextlib
import io
import runpy


def solve(year, day, data):
    with open("input.txt", "w") as f:
        f.write(data)

    a = io.StringIO()
    with contextlib.redirect_stdout(a):
        runpy.run_module(f"{year:04}.{day:02}.a", run_name="__main__")
    a = a.getvalue().strip()

    b = io.StringIO()
    with contextlib.redirect_stdout(b):
        runpy.run_module(f"{year:04}.{day:02}.b", run_name="__main__")
    b = b.getvalue().strip()

    return a, b
