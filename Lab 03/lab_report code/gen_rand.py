# %% Import modules
import numpy as np
import matplotlib.pyplot as plt
import math as m


# %% Seed based on NetID
NetID = input("NetID: ")
seed = 0
for code in map(ord, NetID):
    seed = seed + code

np.random.seed(seed)

# %% Number of numbers
nums = int(input("How many numbers? "))  

# %%Calculate distributions
u_d = np.random.uniform(0, 1, nums) 
n_d = np.random.normal(0, 1, nums)  

# %% Make plots
num_bins = m.ceil(10 * m.log10(nums))

fig = plt.figure(num=1, clear=True)
ax = fig.add_subplot(1, 1, 1)
ax.hist(u_d, num_bins)
ax.set(title="Uniform ({})".format(NetID))    #add (NetID) to graph title
fig.tight_layout()
fig.savefig("UniformPlot.eps")

fig = plt.figure(num=2, clear=True)
ax = fig.add_subplot(1, 1, 1)
ax.hist(n_d, num_bins)
ax.set(title="Normal ({})".format(NetID))
fig.tight_layout()
fig.savefig("NormalPlot.eps")

# %% Print statistics
ud_min = np.amin(u_d)      #to get the min of uniform distribution
ud_avg = np.average(u_d)   #.. ... ... avg .. ....... ............
ud_max = np.amax(u_d)      #.. ... ... max .. ....... ............

nd_min = np.amin(n_d)      #to get the min of normal distribution
nd_avg = np.average(n_d)   #.. ... ... avg .. ....... ............
nd_max = np.amax(n_d)      #.. ... ... max .. ....... ............


print("Uniform: min: {:+0.3e} avg: {:+0.3e} max: {:+0.3e}".format(ud_min, ud_avg, ud_max))
print("Normal:  min: {:+0.3e} avg: {:+0.3e} max: {:+0.3e}".format(nd_min, nd_avg, nd_max))
