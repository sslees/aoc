import importlib


def solve(year, day, data):
    a = importlib.import_module(f"{year}.{day:02}.a")
    b = importlib.import_module(f"{year}.{day:02}.b")
    return a.solve(data), b.solve(data)
