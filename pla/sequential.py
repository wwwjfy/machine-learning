data = []

for line in open('data1', 'r').readlines():
    x = tuple([float(i) for i in line.split()])
    y = int(x[-1])
    x = x[:-1]
    data.append({'x': x, 'y': y})


w = [0.0, 0.0, 0.0, 0.0, 0.0]
i = -1

while True:
    i += 1
    for d in data:
        x = d['x']
        product = w[0] * x[0] + w[1] * x[1] + w[2] * x[2] + w[3] * x[3] + w[4]
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
        print(w)
        print(i, 'times')
        break
