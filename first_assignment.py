from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

def FD(f, x, h):
    fd = (f(x + h) - f(x))/h
    return fd # the value aof the finite difference

def main():
    print("This is the main function of my program")
    x = np.arange(0.0, 2.0, 0.01)
    f = np.sin(2*np.pi*x)
    h = 0.01
    FD(f,x,h)
    plt.plot(x, f)
    plt.plot(x, fd)
    plt.show()
    #FD()
    return

if __name__ == "__main__":
    main()
