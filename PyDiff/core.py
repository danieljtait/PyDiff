# Basic class declaration for a 
# diffusion object
#
import numpy as np


class ItoDiffusion:
    def __init__(self, drift, diff, par):
        self.drift = drift
        self.diff = diff
        self.par = par

    def drift_func(self, x, t):
        return self.drift(x, t, self.par)

    def diff_func(self, x, t):
        return self.diff(x, t, self.par)

    def sim(self, x0, dt, T, t0=0):
        t = t0
        rootdt = np.sqrt(dt)
        tt = [t0]
        X = [x0]
        w = np.random.normal()
        while True:
            if dt < T-t:
                tau = dt
                rootTau = rootdt
            else:
                tau = T-t
                rootTau = np.sqrt(tau)

            x = X[-1]
            xnew = x + tau*self.drift_func(x, t) + rootTau*self.diff_func(x,t)*np.random.normal()

            if t >= T - 1e-12:
                break
            
            else:
                X.append(xnew)
                t += tau
                tt.append(t)

        return np.array(tt), np.array(X)

    def sim2(self, x0, T, N, t0=0.):
        dt = (T-t0)/(N-1)
        self.sim(x0,dt,T,t0)

###
# To do:
#  - Make example SDEs
#    - BBridge subclass of SDE with particular sim function 

"""
def a_bb(x,t,par):
    return -x/(1-t)

def b_bb(x,t,par):
    return 1.

def a(x,t,par):
    return 4*x*(par[0]-x**2)

def b(x,t,par):
    return par[1]

s = .1
dX = ItoDiffusion(a_bb,b_bb,None)

x0 = 0.
T = 0.99


import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)

for i in range(10):
    tt, Xt = dX.sim(x0, 0.02, T=T)
    tt = np.concatenate((tt,[T]))
    Xt = np.concatenate((Xt,[0.]))
    print Xt[0]
    ax.plot(tt, Xt, 'k-', alpha=0.2)

plt.show()
"""
