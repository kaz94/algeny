import numpy as np
import random
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from reverberation_time import reverberation_time

fitness = reverberation_time
#angle = np.array([6.])
angle = np.pi
x = 2.
y = 2.


steps=100
angles = []
X=[]
Y=[]
sigma = 2
sigma_x = 2
sigma_y = 2
c_d = 0.82
c_t = 1.22
succeeded = 0
all = 0

print("t, angle, x, y, sigma")
l = 10 # ile ostatnich mutacji wziac pod uwage
last_l_mut = []
last_l_mut_x = []
last_l_mut_y = []
apply_1_5 = True
fits = []
initial_intensity = 1e-5
threshold_of_hearing = 1e-12
old = fitness(angle, x, y)
for t in range(steps):
    offspring = angle + sigma * random.gauss(0, 1)
    '''x + sigma * random.gauss(0,1),
                 y + sigma * random.gauss(0,1)]'''
    old = fitness(angle, x, y)
    fits.append(old)
    new = fitness(offspring, x, y)
    if new < old:
        angle = offspring
        last_l_mut.append(True)
        old = new
    else:
        last_l_mut.append(False)


    offspring_x = x + sigma_x * random.gauss(0, 1)
    new = fitness(angle, offspring_x, y)
    if new < old:
        x = offspring_x
        last_l_mut_x.append(True)
        old = new
    else:
        last_l_mut_x.append(False)

    offspring_y = y + sigma_y * random.gauss(0, 1)

    new = fitness(angle, x, offspring_y)
    if new < old:
        y = offspring_y
        last_l_mut_y.append(True)
        old = new
    else:
        last_l_mut_y.append(False)


    if len(last_l_mut) > l:
        last_l_mut.remove(last_l_mut[0])
    if len(last_l_mut_x) > l:
        last_l_mut_x.remove(last_l_mut_x[0])
    if len(last_l_mut_y) > l:
        last_l_mut_y.remove(last_l_mut_y[0])
    angles.append(angle)
    X.append(x)
    Y.append(y)

    print t, np.round(angle, 3), x, y, sigma, sigma_x, sigma_y

    if apply_1_5:
        succeeded = float(last_l_mut.count(True))
        all = float(len(last_l_mut))
        fi = succeeded / all # stosunek udanych mutacji do wszystkich
        if fi < 0.2:
            sigma *= c_d
        elif fi > 0.2 and sigma < 3.:
            sigma *= c_t

        succeeded = float(last_l_mut_x.count(True))
        all = float(len(last_l_mut_x))
        fi = succeeded / all # stosunek udanych mutacji do wszystkich
        if fi < 0.2:
            sigma_x *= c_d
        elif fi > 0.2 and sigma_x < 2.:
            sigma_x *= c_t

        succeeded = float(last_l_mut_y.count(True))
        all = float(len(last_l_mut_y))
        print all
        fi = succeeded / all # stosunek udanych mutacji do wszystkich
        if fi < 0.2:
            sigma_y *= c_d
        elif fi > 0.2 and sigma_y < 2.:
            sigma_y *= c_t

plt.plot(range(steps), angles)
plt.scatter(range(steps), angles)
plt.xlabel('czas')
plt.ylabel('kat')
plt.show()

plt.plot(range(steps), X, 'o-', color='r')
plt.xlabel('t')
plt.ylabel('x')
plt.show()

plt.plot(range(steps), Y, 'o-', color='r')
plt.xlabel('t')
plt.ylabel('y')
plt.show()

plt.plot(range(steps), fits, 'o-', color='r')
plt.xlabel('kat')
plt.ylabel('f dopasowania')
plt.show()




