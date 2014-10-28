import random


def stump(data):
    data.sort()
    xs = [d[0] for d in data]
    theta = None
    min_err = len(data)
    s = None
    # positive
    for i, t in enumerate(xs):
        err = 0
        for d in data:
            if (d[0] >= t and d[1] < 0) or (d[0] <= t and d[1] > 0):
                err += 1
        if err < min_err:
            min_err = err
            if i == 0:
                theta = t - .5
            else:
                theta = (t + xs[i-1]) / 2
            s = 1
    #negative
    for i, t in enumerate(xs):
        err = 0
        for d in data:
            if (d[0] >= t and d[1] > 0) or (d[0] <= t and d[1] < 0):
                err += 1
        if err < min_err:
            min_err = err
            theta = (t + xs[i-1]) / 2
            s = -1

    return theta, float(min_err) / len(data), s


theta = []
train_data = [line.split() for line in open('train_data', 'r').readlines()]
e_in_min = len(train_data)
index = None
for i in range(len(train_data[0]) - 1):
    t, err, s = stump([(float(d[i]), int(d[-1])) for d in train_data])
    theta.append((t, s))
    if err < e_in_min:
        e_in_min = err
        index = i

print("Ein:", e_in_min)

test_data = [line.split() for line in open('test_data', 'r').readlines()]
e_out = 0
s = theta[index][1]
for d in test_data:
    d[index] = float(d[index])
    d[-1] = int(d[-1])
    if d[index] >= theta[index][0]:
        if s > 0 and d[-1] > 0:
            continue
        if s < 0 and d[-1] < 0:
            continue
    if d[index] < theta[index][0]:
        if s < 0 and d[-1] > 0:
            continue
        if s > 0 and d[-1] < 0:
            continue
    print(d[index], theta[index])
    e_out += 1

print(float(e_out) / len(test_data))
