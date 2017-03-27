# Basic class declaration for a 
# diffusion object
#

import numpy as np


class ItoDiff:
    def __init__(self, drift, diff, par):
        self.drift = drift
        self.diff = diff
        self.par = par

    def drift_func(self, x, t):
        return self.drift(x, t, self.par)

    def diff_func(self, x, t):
        return self.diff(x, t, self.par)

    def sim(self, dt, T, t0=0):
        t = t0
        while True:
            tau = min(dt, T-t)
            print t
            if t >= T - 1e-12:
                break
            else:
                t += tau

    def sim2(self, T, N, t0=0.):
        dt = (T-t0)/(N-1)
        self.sim(dt,T,t0)

dX = ItoDiff(None,None,None)
dX.sim(0.033,1., 0.5)
print "______________"
print 
print "______________"
dX.sim2(1.,6,0.5)    
