from collections import namedtuple


def sin(angle):
    assert not angle % 90
    angle %= 360
    return 1 if angle == 90 else -1 if angle == 270 else 0


def cos(angle):
    assert not angle % 90
    angle %= 360
    return 1 if not angle else -1 if angle == 180 else 0


class Point2D(namedtuple("Point2D", ("x", "y"))):
    __slots__ = ()

    @property
    def hypot(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def translate(self, dx, dy, dz):
        return Point2D(self.x + dx, self.y + dy)

    def rotate(self, rz):
        x2 = self.x * cos(rz) - self.y * sin(rz)
        y2 = self.x * sin(rz) + self.y * cos(rz)
        return Point2D(x2, y2)


class Point3D(namedtuple("Point3D", ("x", "y", "z"))):
    __slots__ = ()

    @property
    def hypot(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def translate(self, dx, dy, dz):
        return Point3D(self.x + dx, self.y + dy, self.z + dz)

    def rotate(self, rx, ry, rz):
        # rotate about X
        y2 = self.y * cos(rx) - self.z * sin(rx)
        z2 = self.y * sin(rx) + self.z * cos(rx)
        # rotate about Y
        x2 = self.x * cos(ry) + z2 * sin(ry)
        z3 = z2 * cos(ry) - self.x * sin(ry)
        # rotate about Z
        x3 = x2 * cos(rz) - y2 * sin(rz)
        y3 = x2 * sin(rz) + y2 * cos(rz)
        return Point3D(x3, y3, z3)
