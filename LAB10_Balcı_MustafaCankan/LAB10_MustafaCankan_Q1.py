import numpy as np
import matplotlib.pyplot as plt


initial = np.arange(30,75,5)
bounce = np.array([22,26,29,34,38,40,45,50,52])
fit = np.polyfit(initial,bounce,1)

best_fit = np.polyval(fit,initial)
plt.figure(2)
plt.plot(initial,bounce, 'bo')
plt.plot(initial, best_fit, 'r')
plt.title('Initial Height vs. Bounce Height')
plt.xlabel('Initial Height')
plt.ylabel('Bounce Height')
plt.show()
