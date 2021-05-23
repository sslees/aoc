from itertools import product


class Controller:
    def __init__(self, setpoint, kp=0.05, ki=0.0001, kd=1.5):
        self._total = 0
        self._last = 0
        self.setpoint = setpoint
        self.kp = kp
        self.ki = ki
        self.kd = kd

    def control(self, value):
        error = self.setpoint - value
        self._total += error
        p = error * self.kp
        i = self._total * self.ki
        d = (error - self._last) * self.kd
        self._last = error
        return p + i + d


def tune(system, setpoint, start, kpmin=1, kpmax=1, kimin=1, kimax=1, kdmin=0, kdmax=0):
    DIVISIONS = 32
    STABILITY = 8
    TOLERANCE = 0.001
    LIMIT = 1_000

    kps = (
        [kpmin + (kpmax - kpmin) / DIVISIONS * i for i in range(DIVISIONS + 1)]
        if kpmin != kpmax
        else [kpmin]
    )
    kis = (
        [kimin + (kimax - kimin) / DIVISIONS * i for i in range(DIVISIONS + 1)]
        if kimin != kimax
        else [kimin]
    )
    kds = (
        [kdmin + (kdmax - kdmin) / DIVISIONS * i for i in range(DIVISIONS + 1)]
        if kdmin != kdmax
        else [kdmin]
    )
    results = {}
    for ks in product(kps, kis, kds):
        controller = Controller(setpoint, *ks)
        value = start
        errs = [setpoint] * STABILITY
        steps = 0
        while sum((abs(e) for e in errs)) / STABILITY > TOLERANCE and steps < LIMIT:
            control = controller.control(value)
            value = system(value, control)
            errs = errs[1:] + [setpoint - value]
            steps += 1
        results[ks] = steps
    return min(results, key=results.get)


def main():
    system = lambda value, control: value + control * 1.1 + 2.2  # simulates bias
    setpoint = setpoint = float(input("setpoint: "))
    start = 0
    ks = tune(system, setpoint, start, 0.02, 1.32, 0, 1.85, -0.50, 0.29)

    controller = Controller(setpoint, *ks)
    value = start
    while abs(setpoint - value) > 0.001:
        control = controller.control(value)
        value = system(value, control)
        print("value: {} -> control: {}".format(value, control))


if __name__ == "__main__":
    main()
