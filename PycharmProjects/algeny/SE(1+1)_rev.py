import numpy as np
import random
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x, y = np.array([5., 5.])


def fitness(a,b):
    return np.sqrt(a**2+b**2)

steps=200
X=[]
Y=[]
sigma = 0.1
c_d = 0.82
c_t = 1.22
succeeded = 0
all = 0
print("t,   x, y,    sigma,    succeeded")
l = 50 # ile ostatnich mutacji wziac pod uwage
last_l_mut = []
apply_1_5 = True

for t in range(steps):
    offspring = [x + sigma * random.gauss(0,1), y + sigma * random.gauss(0,1)]
    if fitness(*offspring) < fitness(x, y):
        x, y = offspring
        last_l_mut.append(True)
    else:
        last_l_mut.append(False)

    if len(last_l_mut) > l:
        last_l_mut.remove(last_l_mut[0])
    X.append(x)
    Y.append(y)

    print t, np.round(x, 3),np.round(y, 3), sigma, succeeded

    if apply_1_5:
        succeeded = float(last_l_mut.count(True))
        all = float(len(last_l_mut))
        fi = succeeded / all # stosunek udanych mutacji do wszystkich
        if fi < 0.2:
            sigma = c_d * sigma
        elif fi > 0.2:
            sigma = c_t * sigma

plt.plot(range(steps), X, label='x')
plt.scatter(range(steps), X)
plt.xlabel('czas')
plt.ylabel('x / y')
plt.plot(range(steps), Y, 'g', label='y')
plt.scatter(range(steps), Y, color='g')
plt.legend()
plt.show(block=False)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(X, Y, fitness(np.array(X), np.array(Y)))
ax.plot(X, Y, fitness(np.array(X), np.array(Y)))
plt.xlabel('x')
plt.xlabel('y')
plt.ylabel('f dopasowania')
plt.show()




