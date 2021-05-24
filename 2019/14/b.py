#! /usr/bin/env python3


def cost(recipes, extras, units, recipe):
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
    return sum(cost(recipes, extras, i[0] * reactions, i[1]) for i in inputs)


def main():
    recipes = {}
    with open("input.txt") as f:
        for l in f.readlines():
            inputs, output = l.split(" => ")
            increment, recipe = output.split()
            recipes[recipe] = (
                int(increment),
                [(int(i.split()[0]), i.split()[1]) for i in inputs.split(", ")],
            )
    cargo = 1_000_000_000_000
    rate = cost(recipes, {}, 1, "FUEL")
    fuel = (cargo - 1) // rate + 1
    ore = cost(recipes, {}, fuel, "FUEL")
    while ore < cargo:
        fuel += (cargo - ore - 1) // rate + 1
        ore = cost(recipes, {}, fuel, "FUEL")
    print(fuel - 1)


if __name__ == "__main__":
    main()
