from setuptools import find_packages, setup

with open("README.md") as f:
    readme = f.read()
setup(
    name="aoc",
    version="1.0",
    description="Advent of Code solutions by sslees",
    url="https://github.com/sslees/aoc",
    author="sslees",
    author_email="sam@sslees.com",
    long_description=readme,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: Games/Entertainment :: Puzzle Games",
    ],
    install_requires=[
        "advent-of-code-data >= 0.9.7",
    ],
    packages=find_packages(),
    entry_points={"adventofcode.user": ["sslees = utils.plugins:solve"]},
)
