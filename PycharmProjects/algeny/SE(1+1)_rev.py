import numpy as np
import random
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from reverberation_time import reverberation_time

fitness = reverberation_time
angle = np.array([0.])
#angle, x, y = np.array([0., 0., 0.])


steps=100
angles = []
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
fits = []
initial_intensity = 1e-5
threshold_of_hearing = 1e-12

for t in range(steps):
    offspring = angle + sigma * random.gauss(0, 1)
    '''x + sigma * random.gauss(0,1),
                 y + sigma * random.gauss(0,1)]'''
    old = fitness(angle)
    new = fitness(*offspring)
    if new < old:
        angle = offspring
        last_l_mut.append(True)
        fits.append(new)
    else:
        last_l_mut.append(False)
        fits.append(old)

    if len(last_l_mut) > l:
        last_l_mut.remove(last_l_mut[0])
    angles.append(angle)
    #X.append(x)
    #Y.append(y)

    print t, np.round(angle, 3), sigma, succeeded

    if apply_1_5:
        succeeded = float(last_l_mut.count(True))
        all = float(len(last_l_mut))
        fi = succeeded / all # stosunek udanych mutacji do wszystkich
        if fi < 0.2:
            sigma = c_d * sigma
        elif fi > 0.2:
            sigma = c_t * sigma

plt.plot(range(steps), angles)
plt.scatter(range(steps), angles)
plt.xlabel('czas')
plt.ylabel('kat')
plt.show()

plt.plot(angles, fits, color='r')
plt.scatter(angles, fits, color='r')
plt.xlabel('kat')
plt.ylabel('f dopasowania')
plt.show()




