def tf3d(x, y, z, dx, dy, dz, rx, ry, rz):
    # rotate about X
    y2 = y * cos(rx) - z * sin(rx)
    z2 = y * sin(rx) + z * cos(rx)
    # rotate about Y
    x2 = x * cos(ry) + z2 * sin(ry)
    z3 = z2 * cos(ry) - x * sin(ry)
    # rotate about Z
    x3 = x2 * cos(rz) - y2 * sin(rz)
    y3 = x2 * sin(rz) + y2 * cos(rz)
    # translate
    return x3 + dx, y3 + dy, z3 + dz


def tf2d(x, y, dx, dy, r):
    return tf3d(x, y, 0, dx, dy, 0, 0, 0, r)


def cos(angle):
    assert angle % 90 == 0
    angle = ((angle % 360 + 360) % 360)
    if angle == 0:
        return 1
    if angle == 180:
        return -1
    return 0


def sin(angle):
    assert angle % 90 == 0
    angle = ((angle % 360 + 360) % 360)
    if angle == 90:
        return 1
    if angle == 270:
        return -1
    return 0


def pid(p, i, d, total, last, error):
    delta = error - last
    total += error
    last = error
    return total, last,\
        (error / p if p else 0) +\
        (total / i if i else 0) +\
        (delta / d if d else 0)


def pidloop():
    p, i, d = 20, 10_000, 2/3
    total = last = 0
    signal = 100
    while True:
        error = signal - input()
        total, last, control = pid(p, i, d, total, last, error)
        print(signal + control)
