from setuptools import find_packages, setup

with open("README.md") as f:
    readme = f.read()
setup(
    name="aoc",
    version="0.2",
    description="Advent of Code solutions by sslees",
    url="https://github.com/sslees/aoc",
    author="sslees",
    author_email="sam@sslees.com",
    long_description=readme,
    long_description_content_type="text/markdown",
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Topic :: Games/Entertainment :: Puzzle Games",
    ],
    install_requires=[
        "advent-of-code-data >= 1.2.3",
        "more-itertools",
        "networkx",
        "parse",
    ],
    extras_require={
        "dev": ["black", "line_profiler", "pylint", "rope"],
        "test": ["pytest"],
        "viz": ["jupyter", "matplotlib", "pygraphviz", "scipy"],
    },
    packages=find_packages(),
    entry_points={"adventofcode.user": ["sslees = extras.plugins:solve"]},
    scripts=["extras/mkaoc"],
)
