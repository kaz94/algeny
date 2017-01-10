import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


x_init = 2
y_init = 2
angle = np.pi/4.



def reverberation_time(angle, x_init=2., y_init=2., N=500):
    if angle <= 2*np.pi and angle >= np.pi and x_init >=0 and x_init <=4 and y_init >= 0 and y_init <=4:
        wall1_x = 0
        attenuation_factor_wall1_x = 0.1  # malowany beton
        wall2_x = 4
        attenuation_factor_wall2_x = 0.1  # cegla
        wall1_y = 0
        attenuation_factor_wall1_y = 0.1  # beton porowaty
        wall2_y = 4
        attenuation_factor_wall2_y = 0.1  # drewno
        v_soud = 340.  # m/s
        dt = 0.0001  # s
        initial_intensity = 1e-5  # W/m^2
        threshold_of_hearing = 1e-12  # W/m^2
        times = []
        I_sum = 0.
        for i in range(N):
            propagation_angle = np.random.normal(angle, np.pi/10) #random.uniform(angle-np.pi/6., angle+np.pi/6.)
            x = x_init
            y = y_init
            v_x = v_soud * np.cos(propagation_angle)
            v_y = v_soud * np.sin(propagation_angle)
            t = 0
            I = initial_intensity
            while(I >= threshold_of_hearing):
                if y < 3./4. * y_init:
                    I_sum += I
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

        return np.array(times).mean()+ 1./I_sum/25.
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

    angle = 3./2.*np.pi
    x = np.arange(0.1, 3.99, 0.2)
    plt.subplot('121')
    for a in x:
        #plt.plot(a,1./(40.*reverberation_time(angle, a, 3.99, 500)[1])+reverberation_time(angle, a, 3.99, 500)[0], 'o', color='g')
        F = reverberation_time(angle, a, 3.99, 500)
        plt.plot(a,F, 'o', color='r')
        #plt.plot(a,1./F[1]/25., 'o', color='g')
        print a

    plt.xlabel("x")
    plt.ylabel("Average reverberation time")
    #plt.show()


    angles = np.arange(np.pi, 2.*np.pi, 0.2)
    x=1.
    plt.subplot('122')
    for a in angles:
        # plt.plot(a,1./(40.*reverberation_time(angle, a, 3.99, 500)[1])+reverberation_time(angle, a, 3.99, 500)[0], 'o', color='g')
        F = reverberation_time(a, x, 3.99, 500)
        plt.plot(a, F, 'o', color='r')
        #plt.plot(a, 1./F[1]/25., 'o', color='g')
        print a
    plt.xlabel("angle")
    plt.ylabel("Average reverberation time")
    plt.show()

    '''fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    angles = np.arange(np.pi, 2. * np.pi, 0.2)
    x = np.arange(0.1, 3.99, 0.2)
    X=[]
    A=[]
    F=[]

    for xx in x:
        for a in angles:
            A.append(a)
            X.append(xx)
            F.append(reverberation_time(a, xx, 3.99, 500))
            print(xx)
    plt.plot(A, X, F)
    ax.set_xlabel('angle')
    ax.set_ylabel('x')
    ax.set_zlabel('f dopasowania')
    plt.show()'''

