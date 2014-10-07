import random


data = []

for line in open('data1', 'r').readlines():
    x = tuple([float(i) for i in line.split()])
    y = int(x[-1])
    x = x[:-1]
    data.append({'x': x, 'y': y})


sum = 0
for _ in range(2000):
    random.shuffle(data)
    w = [0.0, 0.0, 0.0, 0.0, 0.0]
    i = -1

    while True:
        i += 1
        for d in data:
            x = d['x']
            product = w[0] * x[0] + w[1] * x[1] + w[2] * x[2] + w[3] * x[3] + w[4]
            if product <= 0 and d['y'] > 0:
                w[0] += 0.5 * x[0]
                w[1] += 0.5 * x[1]
                w[2] += 0.5 * x[2]
                w[3] += 0.5 * x[3]
                w[4] += 0.5 * d['y']
                break
            elif product > 0 and d['y'] < 0:
                w[0] -= 0.5 * x[0]
                w[1] -= 0.5 * x[1]
                w[2] -= 0.5 * x[2]
                w[3] -= 0.5 * x[3]
                w[4] += 0.5 * d['y']
                break
        else:
            #print(i, w)
            sum += i
            break

print(sum)
