#! /bin/env python3


def main():
    with open("input.txt") as f:
        d = f.read()
    ps = d.split("\n\n")
    count = 0
    for p in ps:
        if (
            "byr" in p
            and "iyr" in p
            and "eyr" in p
            and "hgt" in p
            and "hcl" in p
            and "ecl" in p
            and "pid" in p
            # p.contains("cid")
        ):
            count += 1
    print(count)


if __name__ == "__main__":
    main()
