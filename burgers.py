import numpy as np
import matplotlib.pylab as plt

def icb(x):
    """ This is the initial condition for burgers equation"""
    return 1.-np.cos(2.*np.pi*x)

# This program solves the nonlinear burgers equation

nx = 20
dx = 1.0/float(nx)
twodx = 2.*dx
x = np.arange(nx)*dx

dt = .01
lfirst = True

# Set initial condition
u0 = icb(x)
u = u0.copy()
um = u0.copy()

plt.plot(x, u, 'b-')

# number of time steps
nstep = 50

t = 0.
mom = np.sum(u*dx)

time = [t]
momentum = [mom]

# Loop over the time steps
for istep in range(nstep):
    twodt = 2.*dt
    if lfirst: # Trick to take forward step the first time
        twodt = dt
        lfirst = False
    up = um - u*(np.roll(u, -1) - np.roll(u, 1))*twodt/twodx
    um = u.copy()
    u = up.copy()

    t += dt
    time.append(t)

    # Diagnose momentum
    mom = np.sum(u*dx)
    momentum.append(mom)

    print('Time: ', t, 'Momentum: ', mom)
plt.plot(x, u, 'r-')
plt.show()

plt.plot(time, momentum)
plt.show()
