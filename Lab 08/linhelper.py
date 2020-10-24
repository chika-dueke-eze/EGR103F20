import numpy as np

def linsolve(A, b, cond_no=2):
    """
    Parameters
    ----------
    A : TYPE 2D Array
        DESCRIPTION; coefficient matrix
    b : TYPE 1D or 2D Array
        DESCRIPTION. 
    cond_no : TYPE, optional
        DESCRIPTION. The default is 2.

    Returns
    -------
    soln--> solution of the linear system
    det--> determinant of the coefficient matrix
    condition_no --> condition number of the coefficient matrix
    """
    try:
        soln = np.linalg.solve(A, b)
        det = "{}".format(np.linalg.det(A))
        condition_no = "{}".format(np.linalg.cond(A, cond_no))
        return soln, float(det), float(condition_no)
    except:
        return None, 0, -1

if __name__ == "__main__":
    a = np.array([[0,-7,5], [0,4,7],[-4,3,-7]])
    b = np.array([[50],[-30],[40]])   
    
    print(linsolve(a, b))
        
        
    
