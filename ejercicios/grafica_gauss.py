import matplotlib.pyplot as plt
import math

def genera(n_sigma):
    sigma = n_sigma * 0.05
    n_points = 200
    deltax = 20.0/n_points

    l = list(range(n_points))
    x = []
    for i in l:
        x.append(-10.0 + deltax * i)

    y = []
    for i in x:
        y.append( math.exp(-0.5*i**2/sigma**2))
    
    plt.figure()
    plt.plot(x,y)    
    plt.savefig('{}.png'.format(n_sigma))
    plt.close()

