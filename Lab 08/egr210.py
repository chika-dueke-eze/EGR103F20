import numpy as np

def truss(arg): 
    #1 required argument of known values
    A = np.array([
                  [np.cos(np.pi/6),0,-np.cos(np.pi/3),0,0,0],
                  [np.sin(np.pi/6),0,np.sin(np.pi/3),0,0,0],
                  [-np.cos(np.pi/6),-1,0,-1,0,0],
                  [-np.sin(np.pi/6),0,0,0,-1,0],
                  [0,1,np.cos(np.pi/3),0,0,0],
                  [0,0,-np.sin(np.pi/3),0,0,-1]
                  ])
    soln = np.linalg.solve(A, arg)
    return soln, A      #return solution and coefficient matrix 


if __name__ == "__main__":
    a = np.array([
                  [67],
                  [56],
                  [34],
                  [20],
                  [2],
                  [20]
                  ]) 
    
    print(truss(a))
