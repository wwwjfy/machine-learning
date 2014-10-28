import random


def f(x):
    result = True if x >= 0 else False
    if random.random() >= .8:
        return not result
    return result


def stump():
    xs = [random.random() * 2 - 1 for _ in range(20)]
    xs.sort()
    data = [(x, f(x)) for x in xs]


    theta = None
    min_err = 20
    s = None
    # positive
    for i, t in enumerate(xs):
        err = 0
        for d in data:
            if (d[0] >= t and d[1] is False) or (d[0] <= t and d[1] is True):
                err += 1
        if err < min_err:
            min_err = err
            theta = (t + xs[i-1]) / 2
            s = 1
    #negative
    for i, t in enumerate(xs):
        err = 0
        for d in data:
            if (d[0] >= t and d[1] is True) or (d[0] <= t and d[1] is False):
                err += 1
        if err < min_err:
            min_err = err
            theta = (t + xs[i-1]) / 2
            s = -1

    return theta, min_err, s


c = 0.0
for _ in range(5000):
    t, err, s = stump()
    c += 0.5 + 0.3 * s * (abs(t) - 1)

# 17
#print(sum(float(stump()[1]) / 20 for _ in range(5000))) / 5000

# 18
print(c / 5000)
