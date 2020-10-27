import numpy as np

def rotate_2d(theta,x,y):
    theta = theta * (np.pi/180)    #convert from degree to radian
    R = np.array([[np.cos(theta),-np.sin(theta)],[np.sin(theta), np.cos(theta)]])
    coords = np.array([x,y])
    soln = np.linalg.solve(R, coords)
    return soln


if __name__ == "__main__":
    c = rotate_2d(360,np.array([1,1,1]),np.array([1,1,1]))
    print(c)
