import numpy as np
import math as m
import matplotlib.pyplot as plt

def draw(x, alfa):
    y = 3.9

    plt.plot([0,4], [0,0], color='k')
    plt.plot([0,4], [4,4], color='k')
    plt.plot([0,0], [0,4], color='k')
    plt.plot([4,4], [0,4], color='k')
    plt.xlim(-0.5,4.5)
    plt.ylim(-0.5,4.5)
    a = np.arange(x-0.08, x, 0.001)
    b = np.tan(alfa)*a + y - np.tan(alfa)*x
    print a, b
    plt.plot(a,b,'o', color = 'g')
    plt.show()

if __name__ == "__main__":
    draw(2.8766, 4.121)
