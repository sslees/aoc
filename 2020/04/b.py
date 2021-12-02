#! /usr/bin/env python3

import re


def valid(p):
    byr = re.search(r"(?:^|\s+)byr:(\d{4})(?:$|\s+)", p)
    iyr = re.search(r"(?:^|\s+)iyr:(\d{4})(?:$|\s+)", p)
    eyr = re.search(r"(?:^|\s+)eyr:(\d{4})(?:$|\s+)", p)
    hgt = re.search(r"(?:^|\s+)hgt:(\d+)(cm|in)(?:$|\s+)", p)
    hcl = re.search(r"(?:^|\s+)hcl:(#[0-9a-f]{6})(?:$|\s+)", p)
    ecl = re.search(r"(?:^|\s+)ecl:(amb|blu|brn|gry|grn|hzl|oth)(?:$|\s+)", p)
    pid = re.search(r"(?:^|\s+)pid:(\d{9})(?:$|\s+)", p)
    valid = bool(byr and iyr and eyr and hgt and hcl and ecl and pid)
    if valid:
        valid &= 1920 <= int(byr.group(1)) <= 2002
        valid &= 2010 <= int(iyr.group(1)) <= 2020
        valid &= 2020 <= int(eyr.group(1)) <= 2030
        if hgt.group(2) == "cm":
            valid &= 150 <= int(hgt.group(1)) <= 193
        else:
            valid &= 59 <= int(hgt.group(1)) <= 76
    return valid


def solve(data: str):
    return len([p for p in data.split("\n\n") if valid(p)])


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
