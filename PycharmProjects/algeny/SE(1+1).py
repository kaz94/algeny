import numpy as np
import random
from matplotlib import pyplot as plt

x = 0.


def fitness(a):
    return np.abs(np.sin(a))

steps=1000
X=[]
sigma = 0.1
c_d = 0.82
c_t = 1.22
succeeded = 0
all = 0
print("t,   x,    sigma,    succeeded")
l = 50 # ile ostatnich mutacji wziac pod uwage
last_l_mut = []
apply_1_5 = True

for t in range(steps):
    offspring = x + sigma * random.gauss(0,1)
    if fitness(offspring) > fitness(x):
        x = offspring
        last_l_mut.append(True)
    else:
        last_l_mut.append(False)

    if len(last_l_mut) > l:
        last_l_mut.remove(last_l_mut[0])
    X.append(x)

    print t, np.round(x, 3), sigma, succeeded

    if apply_1_5:
        succeeded = float(last_l_mut.count(True))
        all = float(len(last_l_mut))
        fi = succeeded / all # stosunek udanych mutacji do wszystkich
        if fi < 0.2:
            sigma = c_d * sigma
        elif fi > 0.2:
            sigma = c_t * sigma

plt.plot(range(steps), X)
plt.scatter(range(steps), X)
plt.xlabel('czas')
plt.ylabel('x')
plt.show()
plt.scatter(X, fitness(X))
plt.plot(X, fitness(X))
plt.xlabel('x')
plt.ylabel('f dopasowania')
plt.show()



