#! /usr/bin/env python3


def ore(recipes, extras, units, recipe):
    if recipe == "ORE":

        return units
    if recipe in extras:
        extra = min(units, extras[recipe])
        units -= extra
        extras[recipe] -= extra
    else:
        extras[recipe] = 0
    increment, inputs = recipes[recipe]
    reactions = (units - 1) // increment + 1
    extras[recipe] += reactions * increment - units

    return sum(ore(recipes, extras, i[0] * reactions, i[1]) for i in inputs)


def solve(data: str):
    recipes = {}
    for l in data.splitlines():
        inputs, output = l.split(" => ")
        increment, recipe = output.split()
        recipes[recipe] = (
            int(increment),
            [(int(i.split()[0]), i.split()[1]) for i in inputs.split(", ")],
        )
    return ore(recipes, {}, 1, "FUEL")


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
