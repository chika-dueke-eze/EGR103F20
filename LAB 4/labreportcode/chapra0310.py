# %% Import modules
import numpy as np
import matplotlib.pyplot as plt

#%% define function
def singularity(x, a, n):
    return (x > a) * ((x - a) ** n)

def deflection(x):
    x1 = singularity(x, 0, 4)
    x2 = singularity(x, 5, 4)
    x3 = singularity(x, 8, 3)
    x4 = singularity(x, 7, 2)
    
    u_y = (-5/6)*(x1 - x2) + (5/2)*(x3) + (325/2)*(x4) + (79/12)*(x**3) - 76/3*(x)
    return u_y
#%% set-up for graph

#get array of x- and y- values
x = np.linspace(0, 10, 100)
y = deflection(x)

#create a figure and axis
fig = plt.figure(num=1, clear=True)
ax = fig.add_subplot(1, 1, 1)

#plot the graph
ax.plot(x, y, 'k-')

# Turn the grid on
ax.grid(True)

# Label and title the graph
ax.set(
    xlabel = "Distance Along Beam (ft)",
    ylabel = "Displacement",
    title = "Displacement vs Distance Along Beam (cgd19 )",
) 

# find min
xVals = np.linspace(0, 10, int(1e6))
yVals = deflection(xVals)
yMin = min(yVals)
xMin = xVals[np.where(yVals==yMin)]
print("Max:  {:+0.4e}, {:+0.4e}".format(xMin[0], yMin))

#find max
yMax = max(yVals)
xMax = xVals[np.where(yVals==yMax)]
print("Max:  {:+0.4e}, {:+0.4e}".format(xMax[0], yMax))

# Save the graph as EPS and PDF
fig.savefig('DisplacementPlot.pdf')
fig.savefig('DisplacementPlot.eps')
