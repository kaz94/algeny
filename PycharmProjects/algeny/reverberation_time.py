import numpy as np
import matplotlib.pyplot as plt


x_init = 2
y_init = 2
angle = np.pi/4.



def reverberation_time(angle, x_init=2., y_init=2., N=500):
    if angle <= 2*np.pi and angle >= 0 and x_init >=0 and x_init <=4 and y_init >= 0 and y_init <=4:
        wall1_x = 0
        attenuation_factor_wall1_x = 0.06  # malowany beton
        wall2_x = 4
        attenuation_factor_wall2_x = 0.02  # cegla
        wall1_y = 0
        attenuation_factor_wall1_y = 0.31  # beton porowaty
        wall2_y = 4
        attenuation_factor_wall2_y = 0.1  # drewno
        v_soud = 340.  # m/s
        dt = 0.0001  # s
        initial_intensity = 1e-5  # W/m^2
        threshold_of_hearing = 1e-12  # W/m^2
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
                #plt.plot(x,y,'.', color='g')
            times.append(t)
            #plt.show()

        return np.array(times).mean()
    else:
        return 1000



if __name__ == "__main__":
    # angles = np.arange(0, 2*np.pi, 0.05)
    # for a in angles:
    #     plt.plot(a, reverberation_time(a, x_init, y_init, 500), 'o', color='g')
    #     print a
    # plt.xlabel("Angle [rad]")
    # plt.ylabel("Average reverberation time [s]")

    # for a in range(1,700):
    #     plt.plot(a, reverberation_time(x_init, y_init, angle, a), 'o', color='g')
    #     print a
    # plt.xlabel("Number of iterations")
    # plt.ylabel("Average reverberation time")

    angle = np.pi/4 + np.pi
    x = np.arange(0.1, 3.99, 0.1)
    for a in x:
        plt.plot(a, reverberation_time(angle, a, a, 500), 'o', color='g')
        print a
    plt.xlabel("x")
    plt.ylabel("Average reverberation time")

    plt.show()