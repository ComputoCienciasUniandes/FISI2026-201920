import matplotlib.pyplot as plt
import math

def espiral(n):
    b = n/100.0
    n_points = 200
    delta_theta = 6.0 * math.pi / n_points

    theta = []
    r = []
    x = []
    y = []
    for i in range(n_points):
        theta.append(delta_theta * i)

    for i in range(n_points):
        r.append(theta[i]*b)

    for i in range(n_points):
        x.append(r[i] * math.cos(theta[i]))
        y.append(r[i] * math.sin(theta[i]))


    plt.figure()
    plt.plot(x,y)    
    plt.xlim(-20,20)
    plt.ylim(-20,20)
    plt.savefig('{}.png'.format(n))
    plt.close()

