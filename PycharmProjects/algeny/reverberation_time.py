import numpy as np
import matplotlib.pyplot as plt


x_init = 2
y_init = 2
angle = 3.*np.pi/2.
wall1_x = 0
attenuation_factor_wall1_x = 0.1 #drewno
wall2_x = 4
attenuation_factor_wall2_x = 0.02 #cegla
wall1_y = 0
attenuation_factor_wall1_y = 0.06 #malowany beton
wall2_y = 4
attenuation_factor_wall2_y = 0.31 #beton porowaty
v_soud = 340. #m/s
dt = 0.0001 #s
initial_intensity = 1e-5 #W/m^2
threshold_of_hearing = 1e-12 #W/m^2


def reverberation_time(x, y, angle, N):
    times = []
    for i in range(N):
        propagation_angle = np.random.normal(angle, np.pi/10) #random.uniform(angle-np.pi/6., angle+np.pi/6.)
        x = x_init
        y = y_init
        v_x = v_soud * np.cos(propagation_angle)
        v_y = v_soud * np.sin(propagation_angle)
        t = 0
        I = initial_intensity
        while(I >= threshold_of_hearing):
            x += v_x * dt
            y += v_y * dt
            if x <= wall1_x:
                v_x *= -1
                I *= (1-attenuation_factor_wall1_x)
            elif x >= wall2_x:
                v_x *= -1
                I *= (1-attenuation_factor_wall2_x)
            elif y <= wall1_y:
                v_y *= -1
                I *= (1-attenuation_factor_wall1_y)
            elif y >= wall2_y:
                v_y *= -1
                I *= (1-attenuation_factor_wall2_y)
            t += dt
            I *= 0.99

        times.append(t)

    return np.array(times).mean()




if __name__ == "__main__":
    angles = np.arange(0, 2*np.pi, 0.05)
    for a in angles:
        plt.plot(a, reverberation_time(x_init, y_init, a, 500), 'o', color='g')
        print a
    plt.xlabel("Angle [rad]")
    plt.ylabel("Average reverberation time [s]")

    # for a in range(1,700):
    #     plt.plot(a, reverberation_time(x_init, y_init, angle, a), 'o', color='g')
    #     print a
    # plt.xlabel("Number of iterations")
    # plt.ylabel("Average reverberation time")

    plt.show()