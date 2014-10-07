import copy
import random


data = []
test_data = []

for line in open('data2', 'r').readlines():
    x = tuple([float(i) for i in line.split()])
    y = int(x[-1])
    x = x[:-1]
    data.append({'x': x, 'y': y})


for line in open('test_data2', 'r').readlines():
    x = tuple([float(i) for i in line.split()])
    y = int(x[-1])
    x = x[:-1]
    test_data.append({'x': x, 'y': y})


def get_product(w, d):
    x = d['x']
    return w[0] * x[0] + w[1] * x[1] + w[2] * x[2] + w[3] * x[3] + w[4]


def judge(w, d):
    product = get_product(w, d)
    if (product <= 0 and d['y'] > 0) or (product > 0 and d['y'] < 0):
        return False
    return True


sum_err = 0
for i in range(2000):
    print(i)
    w = [0.0, 0.0, 0.0, 0.0, 0.0]

    for _ in range(50):
        random.shuffle(data)
        for d in data:
            x = d['x']
            product = get_product(w, d)
            if product <= 0 and d['y'] > 0:
                w[0] += x[0]
                w[1] += x[1]
                w[2] += x[2]
                w[3] += x[3]
                w[4] += d['y']
                break
            elif product > 0 and d['y'] < 0:
                w[0] -= x[0]
                w[1] -= x[1]
                w[2] -= x[2]
                w[3] -= x[3]
                w[4] += d['y']
                break
        else:
            print('is it possible?')

    # verify
    err = 0
    for d in test_data:
        if not judge(w, d):
            err += 1
    sum_err += err

print(sum_err / 2000.0 / len(test_data))
