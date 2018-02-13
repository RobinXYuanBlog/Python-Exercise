import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()

fig.add_subplot(111)

plt.xlim([1, 7])
plt.ylim([1, 5])

plt.text(1.5, 4, r"$ \alpha_i \beta_j \pi \lambda \omega $", size=25)   # r 不转意

plt.text(3.5, 4, r"$ \sin(0)=\cos(\frac{\pi}{2}) $", size=25)

plt.text(1.5, 2, r"$ \lim_{x \rightarrow y} \frac{1}{x^3} $", size=25)

plt.text(3.5, 2, r"$ \sqrt[4]{x}=\sqrt{y} $", size=25)

plt.show()