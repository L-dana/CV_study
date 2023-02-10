##상호상관함수 간단재현

import numpy as np
import matplotlib.pyplot as plt


dt = 0.05
t = np.arange(-7, 7+dt, dt)
xx = ((0 <= t) & (t<2)) * 1.5
yy = ((0 <= t) & (t<3)) * 2.0
r = np.correlate(xx,yy, "same")*dt
plt.plot(t, r)
plt.axis([-7, 7, r.min()-0.5, r.max()+0.5])
plt.grid(True)
plt.tight_layout()
plt.show()
