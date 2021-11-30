import matplotlib.pyplot as plt
import numpy as np 

x = np.array(range(100))
y = x**2
plt.colorbar()
plt.plot(x,y + 5)
plt.show()



